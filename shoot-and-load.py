#!/usr/bin/python
#coding: utf-8
import pyperclip
import os, time


WEBSITE_ROOT_URL = "http://technocake.net/screenshots/"


def genUrl(picture):
	return WEBSITE_ROOT_URL + picture

def putOnServer(picture):
	os.system("scp \"%s\" pompel.komsys.org:/var/www/www.technocake.net/screenshots" % picture)

def deletePicture(picture):
	os.remove(picture)

def lookForPicture(folder='~/Desktop'):
	for file in os.listdir('/Users/technocake/Desktop'):
	    if file.split('.')[-1] == 'png':
	    	print "Found file %s, sending it online!!" % (file,)
	    	putOnServer(file)
	    	copyToClipBoard(genUrl(file))
	    	deletePicture(file)

def copyToClipBoard(what):
	pyperclip.setcb(what)




if __name__ == "__main__":
	while 1:
		time.sleep(0.1)
		lookForPicture()

