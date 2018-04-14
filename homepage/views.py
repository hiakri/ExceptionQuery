from django.shortcuts import render
from __future__ import unicode_literals
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("homepage")

def home(request):
    return render(request,'home.html')