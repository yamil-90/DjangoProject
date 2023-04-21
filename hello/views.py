from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.

def index(request):
    count = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = count
    logged = 'you are logged' if request.user.is_authenticated else 'you are not logged in'

    response = HttpResponse("Hello, world. You're at the hello index.<br>view count="+str(count)+"<br>" + logged + "<br><a href='/'>go home</a>")
    response.set_cookie('dj4e_cookie', '05ede5ce', max_age=1000)
    return response