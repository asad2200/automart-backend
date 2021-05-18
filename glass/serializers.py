from rest_framework import serializers
from .models import Car, Company, Model, Glass


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name']


class CarSerializer(serializers.ModelSerializer):
    company = serializers.StringRelatedField()

    class Meta:
        model = Car
        fields = ['id', 'name', 'company']


class ModelSerializer(serializers.ModelSerializer):
    car = serializers.StringRelatedField()

    class Meta:
        model = Model
        fields = ['id', 'name', 'car']


class GlassSerializer(serializers.ModelSerializer):
    car = serializers.StringRelatedField()
    model = serializers.StringRelatedField()

    class Meta:
        model = Glass
        fields = ['id', 'name', 'car', 'model', 'description', 'price']
