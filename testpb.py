#!/usr/bin/python
import pyperclip
pyperclip.setcb('The text to be copied to the clipboard.')
spam = pyperclip.getcb()
