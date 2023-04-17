from django.urls import path

from . import views


app_name = 'autos'
urlpatterns = [
    path('', views.CarsList.as_view(), name='cars_list'),
    path('main/<int:pk>', views.CarsDetail.as_view(), name='cars_detail'),
    path('main/create', views.CarsCreate.as_view(), name='cars_create'),
    path('main/<int:pk>/update', views.CarsUpdate.as_view(), name='cars_update'),
    path('main/<int:pk>/delete', views.CarsDelete.as_view(), name='cars_delete'),
    path('lookup', views.MakeList.as_view(), name='make_list'),
    path('lookup/<int:pk>', views.MakeDetail.as_view(), name='make_detail'),
    path('lookup/create', views.MakeCreate.as_view(), name='make_create'),
    path('lookup/<int:pk>/update', views.MakeUpdate.as_view(), name='make_update'),
    path('lookup/<int:pk>/delete', views.MakeDelete.as_view(), name='make_delete'),
]