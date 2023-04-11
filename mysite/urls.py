from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='home/main.html')),
    path('css', views.css, name="css"),
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('cats/', include('cats.urls')),
    path('hello/', include('hello.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
