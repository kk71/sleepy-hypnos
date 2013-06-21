# -*- coding: utf-8 -*-
__version__="0.2"
'''
django-mako template connection module
version 0.2, for django1.5+

author: kk(fkfkbill@gmail.com)
'''
#python import
from glob import glob

#django import
from django.http import HttpResponse
from django.core.context_processors import csrf
from django.conf import settings

#mako import
from mako.lookup import TemplateLookup

#default template lookup
djlookup=TemplateLookup(directories=settings.TEMPLATE_DIRS,input_encoding="utf-8")



#==============================================================
def render_to_string(template_name,
		dictionary=None,
		request=None,
        tmpldir=None):
    '''
render a template to a string(like render_to_string django.template.loader)
'''
    #if another template dir is specified,then use it.
    if tmpldir==None or tmpldir=="":
        t=djlookup.get_template(template_name)
    else:
        t=TemplateLookup(directories=tmpldir,input_encoding="utf-8").get_template(template_name)
    if request!=None:
        dictionary.update(csrf(request))
    page=t.render(**dictionary)
    return page
	


#==============================================================
def render_to_response(template_name,
		dictionary={},
		content_type="text/html",
		request=None,
		status=200,
        tmpldir=None):
	'''
a simple http response method just like django's
for easy alternativity
'''
	page=render_to_string(template_name,dictionary,request,tmpldir=tmpldir)
	return HttpResponse(content=page,content_type=content_type,status=status)



#==============================================================
def tmpldebug(request,tmpl=""):
	'''
argument:
	tmpl:specific template file name.
'''
	if tmpl=="":
		t='''
<!DOCTYPE html>
<html>
<head>
<title>djangomako template design mode</title>
</head>
<body>
'''
		for tmpldir in settings.TEMPLATE_DIRS:
			if tmpldir[-1]!="/":tmpldir+="/"
			t+="<h2>"+tmpldir+"</h2>"
			for s in glob(tmpldir+"*"):
				if s[-1:]=="~":continue
				s=s[len(tmpldir):]
				t+='<p><a href=\"'+s+'\">'+s+"</a></p>"
			t+="<br>"
		t+='''
</body> 
</html>
'''
		return HttpResponse(t)

	else:
		return render_to_response(tmpl,{})
