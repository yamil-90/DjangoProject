from django.contrib import admin
from django.urls import path, include, re_path
# from django.conf import settings
# from django.conf.urls.static import static
from django.conf.urls.static import serve
from django.views.generic import TemplateView
from . import views
import os

urlpatterns = [
    path('', TemplateView.as_view(template_name='home/main.html'), name='home'),
    path('css', views.css, name="css"),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), 
    path('polls/', include('polls.urls'), name='polls'),
    path('cats/', include('cats.urls', namespace='cats')),
    path('hello/', include('hello.urls')),
    path('autos/', include('autos.urls', namespace='autos')),
    path('ads/', include('ads.urls', namespace='ads')),
    # path('__debug__/', include('debug_toolbar.urls')),
] 
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
urlpatterns += [
    re_path(r'^site/(?P<path>.*)$', serve,
        {'document_root': os.path.join(BASE_DIR, 'site'),
         'show_indexes': True},
        name='site_path'
        ),
]

# Serve the favicon - Keep for later
urlpatterns += [
    path('favicon.ico', serve, {
            'path': 'favicon.ico',
            'document_root': os.path.join(BASE_DIR, 'home/static'),
        }
    ),
]

# Switch to social login if it is configured - Keep for later
try:
    from . import github_settings
    social_login = 'registration/login_social.html'
    urlpatterns.insert(0,
                       path('accounts/login/', auth_views.LoginView.as_view(template_name=social_login))
                       )
    print('Using', social_login, 'as the login template')
except:
    print('Using registration/login.html as the login template')