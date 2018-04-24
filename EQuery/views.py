#  _*_ coding:utf-8 _*_
# create your views here
from __future__ import unicode_literals
from django.http import HttpResponse
from file.forms import UploadFileForm
from EQuery.models import models
from django.db.models import F,Q
from django.shortcuts import render
from EQuery.models import Exception


def index(request):
    return render(request, 'home.html')


#定义异常查询页面入口函数，即异常查询页面
def exception_query(request):
    return render(request, 'exceptionQuery.html')
    # name = models.exception.objects.all()
    # return render(request, 'exceptionQuery.html', {'name': name})


#定义异常查询结果函数
def query_result(request):
        kw = request.GET('kw')
        exception_name = models.exception.objects.filter(name='kw').update(hit=F('hit')+1)
        return render(request, 'queryResult.html', {'exception_name': exception_name, 'kw': kw})


def uploadfile(request):
        if request.POST:
            f = request.FILES.get('file')

            while True:

                line = f.readline()  # 读取表头
                try:
                    line1 = line.decode('utf-8-sig')
                    if not line1 or line1 == '\r\n' or line1 == '\r' or line1 == '\n' or line1 == '': break
                    arg = line1.split(',')
                    hit = arg[3].rstrip('\r\n')
                    exception = Exception(name=arg[0], example=arg[1], description=arg[2], hit=hit)
                    exception.save()
                except:
                    pass
                    line2 = line.decode('gb2312')
                    if not line2 or line2 == '\r\n' or line2 == '\r' or line2 == '\n' or line2 == '': break
                    arg = line2.split(',')
                    hit = arg[3].rstrip('\r\n')
                    exception = Exception(name=arg[0], example=arg[1], description=arg[2], hit=hit)
                    exception.save()
            f.close()
            return HttpResponse('upload success!')

        else:
            form = UploadFileForm()

            return render(request, 'EQuery/upload.html', context=({'form': form}))


def show(request):
    exceptions = Exception.objects.order_by("hit")
    exceptions.objects.all()[:5]
    listx = []
    listy = []
    for exception in exceptions:  #遍历，拼横纵坐标
        listx.append(str(exception.hit))
        listy.append(int(exception.name))
    return render(request, "show.html", {'exceptions':exceptions, 'X':listx, 'Y':listy})
