from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

# Create your views here.

menu = ["Глагна", "О сайте", "Добавить статью", "Обратная связь", "Войти"]

def index(request):
    posts = Thought.objects.all()
    return render(request, 'thoughts/index.html', {'posts': posts, 'menu': menu, 'title': 'Glagna'})

def about(request):
    return render(request, 'thoughts/about.html', {'menu': menu, 'title': 'О сайте'})

def categories(request, catid):
    if request.POST:
        print(request.POST)
    return HttpResponse(f"<h1>Статьи по категориям </h1><p>{catid}</p>")

def archive(request, year):
    if int(year) > 2020:
        return redirect('glagna', permanent=True)
        #raise Http404

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound(f"<h1>Страница не найдена, сорян! :С</h1>")

