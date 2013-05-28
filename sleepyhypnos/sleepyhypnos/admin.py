# -*- coding: utf-8 -*-
'''


author:kK(fkfkbill@gmail.com)
'''


from django.contrib import admin

from sleepyhypnos.models import *

from django.utils.timezone import template_localtime
from datetime import datetime
from django.utils.timezone import utc




#===========================================
class sleepAdmin(admin.ModelAdmin):
	#list_display=()
	exclude=()
	ordering=()
	list_filter=("finished",)


#===========================================
class archiveAdmin(admin.ModelAdmin):
	#list_display=()
	exclude=()
	ordering=()




#register to the admin
admin.site.register(sleep,sleepAdmin)
admin.site.register(archive,archiveAdmin)
