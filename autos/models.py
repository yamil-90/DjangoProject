from django.db import models

# Create your models here.

class Make(models.Model):
    name = models.CharField(max_length=200)

class Car(models.Model):
    nickname = models.CharField(max_length=200)
    make = models.ForeignKey(Make, on_delete=models.CASCADE)
    mileage = models.IntegerField(default=0)
    comments = models.TextField(max_length=500)

    
