from .models import Cat, Breed
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from django.shortcuts import render

# Create your views here.

class CatList(ListView):
    model = Cat
    def get(self, request):
        cats_list = Cat.objects.all()
        breeds_list = Breed.objects.all()
        context = {
            'object_list' : cats_list,
            'breeds_list' : breeds_list
        }
        return render(request, 'cats/cat_list.html', context)

class CatDetail(DetailView):
    model = Cat

class CatCreate(CreateView):
    model = Cat
    fields = '__all__'
    success_url = '/cats/'

class CatUpdate(UpdateView):
    model = Cat
    fields = '__all__'
    success_url = '/cats/'

class CatDelete(DeleteView):
    model = Cat
    success_url = '/cats/'

class BreedList(ListView):
    model = Breed

class BreedDetail(DetailView):
    model = Breed

class BreedCreate(CreateView):
    model = Breed
    fields = '__all__'
    success_url = '/cats/lookup/'

class BreedUpdate(UpdateView):
    model = Breed
    fields = '__all__'
    success_url = '/cats/lookup/'

class BreedDelete(DeleteView):
    model = Breed
    success_url = '/cats/lookup/'





