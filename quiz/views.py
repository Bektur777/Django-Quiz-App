from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.views.generic import ListView, DetailView

from .models import *

# Create your views here.


class QuizView(ListView):
    model = Quiz
    queryset = Quiz.objects.all().order_by('-id')


class QuizDetailView(DetailView):
    model = Quiz
    context_object_name = 'quiz'
    slug_field = 'slug'
    template_name = 'quiz/question_detail.html'


@require_POST
def checking(request):
    answer = [request.POST.get('checkRadios')]
    request.session['info'] = list(answer)
    request.session.modified = True
    return redirect('get_answers')


def get_answers(request):
    context = {'point': request.session.get('info')}
    return render(request, 'quiz/result.html', context)
