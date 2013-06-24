# -*- coding: utf-8 -*-
'''
sleepy hypnos


author:kk(fkfkbill@gmail.com)
'''

from django.conf import settings
import random,redis
from datetime import datetime
from PIL import Image,ImageDraw,ImageFont


try:
	redis_db = redis.StrictRedis(host=settings.CAPTCHA_REDIS["host"], port=settings.CAPTCHA_REDIS["port"], db=settings.CAPTCHA_REDIS["db"])
except:
	print("Error: redis db isn't well prepared.")
	exit()


try:
	table_file=open(settings.CHN_CHAR_TABLE_FILE,"r")
	chn_gb2312_table=table_file.read()[:-1]
	table_file.close()
except:
	print("Error: GB2312 char table doesn't exist.")
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
		self.randLine(settings.CAPTCHA_LINE)


	def save(self, path):
		self.image.save(path)



#=========================================================
def captcha_gen(sessionid):
	n=datetime.now()
	rand_img_file='/%s%s%s%s%s%s-%s.png'%(n.year,n.month,n.day,n.hour,n.minute,n.second,\
											random.randint(111111,999999))

	ic = ImageChar(fontColor=(100,211, 90))
	ic.randChinese(settings.CAPTCHA_CHAR_NUM)
	ic.save(settings.CAPTCHA_DIR+rand_img_file)
	redis_db.set(sessionid,ic.chars)

	img_file=open(settings.CAPTCHA_DIR+rand_img_file,"rb")
	img=img_file.read()
	img_file.close()
	return img



#=========================================================
def captcha_verify(sessionid,value):
	if value!="" and redis_db.get(sessionid).decode("utf-8")==value:
		redis_db.delete(sessionid)
		return True
	elif redis_db.get(sessionid)!=None:
		redis_db.delete(sessionid)
	return False
