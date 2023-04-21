from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Ad
from django.conf import settings
from django.urls import reverse_lazy
from .owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView

# Create your views here.

class AdsList(OwnerListView):
    print(settings.APP_NAME)
    model = Ad

class AdDetailView(OwnerDetailView):
    model = Ad
    success_url=reverse_lazy('ads:ads_list')

class AdCreateView(OwnerCreateView):
    model = Ad
    success_url=reverse_lazy('ads:ads_list')
    fields = ['title', 'price', 'text']

class AdUpdateView(OwnerUpdateView):
    model = Ad
    success_url=reverse_lazy('ads:ads_list')
    fields = ['title', 'price', 'text']

class AdDeleteView(OwnerDeleteView):
    model = Ad
    success_url=reverse_lazy('ads:ads_list')
