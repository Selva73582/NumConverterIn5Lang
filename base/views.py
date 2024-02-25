# # views.py
# views.py

import os
import string
import random
from django.conf import settings
from django.http import FileResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from gtts import gTTS
from .forms import NumberForm
from .serializers import NumberConversionSerializer


def gemini(num):
    content = "I've developed an artificial intelligence training platform that converts numbers to letters in five languages. When a user inputs a number, such as " + str(num) + ", the system should generate the corresponding text in English, Tamil, Korean, Chinese, and Japanese. Please avoid saying it's impossible; give your best effort. I require the output in the format ['english', 'tamil', 'korean', 'chinese', 'japanese']. Only provide the output for that specific number—no additional information. Ensure the output is correct; do not provide an empty response. If the initial output is incorrect, please make another attempt.i need all that five languages,all 5 langages need to be included"

    import google.generativeai as genai
    import os

    os.environ['GOOGLE_API_KEY'] = 'AIzaSyB2hRDTNDmqDGe0FXZOeGdoLTsl4foLa4M'
    genai.configure(api_key='AIzaSyB2hRDTNDmqDGe0FXZOeGdoLTsl4foLa4M')
    genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(content)
    parts = response.parts

    text_content = ''.join([part.text for part in parts])

    
    output_list = eval(text_content)
    return output_list



@api_view(['POST'])
def number_conversion(request):
    nums = None
    file_names = {}

    try:
        form = NumberForm(request.data)
        if form.is_valid():
            num = form.cleaned_data['inputInteger']
            nums = gemini(num)
            
            language = {0: "English", 1: "Tamil", 2: "Korean", 3: "Chinese", 4: "Japanese"}
            
            for i in range(len(nums)):
                lang = language[i]
                txt = nums[i]
                lang_code = {"English": "en", "Tamil": "ta", "Korean": "ko", "Chinese": "zh", "Japanese": "ja"}
                tts = gTTS(txt, lang=lang_code[lang])
                file_name = f"{''.join(random.choice(string.ascii_lowercase) for _ in range(10))}.mp3"
                file_path = os.path.join(settings.BASE_DIR, "loads", file_name)
                tts.save(file_path)
                file_names[lang] = file_name

            # Serialize the response data
            serializer = NumberConversionSerializer(data={'nums': nums, 'file_names': file_names})
            if serializer.is_valid():
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response({'error': 'Invalid data provided.'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def play_sound(request, file_name):
    file_path = os.path.join(settings.BASE_DIR, "loads", file_name)
    response = FileResponse(open(file_path, 'rb'), content_type='audio/mpeg')
    return response


@api_view(['GET'])
def download_sound(request, file_name):
    file_path = os.path.join(settings.BASE_DIR, "loads", file_name)
    response = FileResponse(open(file_path, 'rb'), content_type='audio/mpeg')
    response['Content-Disposition'] = f'attachment; filename="{file_name}"'
    return response

# from django.shortcuts import render
# from . import ai
# from .forms import NumberForm
# import string
# import random
# from gtts import gTTS
# import os
# from django.http import FileResponse
# from django.conf import settings  

# def numberConversion(request):
#     nums = None
#     file_names = {}

#     try:
#         if request.method == "POST":
#             form = NumberForm(request.POST)
            
#             if form.is_valid():
#                 num = form.cleaned_data['inputInteger']
#                 nums = ai.gemini(num)
                
#                 language = {0: "English", 1: "Tamil", 2: "Korean", 3: "Chinese", 4: "Japanese"}
                
#                 for i in range(len(nums)):
#                     lang = language[i]
#                     txt = nums[i]
#                     lang_code = {"English": "en", "Tamil": "ta", "Korean": "ko", "Chinese": "zh", "Japanese": "ja"}
#                     tts = gTTS(txt, lang=lang_code[lang])
#                     file_name = f"{''.join(random.choice(string.ascii_lowercase) for _ in range(10))}.mp3"
#                     file_path = os.path.join(settings.BASE_DIR, "loads", file_name)
#                     tts.save(file_path)
#                     file_names[lang] = file_name

#         else:
#             form = NumberForm()

#         return render(request, "base/result_template.html", {"form": form, "nums": nums, "file_names": file_names})
#     except:
#         return render(request, "base/result_template.html", {"form": form, "nums": nums, "file_names": file_names})


# def play_sound(request, file_name):
#     file_path = os.path.join(settings.BASE_DIR, "loads", file_name)
#     response = FileResponse(open(file_path, 'rb'), content_type='audio/mpeg')
#     return response

# def download_sound(request, file_name):
#     file_path = os.path.join(settings.BASE_DIR, "loads", file_name)
#     response = FileResponse(open(file_path, 'rb'), content_type='audio/mpeg')
#     response['Content-Disposition'] = f'attachment; filename="{file_name}"'
#     return response



