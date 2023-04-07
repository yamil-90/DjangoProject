from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Cat

# Create your views here.

class CatListViews(View):
    model = Cat

def detail(request, cat_id):
    return HttpResponse("detail of cat %s" % cat_id)

def create(request):
    return HttpResponse("create a cat")

def update(request, cat_id):
    return HttpResponse("update cat %s" % cat_id)

def delete(request, cat_id):
    return HttpResponse("delete cat %s" % cat_id)


