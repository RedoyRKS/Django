from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Car(models.Model):
    car_name = models.CharField(max_length=50)
    car_speed = models.IntegerField(default=50)

    def __str__(self) -> str:
        return self.car_name
    
    
