# -*- coding: utf-8 -*-
'''
sleepy hypnos


author:kK(fkfkbill@gmail.com)
'''


from django.contrib import admin

from hypnos.models import *

from django.utils.timezone import template_localtime
from datetime import datetime
from django.utils.timezone import utc




#===========================================
class sleepAdmin(admin.ModelAdmin):
	list_display=("user","finished","time_begin","time_end","time_period","diary")
	ordering=("-time_begin",)
	list_filter=("finished",)


#===========================================
class archiveAdmin(admin.ModelAdmin):
	list_display=("user","year","month")
	exclude=()
	ordering=("-year","-month")




#register to the admin
#admin.site.register(sleep,sleepAdmin)
admin.site.register(archive,archiveAdmin)
