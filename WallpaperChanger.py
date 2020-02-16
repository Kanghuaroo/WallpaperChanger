#!/usr/bin/python

import os
import random 
import time
import getpass

user = getpass.getuser()
currHour = time.localtime()[3]

if currHour <= 10:
	path = '/home/' + user + '/Pictures/Wallpapers/Morning/'
elif currHour >= 20:
	path = '/home/' + user + '/Pictures/Wallpapers/Night/'
else:
	path = '/home/' + user + '/Pictures/Wallpapers/Day/'

picFolder = os.listdir(path)	
path += random.choice(picFolder)

os.system("gsettings set org.gnome.desktop.background picture-uri file:" + path)
