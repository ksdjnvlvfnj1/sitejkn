from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def main(request):
    return render(request, "index.html")

def services(request):
    return render(request, "services.html")

def specialists(request):
    return render(request, "specialists.html")

def contacts(request):
    return render(request, "contacts.html")
# Create your views here.
