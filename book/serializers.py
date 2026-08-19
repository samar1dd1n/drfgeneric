from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'

    def validate(self, data):
        title = data.get('title')

        if title and title.isdigit():
            raise ValidationError(
                'Title raqamlardan iborat bo‘lmasin'
            )

        return data
