# -*- coding: UTF-8 -*-
from helper.wrapped_dict import wrapped_dict
from helper.imei_generator import generateImei
import random
import enum

DEBUG_MODE = 1#a debug switch for test

HEADERS = {
    "os": "android",
    "IMEI": generateImei(),
    "build": "0",
    "version": "5.3.1",
    "Content-Type": "application/json;charset=utf-8",
}

URLS = wrapped_dict({
    "login":"https://puser.48.cn/usersystem/api/user/v1/login/phone",
    "punch":"https://puser.48.cn/usersystem/api/user/v1/check/in",
    "memberLive":"https://plive.48.cn/livesystem/api/live/v1/memberLivePage",
    "openLive":"https://plive.48.cn/livesystem/api/live/v1/openLivePage",
    "getLiveOne":"https://plive.48.cn/livesystem/api/live/v1/getLiveOne",
    "systemOverview":"https://psync.48.cn/syncsystem/api/cache/v1/update/overview",
    "roomList":"https://pjuju.48.cn/imsystem/api/im/room/v1/login/user/list",
    "roomMain":"https://pjuju.48.cn/imsystem/api/im/v1/member/room/message/mainpage",
    "roomBoard":"https://pjuju.48.cn/imsystem/api/im/v1/member/room/message/boardpage",
    "userInfo":"https://puser.48.cn/usersystem/api/user/v1/show/info/123456",
})

#json in cache
PERSONAL_LIVE_KEYWORD_TITLE = ["生日会", "Mini Live"]
SPECIAL_LIVE_KEYWORD_SUBTITLE = "联合"


class Group(object):
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.teams = []

    def isOneOfTeams(self, teamName):
        return self.getTeam(teamName) != None

    def getTeam(self, teamName):
        for team in self.teams:
            if teamName == team.name:
                return team
        return None

    def getMember(self, memberName, conditionalName=None):
        if conditionalName:
            team = self.getTeam(conditionalName)
            if conditionalName != self.name and not team:
                return None
            return team.getMember(memberName)
        for team in self.teams:
            member = team.getMember(memberName)
            if member:
                return member
        return None

    def isOneOfMembers(self, memberName, conditionalName=None):
        return self.getMember(memberName, conditionalName) == None

class Team(object):
    def __init__(self, name, id, gid = "", group = ""):
        self.name = name
        self.id = id
        self.group = group
        self.gid = gid
        self.members = {}
        self.liveName = ""#current live name
        try:
            self.alias = self.name.split(' ')[1][0]#sometimes, pocket48 uses alias instead of full team name, like N instead of NII
        except:
            self.alias = ""

    def getMember(self, memberName):
        for member in self.members:
            if member.name == memberName:
                return member
        return None

    def isOneOfMembers(self, memberName):
        return self.getMember(memberName) != None

class Member(object):
    def __init__(self, name, id, tid = ""):
        self.name = name
        self.id = id
        self.tid = tid
