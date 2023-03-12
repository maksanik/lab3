from django.http import HttpResponse
from .models import Article
from django.shortcuts import render

def home(request):
    return HttpResponse('Привет, Мир!')
def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})