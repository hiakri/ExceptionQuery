# -*-coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from EShow.models import Exception
# Create your views here.
def index(request):
    return render(request, 'home.html')

def show(request):
    exceptions=Exception.objects.all()  #获取hit值前五的行,此处待修改
    listx = []
    listy = []
    for exception in exceptions:  #遍历，拼横纵坐标
        listx.append(str(exception.hit))
        listy.append(int(exception.name))
    return render(request, "show.html", {'exceptions':exceptions, 'X':listx, 'Y':listy})  #跳转到show.html，并将拼好的数据（{'users':users, 'X':listx, 'Y':listy}）传递到该页面