
# !sur/bin/env python
# -*-coding:utf-8 -*-
from __future__ import unicode_literals
from EQuery.models import models
from django import forms
# Create your models here.


class Exception(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=200)
    example=models.CharField(max_length=200)
    hit=models.IntegerField()