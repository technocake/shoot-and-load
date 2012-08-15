#!/usr/bin/python
#coding: utf-8
import pyperclip
import os, time
import urllib


WEBSITE_ROOT_URL = "http://marte.fjeldsboe.com/screenshots/" #keep trailing slash
LOCALE_FOLDER = "/Users/martebergefjeldsboe/Desktop/screenshots/" # keep the trailing slash
REMOTE_FOLDER = "~/www/screenshots/"
SERVER = "marte@marte.komsys.org"

def genUrl(picture):
	return WEBSITE_ROOT_URL + urllib.quote(picture) #urlencoding the file part

def putOnServer(picture):
	os.system("scp \"%s\" %s:%s" % (picture, SERVER, REMOTE_FOLDER))

def deletePicture(picture):
	os.remove(picture)

def lookForPicture(folder=LOCALE_FOLDER):
	for file in os.listdir(folder):
	    if file.split('.')[-1] in [ 'png', 'jpg'] :
	    	absfile = LOCALE_FOLDER + file
	    	print "Found file %s, sending it online!!" % (file,)
	    	copyToClipBoard(genUrl(file))
	    	putOnServer(absfile)
	    	deletePicture(absfile)

def copyToClipBoard(what):
	pyperclip.setcb(what)




if __name__ == "__main__":
	while 1:
		time.sleep(0.1)
		lookForPicture()

