from dataclasses import field
from rest_framework import serializers
from .models import Car, Employer

class CarSerializier(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
        # fields = ["model", "brand"]


class EmployerSerializier(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = '__all__'


