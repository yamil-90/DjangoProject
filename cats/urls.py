from django.urls import path

from . import views

app_name = 'cats'
urlpatterns = [
    path('', views.CatListViews.as_view(), name="index"),
    path('<int:cat_id>/', views.detail, name="detail"),
    path('create', views.create, name="create"),
    path('<int:cat_id>/update', views.update, name="update"),
    path('<int:cat_id>/delete', views.delete, name="delete"),
]
