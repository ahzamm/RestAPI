from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    vxvx