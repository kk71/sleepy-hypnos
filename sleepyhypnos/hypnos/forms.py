# -*- coding: utf-8 -*-
'''
sleepy hypnos


author:kk(fkfkbill@gmail.com)
'''

from django.conf import settings
from django import forms
from django.forms import CharField,EmailField,BooleanField,ChoiceField,FileField,ImageField,IntegerField,IPAddressField,URLField
from django.forms import ValidationError



#======================================
class login(forms.Form):
	account=				CharField(max_length=19)
	password=				CharField(max_length=12)

	

#======================================
class reg(forms.Form):
	account=				CharField(max_length=19)
	password=				CharField(max_length=12)
	repassword=				CharField(max_length=12)
	captcha=				CharField(max_length=settings.CAPTCHA_CHAR_NUM)

	def clean_password(self):
		if self.password!=self.repassword:
			raise ValidationError("两次密码不一致。")
		return self.password
