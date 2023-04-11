from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    resp = HttpResponse("Hello, world. You're at the hello index.")
    resp.set_cookie('dj4e_cookie', '05ede5ce', max_age=1000)
    return resp