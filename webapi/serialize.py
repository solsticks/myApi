from rest_framework import serializers
from .models import employees, product


class employeesSerializers(serializers.ModelSerializer):
    class Meta:
        model = employees
        fields = '__all__'


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = '__all__'
