from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.TextField(null=True , blank=True)
    email = models.EmailField(null=True , blank=True)
    

class Product(models.Model):
    pName = models.CharField(max_length=50)
    pDate = models.DateField()    