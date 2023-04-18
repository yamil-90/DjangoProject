from django.urls import path

from . import views

app_name = 'cats'
urlpatterns = [
    path('', views.CatList.as_view(), name="cats_list"),
    path('main/<int:pk>/', views.CatDetail.as_view(), name="cats_detail"),
    path('main/create/', views.CatCreate.as_view(), name="cats_create"),
    path('main/<int:pk>/update', views.CatUpdate.as_view(), name="cats_update"),
    path('main/<int:pk>/delete', views.CatDelete.as_view(), name="cats_delete"),
    path('lookup/', views.BreedList.as_view(), name='breed_list'),
    path('lookup/<int:pk>', views.BreedDetail.as_view(), name='breed_detail'),
    path('lookup/create', views.BreedCreate.as_view(), name='breed_create'),
    path('lookup/<int:pk>/update', views.BreedUpdate.as_view(), name='breed_update'),
    path('lookup/<int:pk>/delete', views.BreedDelete.as_view(), name='breed_delete'),
]
