# -*-coding:utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from file.forms import UploadFileForm
from EImport.models import Exception

# Create your views here.


def index(request):
    return render(request, 'home.html')


def uploadfile(request):
        if request.POST:

            form = UploadFileForm(request.POST, request.FILES)

            f = request.FILES['file']
            line = f.readline()  # 读取表头
            while True:
                line = f.readline()
                try:
                    line1 = line.decode('utf-8-sig')
                    if not line1 or line1 == '\r\n' or line1 == '\r' or line1 == '\n' or line1 == '': break
                    arg = line1.split(',')
                    hit = arg[3].rstrip('\r\n')
                    exception = Exception(arg[0], arg[1], arg[2], hit)
                    exception.save()
                except:
                    pass
                    line2 = line.decode('gb2312')
                    if not line2 or line2 == '\r\n' or line2 == '\r' or line2 == '\n' or line2 == '': break
                    arg = line2.split(',')
                    hit = arg[3].rstrip('\r\n')
                    exception = Exception(arg[0], arg[1], arg[2], hit)
                    exception.save()
            f.close()
            return HttpResponse('upload ok!')

        else:

            form = UploadFileForm()

        return render(request, 'EImport/upload.html', context=({'form': form}))