# -*- coding: utf-8 -*-
'''
sleepy hypnos


author:kk(fkfkbill@gmail.com)
'''

from django.conf import settings
import redis
import random
from PIL import Image,ImageDraw,ImageFont

try:
	redis_db = redis.StrictRedis(host=settings.CAPTCHA_REDIS["host"], port=settings.CAPTCHA_REDIS["port"], db=settings.CAPTCHA_REDIS["db"])
except:
	print("Error: redis db isn't well prepared.")
	exit()

try:
	table_file=open(settings.CHN_CHAR_TABLE_FILE,"r")
	chn_gb2312_table=table_file.read()
	table_file.close()
except:
	print("Error: GB2312 char table")
	exit()




#=========================================================
def RandomChar():
	global chn_gb2312_table
	return random.sample(chn_gb2312_table,1)[0]



#=========================================================
class ImageChar():
	def __init__(self,
				fontColor = (0,0,0),
				size = (100, 40),
				fontPath = settings.CAPTCHA_TTC,
				bgColor = (255, 255, 255),
				fontSize = 20):
		self.size = size
		self.fontPath = fontPath
		self.bgColor = bgColor
		self.fontSize = fontSize
		self.fontColor = fontColor
		self.font = ImageFont.truetype(self.fontPath, self.fontSize)
		self.image = Image.new('RGB', size, bgColor)  


	def rotate(self):
		self.image.rotate(random.randint(0, 30), expand=0)  


	def drawText(self, pos, txt, fill):
		draw = ImageDraw.Draw(self.image)
		draw.text(pos, txt, font=self.font, fill=fill)
		del draw  


	def randRGB(self):
		return (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))  


	def randPoint(self):
		(width, height) = self.size
		return (random.randint(0, width), random.randint(0, height))  


	def randLine(self, num):
		draw = ImageDraw.Draw(self.image)
		for i in range(0, num):
			draw.line([self.randPoint(), self.randPoint()], self.randRGB())
		del draw  


	def randChinese(self, num):
		gap = 5
		start = 0
		self.chars=""
		for i in range(0, num):
			char = RandomChar()
			self.chars+=char
			x = start + self.fontSize * i + random.randint(0, gap) + gap * i
			self.drawText((x, random.randint(-5, 5)), char, self.randRGB())
			self.rotate()
		self.randLine(3)


	def save(self, path):
		self.image.save(path)



#=========================================================
class captcha_manage():
	def __init__(self,request):
		self.request=request
		return


	def gen(self):
		'''
	生成验证码图片，并将值存放在redis数据库中	
	return:
		图片url
	'''
		ic = ImageChar(fontColor=(100,211, 90))
		ic.randChinese(3)
		ic.save(settings.CAPTCHA_DIR+'/test.png')
		redis_db.set(self.request.COOKIES["sessionid"],ic.chars)
		return settings.CAPTCHA_URL_PREFIX+"/test.png"


	def verify(self):
		'''
	验证request的session值和redis中储存的是否一致，
	若不一致则删除原验证码图片和redis数据，重新建立新的验证码和图片
	注意：form中验证码的索引名为“captcha”
	return:
		验证成功：True
		验证失败：新的验证码图片url
	'''
		try:
			sessionid=self.request.COOKIES["sessionid"]
			captcha_val=self.request.POST["captcha"]
			val_in_db=redis_db.get(sessionid)
			if val_in_db is None:
				return self.gen()
			if val_in_db==captcha_val:
				return True
			else:
				return self.gen()
		except:
			return self.gen()
