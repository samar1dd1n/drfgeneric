from django.shortcuts import render
from rest_framework import status , generics
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.exceptions import NotFound
from rest_framework.generics import get_object_or_404
from .models import Car
from .serializers import CarSerializer
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView

class CarListCreateAPIView(ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    