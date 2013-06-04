# -*- coding: utf-8 -*-
'''
sleepy hypnos


author: kk(fkfkbill@gmail.com)
'''


from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


from hypnos import views

urlpatterns = patterns('',
	url(r'^grappelli/', include('grappelli.urls')),
	url(r'^admin/', include(admin.site.urls)),
	
	#account management
	url(r"^reg/?$",views.reg),
	url(r"^loginout/?$",views.loginout),
	url(r"^config/?$",views.config),
	url(r"^change-password/?$",views.change_password),
	
	#diaries
	url(r"^switch-status/?$",views.switch_status),
	url(r"^list/?(.*)/?(.*)/?$",views.list),
	url(r"^sleep/(.+)/(.+)/(.+)/?$",views.sleep),
	url(r"^analysis/?(.*)/?(.*)/?$",views.analysis),
	url(r"^$",views.index),
)
