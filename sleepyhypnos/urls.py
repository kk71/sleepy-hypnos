# -*- coding: utf-8 -*-
'''
sleepy hypnos


author: kk(fkfkbill@gmail.com)
'''


from django.conf.urls import patterns, include, url
from django.conf import settings
from hypnos import views
from djangomako import tmpldebug

from django.contrib import admin
admin.autodiscover()




urlpatterns = patterns('',
	url(r'^grappelli/', include('grappelli.urls')),
	url(r'^admin/', include(admin.site.urls)),
	
	#account management
	url(r"^reg/?$",views.reg),
	url(r"^log/?$",views.loginout),
	url(r"^captcha/?$",views.captcha),
	url(r"^config/?$",views.config),
	url(r"^change-password/?$",views.change_password),
	
	#diaries
	url(r"^switch-status/?$",views.switch_status),
	url(r"^list/?(.*)/?(.*)/?$",views.list),
	url(r"^sleep/(.+)/(.+)/(.+)/?$",views.sleep),
	url(r"^analysis/?(.*)/?(.*)/?$",views.analysis),
	url(r"^$",views.index),
)

if settings.DEBUG==True:
	urlpatterns+=patterns("",
			url(r"^tmpldebug/(.*)/?$",tmpldebug)
	)
