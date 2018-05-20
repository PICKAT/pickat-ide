from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter.scrolledtext import ScrolledText
import PIL.Image
import PIL.ImageTk
import os
import json
from functions import *

settings_path = "assets/settings.ini"


Jobjects = []
frameWall = None
rootObj = None
def getSettings(sec,var):
	import configparser
	config = configparser.ConfigParser()
	config.read(settings_path)
	data = config.get(sec,var)
	return data

from past.builtins import execfile

execfile('functions.py')

def draw(root):
	global frameWall,rootObj
	rootObj = root
	#set title
	rootObj.title(getSettings('form','name'))
	#set icon
	rootObj.iconbitmap(getSettings('form','icon'));
	#set form size
	widthvar = getSettings('form','width')
	heightvar = getSettings('form','height')
	rootObj.geometry('{}x{}'.format(widthvar, heightvar))
	#set resizable
	rootObj.resizable(int(getSettings('form','resizewidth')), int(getSettings('form','resizeheight')))
	
	frameWall=ttk.Frame(rootObj, width=widthvar, height=heightvar)
	frameWall.grid()
	#print images
	images(frameWall,getSettings('elements','images'))
	
	#print buttons
	buttons(frameWall,getSettings('elements','buttons'))
	
	#print labels
	labels(frameWall,getSettings('elements','lables'))
	
	#print textbox
	textbox(frameWall,getSettings('elements','textbox'))
	

def ButtonsClick(this):
	for i in range(0,len(Jobjects)):
		if this in Jobjects[i]:
			eval('{}("{}")'.format(Jobjects[i][this]['command'],this))
	

def setConfig(id,conf):
	global frameWall
	for i in range(0,len(Jobjects)):
		if id in Jobjects[i]:
			Jobjects[i][id]['obj'].config(conf)
			return True
		
	print("not found %s" % id)
	return False
	
def setTextBoxText(id,text):
	global frameWall
	for i in range(0,len(Jobjects)):
		if id in Jobjects[i]:
			Jobjects[i][id]['obj'].delete("1.0", "end")
			Jobjects[i][id]['obj'].insert(INSERT, text)
			return True
		
	print("not found %s" % id)
	return False
def appendTextBoxText(id,text):
	global frameWall
	for i in range(0,len(Jobjects)):
		if id in Jobjects[i]:
			Jobjects[i][id]['obj'].insert(INSERT, text)
			return True
		
	print("not found %s" % id)
	return False
def deleteTextBoxText(id):
	global frameWall
	for i in range(0,len(Jobjects)):
		if id in Jobjects[i]:
			Jobjects[i][id]['obj'].delete("1.0", "end")
			return True
		
	print("not found %s" % id)
	return False
def labels(frame,jdata):
	data = json.load(open(jdata))
	
	for index in range(0,len(data)):
		
		label = None
		jobj = {
			'{}'.format(data[index]['id']): {
				"obj":label
			}
		}
		Jobjects.append(jobj)
		
		Jobjects[-1][data[index]['id']]['obj'] = Label(frame, text="not defined")
		Jobjects[-1][data[index]['id']]['obj'].config(data[index]['prop'])
		Jobjects[-1][data[index]['id']]['obj'].place(data[index]['posi'])
		
	
def buttons(frame,jdata):
	data = json.load(open(jdata))
	
	for index in range(0,len(data)):
		btn = None
		comn = ""
		if "command" in data[index]:
			comn=data[index]["command"]
		jobj = {
			'{}'.format(data[index]['id']): {
				"obj":btn,
				"command":comn
			}
		}
		
		Jobjects.append(jobj)
		
		Jobjects[-1][data[index]['id']]['obj'] = Button(frame, text="not defined")
		
		if "command" in data[index]:
			Jobjects[-1][data[index]['id']]['obj'].config(command=lambda sendingdata=data[index]['id']: ButtonsClick(sendingdata))
		
		Jobjects[-1][data[index]['id']]['obj'].config(data[index]['prop'])
		Jobjects[-1][data[index]['id']]['obj'].place(data[index]['posi'])
	

def images(frame,jdata):
	data = json.load(open(jdata))
	
	for index in range(0,len(data)):
		panel = None
		jobj = {
			'{}'.format(data[index]['id']): {
				"obj":panel
			}
		}
		Jobjects.append(jobj)
		path = data[index]['imgp']['src']
		
		im = PIL.Image.open(path)
		if "width" in data[index]['imgp'] and "height" in data[index]['imgp']:
			im = im.resize((data[index]['imgp']['width'], data[index]['imgp']['height']), PIL.Image.ANTIALIAS)
		photo = PIL.ImageTk.PhotoImage(im)
		
		Jobjects[-1][data[index]['id']]['obj'] = Label(frame, image = photo)
		Jobjects[-1][data[index]['id']]['obj'].image = photo
		Jobjects[-1][data[index]['id']]['obj'].config(data[index]['prop'])
		Jobjects[-1][data[index]['id']]['obj'].place(data[index]['posi'])
	
def textbox(frame,jdata):
	data = json.load(open(jdata))
	
	for index in range(0,len(data)):
		tbx = None
		jobj = {
			'{}'.format(data[index]['id']): {
				"obj":tbx
			}
		}
		Jobjects.append(jobj)
		if "multiline" in data[index]:
			if data[index]['multiline'] == True:
				Jobjects[-1][data[index]['id']]['obj'] = ScrolledText(frame)
		else:
			Jobjects[-1][data[index]['id']]['obj'] = Entry(frame)
		Jobjects[-1][data[index]['id']]['obj'].insert(INSERT, "not Defined")
		if "text" in data[index]:
			Jobjects[-1][data[index]['id']]['obj'].delete("1.0", "end")
			Jobjects[-1][data[index]['id']]['obj'].insert(INSERT, data[index]['text'])
		
		Jobjects[-1][data[index]['id']]['obj'].config(data[index]['prop'])
		Jobjects[-1][data[index]['id']]['obj'].place(data[index]['posi'])