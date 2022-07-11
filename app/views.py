import jsonw
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from iniconfig import ParseError
from .models import Employee
from .serializers import EmployeeSerializer, UserSerializer
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
# Create your views here.

@csrf_exempt
def employeeListView(request):
    if request.method == 'GET':
        employee = Employee.objects.all()
        s = EmployeeSerializer(employee, many=True)
        return JsonResponse(s.data, safe=False)

    elif request.method=='POST':
        parser = JSONParser().parse(request)
        serializer = EmployeeSerializer(data=parser)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse(serializer.errors, safe=False)

def userListView(request):
    users = User.objects.all()
    u = UserSerializer(users, many=True)
    return JsonResponse(u.data, safe=False)