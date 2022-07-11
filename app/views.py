import json
from django.shortcuts import render
from django.http import JsonResponse
from .models import Employee
from .serializers import EmployeeSerializer, UserSerializer
from django.contrib.auth.models import User
# Create your views here.


def employeeListView(request):
    employee = Employee.objects.all()
    s = EmployeeSerializer(employee, many=True)
    return JsonResponse(s.data, safe=False)


def userListView(request):
    users = User.objects.all()
    u = UserSerializer(users, many=True)
    return JsonResponse(u.data, safe=False)