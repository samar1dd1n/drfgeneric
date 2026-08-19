from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import BookCRUD


router = DefaultRouter()

router.register('books', BookCRUD, basename='books')


urlpatterns = [
    path('', include(router.urls)),
]