from django.shortcuts import render

# Create your views here.
from .models import Question, Choice

# Get questions


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
