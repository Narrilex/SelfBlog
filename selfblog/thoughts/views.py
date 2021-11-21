from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return HttpResponse("Страница приложения thoughts")

def categories(request, catid):
    return HttpResponse(f"<h1>Статьи по категориям </h1><p>{catid}</p>")

def archive(request, year):
    if int(year) > 2020:
        return redirect('glagna', permanent=True)
        #raise Http404

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound(f"<h1>Страница не найдена, сорян! :С</h1>")

