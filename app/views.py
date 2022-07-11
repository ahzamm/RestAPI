import json
from django.shortcuts import render
from django.http import JsonResponse
from .models import Employee
from .serializers import EmployeeSerializer
# Create your views here.


def employeeListView(request):
    employee = Employee.objects.all()
    s = EmployeeSerializer(employee, many=True)

    return JsonResponse(s.data, safe=False)