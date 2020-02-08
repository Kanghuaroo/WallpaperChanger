import os
import random 


pics = os.listdir('/home/lyrk/Pictures/Wallpapers/')
path = "/home/lyrk/Pictures/Wallpapers/" + random.choice(pics)

os.system("gsettings set org.gnome.desktop.background picture-uri file:" + path)
