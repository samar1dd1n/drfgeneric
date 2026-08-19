from django.urls import path
from .views import (
    CarListCreateAPIView,
    CarRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path('cars/', CarListCreateAPIView.as_view()),
    path('cars/<int:pk>/', CarRetrieveUpdateDestroyAPIView.as_view()),
]