from .models import Employee
from rest_framework import serializers


class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    email = serializers.EmailField(max_length=30)
    password = serializers.CharField(max_length=30)
    phone = serializers.CharField(max_length=11)

    def create(self, validation_data):
        """This function is for insert data in to table when POST request is called without providing id argumment

        Args:
            validation_data (dictionary): data entries for new user

        Returns:
            json: it return json form of the provided data
        """
        return Employee.objects.create(**validation_data)


    def update(self, employee, validation_data):
        newEmployee = Employee(**validation_data)
        newEmployee.id = employee.id
        newEmployee.save()
        return newEmployee


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=10)
    email = serializers.EmailField()
    last_login = serializers.DateTimeField()
    date_joined = serializers.DateTimeField()