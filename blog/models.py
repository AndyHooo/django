# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

# Create your models here.字段中不能有双下划线，因为在Django QuerySet API中有特殊含义。
class BlogsPost(models.Model):
    title = models.CharField(max_length = 150)
    body = models.TextField()
    timestamp = models.DateTimeField()

class People(models.Model):
	name = models.CharField(max_length = 50)
	age = models.IntegerField()
	email = models.CharField(max_length = 120)
	def __unicode__(self):
    # 在Python3中使用 def __str__(self):
		return 'name=' + self.name + ',age=' + str(self.age) + ',email=' + self.email

admin.site.register(BlogsPost)
admin.site.register(People)

#django querySet API：
#一.新建一个对象的方法:
#1.People.objects.create(name='andy',age=10,email='396877565@qq.com')
#2.p = People(name='andy',age=10,email='396877565@qq.com')
#  p.save()
#3.p = People(name='andy')
#  p.age = 10
#  p.email = '396877565@qq.com'
#  p.save()
#4.People.objects.get_or_create(name="andy", age=10)
#这种方法是防止重复很好的方法，但是速度要相对慢些，返回一个元组，
#第一个为Person对象，第二个为True或False, 新建时返回的是True, 已经存在时返回False.
#
#二.获取对象有以下方法：
#1.Person.objects.all()
#2.Person.objects.all()[:10] 切片操作，获取10个人，不支持负索引，切片可以节约内存
#3.Person.objects.get(name=name)
#get是用来获取一个对象的，如果需要获取满足条件的一些人，就要用到filter
#4.Person.objects.filter(name="abc")  # 等于Person.objects.filter(name__exact="abc") 名称严格等于 "abc" 的人
#5.Person.objects.filter(name__iexact="abc")  # 名称为 abc 但是不区分大小写，可以找到 ABC, Abc, aBC，这些都符合条件
#6.Person.objects.filter(name__contains="abc")  # 名称中包含 "abc"的人
#7.Person.objects.filter(name__icontains="abc")  #名称中包含 "abc"，且abc不区分大小写
#8.Person.objects.filter(name__regex="^abc")  # 正则表达式查询
#9.Person.objects.filter(name__iregex="^abc")  # 正则表达式不区分大小写
#10.filter是找出满足条件的，当然也有排除符合某条件的
#11.Person.objects.exclude(name__contains="WZ")  # 排除包含 WZ 的Person对象
#12.Person.objects.filter(name__contains="abc").exclude(age=23)  # 找出名称含有abc, 但是排除年龄是23岁的
#
#