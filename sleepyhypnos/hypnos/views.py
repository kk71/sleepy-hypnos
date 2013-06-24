# -*- coding: utf-8 -*-
'''
sleepy hypnos


author:kk(fkfkbill@gmail.com)
'''


from django.http import HttpResponse,HttpResponseRedirect
from djangomako import render_to_response
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
import pdb

from hypnos import forms

from hypnos.captcha import captcha_gen





#======================================
@login_required
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
def captcha(request):
	'''
获取验证码
'''
	return HttpResponse(captcha_gen(request.COOKIES["sessionid"]),content_type="image/png")



#======================================
def reg(request):
	'''
'''
	if request.user.is_authenticated():
		return HttpResponseRedirect("/")

	else:
		dic={
				"username_taken_prompt":False,
				"password_not_matched_prompt":False,
				"captcha_not_matched_prompt":False
		}
		if request.method=="POST":
			reg_form=forms.register(request)
			if reg_form==0:
				return HttpResponseRedirect("/")
			elif reg_form==1:
				dic.update({"username_taken_prompt":True})
			elif reg_form==2:
				dic.update({"password_not_matched_prompt":True})
			elif reg_form==3:
				dic.update({"captcha_not_matched_prompt":True})
		return render_to_response("register.html",dic,request=request)




#======================================
def loginout(request):
	'''
'''
	if request.user.is_authenticated():
		logout(request)
		return HttpResponseRedirect("/")

	else:
		dic={
			"not_matched_prompt":False,
			"user_locked_prompt":False,
		}
		if request.method=="POST":
			login_form=forms.login(request)
			if login_form==0:
				return HttpResponseRedirect("/")
			elif login_form==1:
				dic.update({
					"not_matched_prompt":True
				})
			elif login_form==2:
				dic.update({
					"user_locked_prompt":True
				})
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

