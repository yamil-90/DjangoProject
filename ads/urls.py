from django.urls import path
from . import views

app_name = 'ads'
urlpatterns = [
    path('', views.AdsList.as_view(), name='ads_list'),
    path('ad/<int:pk>', views.AdDetailView.as_view(), name='ads_detail'),
    path('ad/create', views.AdCreateView.as_view(), name='ads_create'),
    path('ad/<int:pk>/update', views.AdUpdateView.as_view(), name='ads_update'),
    path('ad/<int:pk>/delete', views.AdDeleteView.as_view(), name='ads_delete'),
]