from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
# Create your views here.

def index(request):
    latest_que_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_que_list])
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse('You are looking at QUESTION: %d' % question_id)

def result(request, question_id):
        return HttpResponse('You are looking at result of a  QUESTION: %d' % question_id)

def vote(request, question_id):
    return HttpResponse('You are voting on QUESTION: %d' % question_id)
