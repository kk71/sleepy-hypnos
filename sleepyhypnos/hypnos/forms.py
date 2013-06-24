# -*- coding: utf-8 -*-
'''
sleepy hypnos forms


author:kk(fkfkbill@gmail.com)
'''

from django.conf import settings
from django.contrib import auth
from django.contrib.auth.models import User
from hypnos.captcha import captcha_verify



#======================================
def login(request):
	'''
return:
	0无错误
	1用户不匹配、不存在
	2用户被禁用
	None其他
	'''
	#verify
	form_data=request.POST
	try:
		if form_data["account"].strip()=="":
			return 1
		if form_data["password"].strip()=="":
			return 1
	except:
		return 1

	#login
	user_tolog=auth.authenticate(username=form_data["account"],password=form_data["password"])
	if user_tolog==None:
		return 1
	if not user_tolog.is_active:
		return 2
	auth.login(request,user_tolog)
	return 0

	

#======================================
def register(request):
	'''
	return:
		0注册成功(且已登录)
		1用户名被占用
		2密码不符合
		3验证码错误
		None
'''
	#verify
	form_data=request.POST
	try:
		account=form_data["account"].strip()
		password=form_data["password"].strip()
		repassword=form_data["repassword"].strip()
		captcha=form_data["captcha"].strip()

		if account=="" or len(account)>=19:
			return 1
		if password=="" or \
				password!=repassword or \
				len(password)>12:
			return 2
		if not captcha_verify(request.COOKIES["sessionid"],captcha):
			return 3
	except:
		return None
	try:
		#create user
		new_usr=User.objects.create_user(account,password=password)
		new_usr.save()
		#login
		user_tolog=auth.authenticate(username=account,password=password)
		auth.login(request,user_tolog)
	except:
		return 1
	return 0
