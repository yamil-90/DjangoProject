from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Poll

def index(request):
	polls = Poll.objects.all()
	return render(request, 'polls/index.html', {'polls': polls})

def detail(request, poll_id):
    poll = Poll.objects.get(id=poll_id)

    if(not poll):
        raise Http404("Poll does not exist")

    return render(request, 'polls/detail.html', {'poll': poll})
