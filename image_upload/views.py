#from django.shortcuts import render

# Create your views here.



from rest_framework import viewsets
from .models import UploadedImage
from .serializers import UploadedImageSerializer

class UploadedImageViewSet(viewsets.ModelViewSet):
    queryset = UploadedImage.objects.all()
    serializer_class = UploadedImageSerializer