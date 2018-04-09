#  _*_ coding:utf-8 _*_
# create your views here
from  __future__ import unicode_literals
from django.http import HttpResponse
from .import models
from django.shortcuts import render
from django.db.models import F,Q



#定义主函数，即页面显示
def home(request):
    return render(request,'home.html')

#定义文件导入函数，即文件导入页面
def file_import(request):
    return render(request,'file_import.html')


#定义异常查询页面入口函数，即异常查询页面
def exception_query(request):
    name=models.exception.objects.all()
    return render(request,'exception_query.html',{'name':name})

#定义异常查询结果函数
def query_result(request):
        kw=request.GET('kw')
        exception_name=models.exception.objects.filter(name='kw').update(hit=F('hit')+1)
        return render(request,'query_result.html',{'exception_name':exception_name,'kw':kw})


#定义统计展示入口函数，即统计展示页面
def statistics_show(request):
    return render(request,'statistics_show.html')

#统计展示结果函数
def show_result(request):
    pass