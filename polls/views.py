from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Question

def index(request):
	questions = Question.objects.all()
	return render(request, 'polls/index.html', {'questions': questions})

def detail(request, question_id):
    try:
        question = Question.objects.get(id=question_id)
    except question.DoesNotExist:
        raise Http404("Question does not exist :(")
    
    return render(request, 'questions/detail.html', {'question': question})
