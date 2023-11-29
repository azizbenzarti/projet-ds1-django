# your_project_name/urls.py

from django.urls import path
from apiApp.views import process_form, get_generated_string

urlpatterns = [
    path('api/process_form/', process_form, name='process_form'),
    path('api/get_generated_string/', get_generated_string, name='get_generated_string'),
]
