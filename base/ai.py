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



""" AIzaSyB2hRDTNDmqDGe0FXZOeGdoLTsl4foLa4M """


   # content="i have created the social media platform were users can enter their skills , one of the user has given skills as"+str(list)+"so i need to recommaned him a good new skills,you need to give skills according to his sector of learning, so please give me a new skill that user needs like this strictly ['skill1','skill2','skill3']"
#     content="""In the health control platform, users can input their weight (in kg), height (in cm), age, and gender (assuming normal human conditions) using metric units. A sample user provided the following details: """+ str(list)+""". The platform generates recommendations based on the entered information, adhering to the strict resolution format: ['increase weight', 'increase height', 'decrease weight', 'decrease height'].

# Recommendations are determined through analysis, taking into account the user's details. For instance, the system might suggest: ['increase weight', 'decrease height']. Users are advised to follow these recommendations diligently for optimal health management.
# """