from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Car

# Create your views here.

class CarsList(ListView):
    model = Car 
    template_name = 'autos/car_list.html'

class CarsDetail(DetailView):
    model = Car
    template_name = 'autos/car_detail.html'

class CarsCreate(CreateView):
    model = Car
    fields = '__all__'
    success_url = reverse_lazy('autos:cars_list')

class CarsUpdate(UpdateView):
    model = Car
    fields = '__all__'
    success_url = reverse_lazy('autos:cars_list')

class CarsDelete(DeleteView):
    model = Car
    fields = '__all__'
    success_url = reverse_lazy('autos:cars_list')