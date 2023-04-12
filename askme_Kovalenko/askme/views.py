from . import models
from django.shortcuts import render
from django.http import HttpRequest

def index(request):
    content = {'quastions' : models.quastions}
    return render(request, 'index.html', content)


def question(request):
    return render(request, 'question.html')


def login(request):
    return render(request, 'login.html')


def registration(request):
    return render(request, 'registration.html')