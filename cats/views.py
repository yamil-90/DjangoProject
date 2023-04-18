from .models import Cat, Breed
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.

class CatList(LoginRequiredMixin, ListView):
    model = Cat
    def get(self, request):
        cats_list = Cat.objects.all()
        breeds_list = Breed.objects.all()
        context = {
            'object_list' : cats_list,
            'breeds_list' : breeds_list
        }
        return render(request, 'cats/cat_list.html', context)

class CatDetail(LoginRequiredMixin, DetailView):
    model = Cat

class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:cats_list')

class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:cats_list')

class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    success_url = reverse_lazy('cats:cats_list')

class BreedList(LoginRequiredMixin, ListView):
    model = Breed

class BreedDetail(LoginRequiredMixin, DetailView):
    model = Breed

class BreedCreate(LoginRequiredMixin, CreateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:cats_list')

class BreedUpdate(LoginRequiredMixin, UpdateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:cats_list')

class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed
    success_url = reverse_lazy('cats:cats_list')





