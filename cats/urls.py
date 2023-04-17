from django.urls import path

from . import views

app_name = 'cats'
urlpatterns = [
    path('', views.CatListViews.as_view(), name="index"),
    path('<int:cat_id>/', views.detail, name="cats_detail"),
    path('create', views.create, name="cats_create"),
    path('<int:cat_id>/update', views.update, name="cats_update"),
    path('<int:cat_id>/delete', views.delete, name="cats_delete"),
]
