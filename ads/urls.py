from django.urls import path
from . import views

app_name = 'ads'
urlpatterns = [
    path('', views.AdsList.as_view(), name='ads_list'),
    path('<int:pk>', views.AdDetailView.as_view(), name='ads_detail'),
    path('create', views.AdCreateView.as_view(), name='ads_create'),
    path('<int:pk>/update', views.AdUpdateView.as_view(), name='ads_update'),
    path('<int:pk>/delete', views.AdDeleteView.as_view(), name='ads_delete'),
]