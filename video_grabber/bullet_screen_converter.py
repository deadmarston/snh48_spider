#I don't why it's called bullet screen,
#or maybe you could call it real-time comment(which is not realtime)
#anyway, what this py file does is
#to convert bullet screen into ass file

#origin file is lrt file (maybe supports xml file later)
#output file is ass file

#an example of ass file:
'''
[Script Info]
Title: ass converter
Original Script:
ScriptType: v4.00+
Collisions: Normal
PlayResX: 560
PlayResY: 420
Timer: 10.0000

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Fix,Microsoft YaHei UI,25,&H66FFFFFF,&H66FFFFFF,&H66000000,&H66000000,1,0,0,0,100,100,0,0,1,2,0,2,20,20,2,0
Style: R2L,Microsoft YaHei UI,25,&H66FFFFFF,&H66FFFFFF,&H66000000,&H66000000,1,0,0,0,100,100,0,0,1,2,0,2,20,20,2,0

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 0,0:00:05.70,0:00:13.70,R2L,,20,20,2,,{\move(660,25,-100,25)}this is a demo
'''

#the most important thing is to insert {\move(600, 25, -100, 25)} into dialogue
#so that it could work as bullet screen

from enum import Enum
import exceptions
import time
import os

from video_grabber import *

INPUT_BULLETSCREEN_FILE = Enum('INPUT_BULLETSCREEN_FILE', ('lrt', 'xml'))

BULLET_SCREEN_FOLDER = 'bulletscreen'
if DEBUG_MODE:
    DEFAULT_OUTPUT_PATH = os.path.join(os.path.abspath('..'), BULLET_SCREEN_FOLDER)
else:
    DEFAULT_OUTPUT_PATH = os.path.join(os.path.abspath('.'), BULLET_SCREEN_FOLDER)

#the postprogressed ass file should be saved into the preset path
#and return the path to the caller

def convert_file(input_file, input_type=INPUT_BULLETSCREEN_FILE.lrt, path=DEFAULT_OUTPUT_PATH):
    checkOrCreateFolder(path)
    now = time.strftime("%Y%m%d", time.localtime(time.time()))
    subpath = os.path.join(path, now)
    checkOrCreateFolder(subpath)
    if input_type == INPUT_BULLETSCREEN_FILE.lrt:
        convert_lrt(input_file, subpath)
    elif input_type == INPUT_BULLETSCREEN_FILE.xml:
        pass
    else:
        raise Exception('no such input bulletscreen type, must be lrt or xml, please check the origin file')

def convert_lrt(input_file, outputPath):
    pass

def convert_xml(input_file):
    pass

def read_lrt_files(input_file):
    pass

def getFileName(file):
    return file.split('.')[0]

def checkOrCreateFolder(path):
    if os.path.exists(path):
        if os.path.isdir(path):
            return
    print(path)
    os.mkdir(path)

if __name__ == "__main__":
    #test
    convert_file("demo.lrt")