#!/usr/bin/python3

import os
import random 
import time
import getpass
import argparse


def getDir(override):
    user = getpass.getuser()
    if override == -1:
        currHour = time.localtime()[3]
    else:
        currHour = override

    if currHour < 10:
            path = '/home/' + user + '/Pictures/Wallpapers/Morning/'
    elif currHour >= 20:
            path = '/home/' + user + '/Pictures/Wallpapers/Night/'
    else:
            path = '/home/' + user + '/Pictures/Wallpapers/Day/'
    return path

def main(args):
    path = getDir(args.time)

    picFolder = os.listdir(path)	
    path += random.choice(picFolder)

    os.system("gsettings set org.gnome.desktop.background picture-uri file:" + path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
            '-t', '--time',
            help='what time you want to override with',
            type=int,
            default = -1)
    #TODO not implemented
    parser.add_argument(
            '-r', '--random',
            help="Can randomly pick from ALL availible background photos",
            type=bool,
            default=False)

    args = parser.parse_args()
    main(args)
