from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from .models import Question, Choice

class IndexView(ListView):
    
    template_name = 'polls/index.html'
    context_object_name = 'latest_questions_list'
    
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(DetailView):
    model = Question
    template_name = 'polls/results.html'

# class Vote(DetailView):
#     model = Question
#     def post(self):
#         try:
#             selected_choice = self.model.choice_set.get(pk=request.POST['choice'])
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def owner(request):
    return HttpResponse("Hello, world. 05ede5ce is the polls index.")

def cookie(request):
    print(request.COOKIES)
    response = HttpResponse("this is the cookies page where we set some cookies")
    response.set_cookie('cookie', 'value of the cookie, if no max_age is set then it wont expire until the browser is closed')
    response.set_cookie('temporal_cookie', 'value of the temporal cookie 2', max_age=60)
    return response