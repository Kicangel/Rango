from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    response = '<a href = "about/">"About"</a> Rango says hey there partner'
    return HttpResponse(response)

def about(request):
    response = '<a href = "/rango">"Index"</a> "Rango says here is the about page"'
    return HttpResponse(response)