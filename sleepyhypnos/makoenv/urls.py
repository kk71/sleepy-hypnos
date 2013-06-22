# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

import djangomako



urlpatterns=patterns("",
		url(r"^(.*)",djangomako.tmpldebug),
)
