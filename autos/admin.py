from django.contrib import admin
from .models import Car, Make

# Register your models here.

admin.site.register(Make) 
admin.site.register(Car)