import os
import random 
import time

currHour = time.localtime()[3]
if currHour < 10:
	path = '/home/lyrk/Pictures/Wallpapers/Morning/'
elif currHour > 8:
	path = '/home/lyrk/Pictures/Wallpapers/Night/'
else:
	path = '/home/lyrk/Pictures/Wallpapers/'

picFolder = os.listdir(path)	
path +=  random.choice(picFolder)

os.system("gsettings set org.gnome.desktop.background picture-uri file:" + path)
