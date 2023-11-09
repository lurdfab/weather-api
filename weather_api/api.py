from django.shortcuts import render
from .serializers import DescriptionSerializer
from .models import Description
from rest_framework import viewsets

# Create your views here.

#with viewsets we don't need to specify the endpoints like we do with APIView and GenericAPIVIew cos it handles these operations automatically.
class DescriptionViewSet(viewsets.ModelViewSet):
    queryset = Description.objects.all()
    serializer_class = DescriptionSerializer

