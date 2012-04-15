#!/usr/bin/python
#coding: utf-8
import pyperclip
import os, time
import urllib


WEBSITE_ROOT_URL = "http://technocake.net/screenshots/" #keep trailing slash
LOCALE_FOLDER = "/Users/technocake/Desktop/" # keep the trailing slash
REMOTE_FOLDER = "/var/www/www.technocake.net/screenshots"
SERVER = "pompel.komsys.org"

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
	    	putOnServer(absfile)
	    	copyToClipBoard(genUrl(file))
	    	deletePicture(absfile)

def copyToClipBoard(what):
	pyperclip.setcb(what)




if __name__ == "__main__":
	while 1:
		time.sleep(0.1)
		lookForPicture()

