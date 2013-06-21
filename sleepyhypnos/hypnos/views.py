# -*- coding: utf-8 -*-
'''
sleepy hypnos


author:kk(fkfkbill@gmail.com)
'''


from django.http import HttpResponse,HttpResponseRedirect
from djangomako import render_to_response
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import auth
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
		if request.method=="GET":
			dic={
				"not_matched_prompt":False,
			}
		else:
			user_id=request.POST["account"]
			user_key=request.POST["password"]
			user_tolog=auth.authenticate(username=user_id,password=user_key)
			if user_tolog!=None:
				if user_tolog.is_active==True:
					auth.login(request,user_tolog)
					return HttpResponseRedirect("/")
				else:
					return render_to_response("") #需要一个“用户被禁用”的模板？
			else:
				dic={
					"not_matched_prompt":True
				}
		return render_to_response("login.html",dic,request=request)




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

