# -*- coding: UTF-8 -*-

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
import datetime
import os
import re
import chardet

from video_grabber import *
from helper.logger import *

INPUT_BULLETSCREEN_FILE = Enum('INPUT_BULLETSCREEN_FILE', ('lrc', 'xml'))

TUPLE_TIME_INDEX = 0
TUPLE_AUTHOR_INDEX = 1
TUPLE_MESSAGE_INDEX = 2

BULLET_SCREEN_FOLDER = 'bulletscreen'
if DEBUG_MODE:
    DEFAULT_OUTPUT_PATH = os.path.join(os.path.abspath('..'), BULLET_SCREEN_FOLDER)
else:
    DEFAULT_OUTPUT_PATH = os.path.join(os.path.abspath('.'), BULLET_SCREEN_FOLDER)

#the postprogressed ass file should be saved into the preset path
#and return the path to the caller


def convert_file(input_file, input_type=INPUT_BULLETSCREEN_FILE.lrc, path=DEFAULT_OUTPUT_PATH, height=960, width=540, offset=0):
    checkOrCreateFolder(path)
    now = time.strftime("%Y%m%d", time.localtime(time.time()))
    subpath = os.path.join(path, now)
    checkOrCreateFolder(subpath)
    file = os.path.basename(input_file)
    if input_type == INPUT_BULLETSCREEN_FILE.lrc:
        outputFile = file.rstrip(".lrc")+".ass"
        outputPath = os.path.join(subpath, outputFile)
        convert_lrc(input_file, outputPath, height, width, offset)
    elif input_type == INPUT_BULLETSCREEN_FILE.xml:
        pass
    else:
        raise Exception('no such input bulletscreen type, must be lrt or xml, please check the origin file')

def convert_lrc(input_file, outputPath, height, width, offset=0):
    messages = read_lrc_files(input_file)
    lines = []
    lines.extend(generate_header(height, width))
    lines.extend(generate_styles(height, width))
    lines.extend(generate_events(messages, height, width, offset=offset))
    writeAssFile(lines, outputPath)

def convert_xml(input_file):
    pass

def writeAssFile(lines, outputPath):
    with open(outputPath, 'w') as f:
        for line in lines:
            f.write(line)

def generate_header(height, width, title="Bullet Screen"):
    lines = []
    lines.append("[Script Info]\n")
    lines.append("Title: %s\n"%title)
    lines.append("Original Script: converted from lrc or xml file\n")
    lines.append("ScriptType: v4.00+\n")
    lines.append("Collisions: Normal\n")
    lines.append("PlayResX: %d\n"%width)
    lines.append("PlayResY: %d\n"%height)
    lines.append("Timer: 100.0000\n")
    lines.append("\n")
    return lines

def generate_styles(height, width):
    lines = []
    lines.append("[V4+ Styles]\n")
    #todo:
    fontSize = height/20/1.5
    lines.append("Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding\n")
    lines.append("Style: R2L,Microsoft YaHei UI,%d,&H66FFFFFF,&H66FFFFFF,&H66000000,&H66000000,1,0,0,0,100,100,0,0,1,2,0,2,20,20,2,0\n"%fontSize)
    lines.append("\n")
    return lines

def generate_events(messages, height, width, last=10.0, offset=0):
    #init the variable
    bullet_screen_tables = [0.0 for i in range(0, 10)]#a table to record the power of this line, the value is smaller, this line is better to insert a bullet screen
    beginWidth = width
    endWidth = 0

    perLineHeight = height/20.0/1.5#for each word, the height and width should be about height/20/1.5
    beginHeight = perLineHeight

    speed = (beginWidth-endWidth)/last

    '''
    ******width******  the bullet screen will only show in the up half screen
    *****************
    ****************h
    ****************e
    ****************i  
    ****************g
    ****************h
    ****************t
    *****************
    
    divide the screen into 20 piece, only first 10 piece will have bullet screen
    the bullet screen comes from right to left
    '''
    lines = []
    lines.append("[Events]\n")
    lines.append("Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n")

    lastBulletScreenTime = "00:00:00.00"
    for eachMessage in messages:
        time = eachMessage[TUPLE_TIME_INDEX]

        if time > lastBulletScreenTime:
            deltaTime = datetime.datetime.strptime(time, "%H:%M:%S.%f") - datetime.datetime.strptime(lastBulletScreenTime, "%H:%M:%S.%f")
        else:
            deltaTime = datetime.datetime.strptime(lastBulletScreenTime, "%H:%M:%S.%f") - datetime.datetime.strptime(
                time, "%H:%M:%S.%f")
        if deltaTime.days < 0:
            deltaTime = deltaTime + datetime.timedelta(days=1)
        deltaTime = deltaTime.seconds
        lastBulletScreenTime = time

        #needs to get a free line to insert bullet screen
        _min = 0

        for i in range(0, len(bullet_screen_tables)):
            bullet_screen_tables[i] = max(0, bullet_screen_tables[i] - deltaTime * speed)
            if bullet_screen_tables[_min] > bullet_screen_tables[i]:
                _min = i

        lineHeight = _min * perLineHeight + beginHeight

        messageLength = len(eachMessage[TUPLE_MESSAGE_INDEX])
        alignWidth = messageLength/4 * perLineHeight

        lineBeginWidth = beginWidth + alignWidth
        lineEndWidth = endWidth - alignWidth
        lineLast = (lineBeginWidth - lineEndWidth) / speed
        beginTime, endTime = getStandardTimes(time, last=lineLast, offset=offset)

        bullet_screen_tables[_min] = bullet_screen_tables[_min] + perLineHeight*(messageLength+1)
        lines.append("Dialogue: 0,%s,%s,R2L,,20,20,2,,{\move(%f,%f,%f,%f)}%s\n"%(beginTime, endTime, lineBeginWidth, lineHeight, lineEndWidth, lineHeight, eachMessage[TUPLE_MESSAGE_INDEX]))


    return lines

def getStandardTimes(beginTime, last = 10, offset=0):
    beginTimeInDate = datetime.datetime.strptime(beginTime, "%H:%M:%S.%f")-datetime.timedelta(seconds=offset)
    endTimeInDate = beginTimeInDate+datetime.timedelta(seconds=last)
    return beginTimeInDate.strftime("%H:%M:%S.%f")[:-4], endTimeInDate.strftime("%H:%M:%S.%f")[:-4]

def read_lrc_files(input_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()
    messages = []
    for line in lines:
        match = re.search(r'(?P<time>\[\d{2}:\d{2}:\d{2}.\d{2}\])(?P<message>.*)', line)
        if not match:
            warning_print("the bullet screen: ( %s ) happens some error during searching, please check"%line)
            continue
        try:
            realtime = match.group("time").strip("][")
            author = match.group("message").split("\t")[0]
            message = match.group("message").split("\t")[1]
        except:
            warning_print("the bullet screen: ( %s ) happens some error during splitting, please check" % line)
            continue
        messages.append((realtime, author, message))
    return messages


def getFileName(file):
    return file.split('.')[0]

def checkOrCreateFolder(path):
    if os.path.exists(path):
        if os.path.isdir(path):
            return
    os.mkdir(path)

if __name__ == "__main__":
    #test
    convert_file("rutusuoshi.lrc", offset = 30)
