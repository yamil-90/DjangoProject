from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class SoloList(LoginRequiredMixin, View):
    template_name = 'solo/index.html'

    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        if not request.POST.get('field1') or not request.POST.get('field2'):
            return render(request, self.template_name, {'message': 'Please enter both fields'})
        input1 = request.POST.get('field1').rstrip()
        input2 = request.POST.get('field2').rstrip()
        result = " ".join([input1, input2])
        result = result[::-1].title()
        return render(request, self.template_name, {'message': result})