# -*- coding: utf-8 -*-
'''



author: kk(fkfkbill@gmail.com)
'''

from django.db import models
from django.db.models.fields import TextField,DateTimeField,TimeField,BooleanField,SmallIntegerField
from django.db.models import ForeignKey,ManyToManyField

from django.contrib.auth.models import User



class sleep(models.Model):
	user=ForeignKey(User)
	finished=BooleanField(default=False,verbose_name="已结束")
	time_begin=DateTimeField(verbose_name="起始时间")
	time_end=DateTimeField(blank=True,null=True,verbose_name="终止时间")
	time_period=TimeField(blank=True,null=True,verbose_name="时间周期")
	to_archive=ForeignKey("archive",verbose_name="归档于")
	diary=TextField(blank=True,null=True,verbose_name="日记")

	class Meta():
		verbose_name="睡眠记录"
		verbose_name_plural=verbose_name
	
	def __unicode__(self):
		return "user:%s, finished:%s, time_period:%s "%(user,finished,time_period)


class archive(models.Model):
	user=ForeignKey(User)
	year=SmallIntegerField(verbose_name="年",unique=True)
	month=SmallIntegerField(verbose_name="月",unique=True)
	sleeps=ManyToManyField("sleep",verbose_name="睡眠记录")

	class Meta():
		verbose_name="归档"
		verbose_name_plural=verbose_name

	def __unicode__(self):
		return "user:%s, year:%s, month:%s "%(user,year,month)
