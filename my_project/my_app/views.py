from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("this is my django project practices demo")

def form(request):
    return HttpResponse("this is my django project practices demo")


def login(request):
    return HttpResponse("this is my django project practices demo")
