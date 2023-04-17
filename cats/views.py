from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Cat

# Create your views here.

class CatListViews(ListView):
    model = Cat
    template_name = 'cats/index.html'

def detail(request, cat_id):
    return HttpResponse("detail of cat %s" % cat_id)

def create(request):
    return HttpResponse("create a cat")

def update(request, cat_id):
    return HttpResponse("update cat %s" % cat_id)

def delete(request, cat_id):
    return HttpResponse("delete cat %s" % cat_id)


