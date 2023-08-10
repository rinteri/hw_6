from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Мой сайт</h1>')

def ind(request):
    return HttpResponse('<h1>Hello world</h1>')

def hw(request):
    return HttpResponse('Домашка по 4 занятию')
