from .models import Employee
from rest_framework import serializers


class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    email = serializers.EmailField(max_length=30)
    password = serializers.CharField(max_length=30)
    phone = serializers.CharField(max_length=11)

    def create(self, validation_data):
        print('create method called')
        print(validation_data)
        print(Employee.objects.create(**validation_data))
        return Employee.objects.create(**validation_data)


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=10)
    email = serializers.EmailField()
    last_login = serializers.DateTimeField()
    date_joined = serializers.DateTimeField()