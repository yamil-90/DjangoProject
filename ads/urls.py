from django.urls import path
from . import views

app_name = 'ads'
urlpatterns = [
    path('', views.AdsList.as_view(), name='ads_list'),
    path('<int:pk>', views.AdDetailView.as_view(), name='ads_detail'),
    path('create', views.AdCreateView.as_view(), name='ads_create'),
    path('ad_picture/<int:pk>', views.stream_file, name='ads_picture'),
    path('<int:pk>/update', views.AdUpdateView.as_view(), name='ads_update'),
    path('<int:pk>/delete', views.AdDeleteView.as_view(), name='ads_delete'),
    path('comment/<int:pk>/create', views.CommentCreateView.as_view(), name='ads_comment_create'),
    path('comment/<int:pk>/delete', views.CommentDeleteView.as_view(), name='ads_comment_delete'),
    path('<int:pk>/favorite', views.AddFavoriteView.as_view(), name='ad_favorite'),
    path('<int:pk>/unfavorite', views.DeleteFavoriteView.as_view(), name='ad_unfavorite'),
]