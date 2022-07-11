from .models import Employee
from rest_framework import serializers


class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    email = serializers.EmailField(max_length=30)
    password = serializers.CharField(max_length=30)
    phone = serializers.CharField(max_length=11)


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=10)
    email = serializers.EmailField()
    last_login = serializers.DateTimeField()
    date_joined = serializers.DateTimeField()