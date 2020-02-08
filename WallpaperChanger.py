import os
import random 
import time

currHour = time.time()[3]
if currHour < 10:
	picFolder = os.listdir('/home/lyrk/Pictures/Wallpapers/')
elif currHour > 8:
	picFolder = os.listdir('/home/lyrk/Pictures/Wallpapers/')
else:
	picFolder = os.listdir('/home/lyrk/Pictures/Wallpapers/')
	
path = "/home/lyrk/Pictures/Wallpapers/" + random.choice(picFolder)

os.system("gsettings set org.gnome.desktop.background picture-uri file:" + path)
