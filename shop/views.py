from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render (request, 'index.html')

def about(request):
    return render (request, 'about.html')

def contact(request):
    return render (request, 'basic.html')

def tracker(request):
    return HttpResponse("Tracker")

def search(request):
    return HttpResponse("Search")

def productView(request):
    return HttpResponse("ProdView")

def checkout(request):
    return HttpResponse("CheckOut")
