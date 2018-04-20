# -*-coding:utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'home.html')


def toupload(request):
    return render(request, 'upload.html')


def toexception_query(request):
    return render(request, 'exception_query.html')


def toshow(request):
    return render(request, 'show.html')