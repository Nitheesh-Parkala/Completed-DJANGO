
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def view1(request):
    s= "<h1>Welcome to django session"
    return HttpResponse(s)

def view2(request):
    s= "Hi"
    return HttpResponse(s)