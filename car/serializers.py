from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import  Car


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = '__all__'

    def validate(self, data):
        name = data.get('title')

        if name and name.isdigit():
            raise ValidationError(
                'Nomi raqamlardan iborat bo‘lmasin'
            )

        return data
