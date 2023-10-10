from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CarSerializer, CategorySerializer
from .models import Car, Category

# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer