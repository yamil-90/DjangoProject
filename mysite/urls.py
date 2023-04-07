from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('css', views.css, name="css"),
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('cats/', include('cats.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
