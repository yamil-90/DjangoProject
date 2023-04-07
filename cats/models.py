from django.db import models

# Create your models here.

class Cat(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.CharField(max_length=100, null=True, blank=True )
    description = models.TextField()
    photo_url = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.name
