from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Car, Make

# Create your views here.

class CarsList(LoginRequiredMixin, ListView):
    model = Car 

    def get(self, request):
        cars_list = Car.objects.all()
        makes_list = Make.objects.all()
        context = {
            'object_list' : cars_list,
            'makes_list' : makes_list
        }
        return render(request, 'autos/car_list.html', context)


class CarsDetail(LoginRequiredMixin, DetailView):
    model = Car

class CarsCreate(LoginRequiredMixin, CreateView):
    model = Car
    fields = '__all__'
    success_url = reverse_lazy('autos:cars_list')

class CarsUpdate(LoginRequiredMixin, UpdateView):
    model = Car
    fields = '__all__'
    success_url = reverse_lazy('autos:cars_list')

class CarsDelete(LoginRequiredMixin, DeleteView):
    model = Car
    fields = '__all__'
    success_url = reverse_lazy('autos:cars_list')

class MakeList(LoginRequiredMixin, ListView):
    model = Make 

class MakeDetail(LoginRequiredMixin, DetailView):
    model = Make

class MakeCreate(LoginRequiredMixin, CreateView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:cars_list')

class MakeUpdate(LoginRequiredMixin, UpdateView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:cars_list')

class MakeDelete(LoginRequiredMixin, DeleteView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:cars_list')