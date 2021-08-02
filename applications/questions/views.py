from django.views.generic import View
from django.shortcuts import render, redirect
from .models import Question
from .forms import QuestionForm
# Create your views here.


class QuestionView(View):

    def get(self, request):
        question = Question.objects.all()
        return render(request, 'main.html', context={'question': question})

    def post(self, request):
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(form)
        return render(request, 'main.html', context={'form': form})