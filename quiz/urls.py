from django.urls import path
from .views import *

urlpatterns = [
    path('', QuizView.as_view(), name='quizzes'),
    path('result/', checking, name='checking'),
    path('finish/', get_answers, name='get_answers'),
    path('<slug:slug>', QuizDetailView.as_view(), name='question_detail'),

]
