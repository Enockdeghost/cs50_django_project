from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the first index.")

def enock(request):
    return HttpResponse("enock")

def name(request,names):
    return HttpResponse(f"hello {names}")