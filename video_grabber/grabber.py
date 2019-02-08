# -*- coding: UTF-8 -*-
### grab the video from pocket 48

import os
import re

from grabber_api import *
from helper import *
from helper.wrapped_dict import wrapped_dict
from video_grabber import Group, Team, Member
cacheFolder = "cache"
overviewCache = "overview.data"

if DEBUG_MODE:
    cachePath = os.path.join(os.path.abspath('..'), cacheFolder)
else:
    cachePath = os.path.join(os.path.abspath('.', cacheFolder))
if not os.path.exists(cachePath):
    os.mkdir(cachePath)

def downloadFile(id, path):
    pass

def cacheOverview(groups):
    overview = {}
    overview.update({"groups":groups})
    overview.update({"utime":int(time.time())})
    file = os.path.join(cachePath, overviewCache)
    overview_json = json.dumps(overview, ensure_ascii=False, indent=4, separators=(",",":"))
    with open(file, 'w') as f:
        f.write(overview_json)

def readCacheOverview():
    cachedFile = os.path.join(cachePath, overviewCache)
    json_file = {}
    with open(cachedFile, 'r') as f:
        json_file = f.read()
    overview = json.loads(json_file)
    return overview["groups"], overview["utime"]

def cacheCurrentTask():
    pass

def updateOverview():
    r = pocket48_syncSystemOverview()
    try:
        groups = {}
        for group in r.groups:#add groups
            new_group = Group(group.group_name, group.group_id)
            groups[group.group_id] = new_group

        teams = {}
        for team in r.teams:#add teams
            new_team = Team(team.team_name, team.team_id, team.group_id)
            groups[team.group_id].teams.append(new_team)
            teams[team.team_id] = []
        for member in r.memberInfo:
            new_member = Member(member.real_name, member.member_id, member.team)
            teams[member.team].append(new_member)

        for team_id in teams.keys():
            for gid in groups.keys():
                tmp_group = groups[gid]
                

    except:
        warning_print("update overview failed, please check the log for detail")
        exit(-1)

def readID(idPath):
    with open(idPath, 'r') as f:
        lines = f.readlines()
    #skip the line begin with '#'
    files = []
    for line in lines:
        if line.startswith('#'):
            continue
        files.append(line)
    return files

#isPath is the a txt that saves the member name or team name,
#according to the member name or team name, it will grab the related video
#outputPath is a path that saves the grabbed video to
def grapvideo(idPath, outputPath, needUpdate):
    #first, read the file according to the idPath
    #parse it and get the member name and team name, it should be a list
    ids = readID(idPath)
    #the example of id:
    #all
    #snh48/gnz48/bej48
    #team nii/team x/etc
    #张茜/张怡/etc

    #then get the memberID or groupID from the cache
    #if they are not cached or it's out of date,
    #we will querry them by pocket48_syncSystemOverview
    if not needUpdate:
        try:
            groups,utime = readCacheOverview()
        except:
            utime = 0#happens some error, so set the utime to 0 to update forcefully
        if int(time.time()) - utime > 2592000:#30*24*60*60
            needUpdate = True
    if needUpdate:
        groups = updateOverview()

    #generally, it will grab the 20 recent videoes
    #and according to the last video name cached
    #get the video to be downloaded
    #get the url and lrt path by pocket48_getLiveInfo
    #download the url and lrt
    #process the lrt into ass file
    #then merge the ass file into video


    cacheOverview(groups)#because we may update the live name of teams, so cache will be the final job to do
    cacheCurrentTask()#cache current task, in next times we will only grab the videoes after current task

def main():
    updateOverview()

#for test
if __name__ == "__main__":
    main()