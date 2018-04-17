#  _*_ coding:utf-8 _*_
# create your views here
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django.http import *
from EQuery.models import models
from django.db.models import F,Q

from django.shortcuts import render
def index(request):
    return render(request, 'home.html')
#定义异常查询页面入口函数，即异常查询页面
def exception_query(request):
    name=models.exception.objects.all()
    return render(request,'exception_query.html',{'name':name})
#定义异常查询结果函数
def query_result(request):
        kw=request.GET('kw')
        exception_name=models.exception.objects.filter(name='kw').update(hit=F('hit')+1)
        return render(request,'query_result.html',{'exception_name':exception_name,'kw':kw})

