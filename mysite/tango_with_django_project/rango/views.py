from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    response = '<a href = "about/">"Go to about Page"</a> Rango says hey there partner'
    return HttpResponse(response)

def about(request):
    response = '<a href = "/rango">"Back to index page"</a> "Rango says here is the about page"'
    return HttpResponse(response)