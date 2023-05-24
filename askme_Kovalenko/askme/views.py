from . import models
from django.shortcuts import render
from django.http import HttpRequest

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request, **kwargs):
    pk = kwargs.get('pk', 1) or 1
    data, paginator = select_page(Question.objects.new().all(), pk)
    return render(request, "index.html", {'questions': data, 'paginator': paginator})


def select_page(list_item, page):
    paginator = Paginator(list_item, 10)
    try:
        return paginator.page(page), paginator
    except PageNotAnInteger:
        raise Http404("Page not an integer")
    except EmptyPage:
        return paginator.page(paginator.num_pages), paginator

def index(request):
    content = {'quastions' : models.quastions}
    return render(request, 'index.html', content)


def question(request):
    return render(request, 'question.html')


def login(request):
    return render(request, 'login.html')


def registration(request):
    return render(request, 'registration.html')


def ask(request):
    return render(request, 'ask.html')


def settings(request):
    return render(request, 'settings.html')


def tag(request):
    return render(request, 'tag.html')