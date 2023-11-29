# your_app_name/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import FormData
from .serializers import FormDataSerializer

@api_view(['POST'])
def process_form(request):
    serializer = FormDataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        # Adjust the logic for generating the string based on your requirements
        generated_string = f"Generated string: {serializer.data['name']} - {serializer.data['age']}"
        return Response({'result': generated_string})
    return Response({'error': 'Invalid data'})

@api_view(['GET'])
def get_generated_string(request):
    # Fetch the latest form data and generate the string
    latest_form_data = FormData.objects.last()
    if latest_form_data:
        generated_string = f"Generated string: {latest_form_data.name} - {latest_form_data.age}"
        return Response({'result': generated_string})
    return Response({'error': 'No data available'})
