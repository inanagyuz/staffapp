from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):     
    return HttpResponse("Anasayfa")

def about(request):
    return HttpResponse("About")

def contact(request):
    return HttpResponse("iletişim")