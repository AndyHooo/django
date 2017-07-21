# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def add(request):
	a = request.GET['a']
	b = request.GET['b']
	c = int(a) + int(b)
	return HttpResponse(str(c))

def add2(request,a,b):
	c = int(a) + int(b)
	return HttpResponse(str(c))

def index(request):
	list = ['java','php','css','js']
	nums = map(str,range(100))
	dataDict = {'course':list,'nums':nums}
	return render(request,'home.html',{'data':dataDict})
