# -*- coding: utf-8 -*-
'''
sleepy hypnos


author:kk(fkfkbill@gmail.com)
'''


from django.http import HttpResponse,HttpResponseRedirect
from djangomako import render_to_response
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import pdb



#======================================
def index(request):
	'''
'''
	if not request.user.is_authenticated:
		dic={}
		return render_to_response("login.html",dic)

	else:
		dic={}
		return render_to_response("index.html",dic)



#======================================
def reg(request):
	'''
'''
	if request.user.is_authenticated():
		return HttpResponseRedirect("/log")

	else:
		dic={}
		return render_to_response("reg.html",dic)



#======================================
def loginout(request):
	'''
'''
	if request.user.is_authenticated():
		logout(request)
		return HttpResponseRedirect("/")

	else:
		dic={}
		return render_to_response("login.html",dic)



#======================================
@login_required
def change_password(request):
	'''
'''
	return HttpResponse("change-password.html")



#======================================
@login_required
def config(request):
	'''
'''
	return HttpResponse("config.html")



#======================================
@login_required
def switch_status(request):
	'''
'''
	return HttpResponse("post.html")



#======================================
@login_required
def list(request,offsets):
	'''
'''
	return HttpResponse("list.html")



#======================================
@login_required
def sleep(request,offsets):
	'''
'''
	return HttpResponse("sleep.html")



#======================================
@login_required
def analysis(request,offsets):
	'''
'''
	return HttpResponse("analysis.html")

