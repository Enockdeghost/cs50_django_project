from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"first/hello.html")

def enock(request):
    return HttpResponse("enock")

def name(request,names):
    return render(request, "first/name.html",{
        "name":names.upper()
    })