from django.urls import path
from . import views
# urlpatterns in urls.py

from .views import *

urlpatterns = [
    path('api/number-conversion/', number_conversion, name='number_conversion'),
    path('api/play-sound/<str:file_name>/', play_sound, name='play_sound'),
    path('api/download-sound/<str:file_name>/', download_sound, name='download_sound'),
    # ... other paths ...
]
