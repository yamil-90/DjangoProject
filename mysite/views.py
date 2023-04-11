from django.shortcuts import render
from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Hello, world! This is the home page.")

def css(request):
    return render(request, 'css/index.html')

def blocks(request):
    return render(request, 'css/blocks.css')