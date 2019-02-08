import requests
import json
import time

from video_grabber import *
from helper.logger import *

SUCCESS_CODE = 200
TOKEN = str(0)

def set_token(token):
    if token:
        global TOKEN
        TOKEN = token

def get_headers():
    HEADERS.update({"token":TOKEN})
    return HEADERS

def check_retcode(message, targetCode=SUCCESS_CODE):
    return message['status'] == targetCode

def pocket48_post(url, data={}):
    #data is a dict, converts it to json
    r = requests.post(url=url, headers=get_headers(), data=json.dumps(data))
    ret = json.loads(r.text)
    if not check_retcode(ret):
        print("http request failed, return message is %s"%ret['message'] if 'message' in ret.keys() else "unknown")
        return None
    content = json.loads(r.text)['content']
    return wrapped_dict(content)

### wrap the api for the video grabber

#login the pocket48
def pocket48_login(account, psw):
    data = {"password":str(psw), "account":str(account)}
    r = pocket48_post(URLS.login, data)
    if not r:
        print("login failed")
    else:
        print("login success")
        set_token(r.token)



#everyday punch, must call pocket48_login first
def pocket48_punch():
    r = pocket48_post(URLS.punch)
    if not r:
        print("punch failed")
    else:
        print("punch succcess")

#check the member live
#groupID could be found above
#memberID, 0 means all
#limit, the limit of response
def pocket48_memberLive(grounpID=0, memberID=0, lastTime=0, limit=10):
    data = {"lastTime":lastTime, "groupId":grounpID, "type":0, "memberID":memberID, "limit":limit}
    r = pocket48_post(URLS.memberLive, data)
    #needs to parse it into a live list
    return r

#check the live information
#isReveiw, 0 means live, 1 means review
#limit, the limit of response
def pocket48_openLive(isReview=0, groupID=0, lastTime=0, limit=20):
    data = {"isReview":isReview, "groupID":groupID, "limit":limit, "lastTime":lastTime}
    r = pocket48_post(URLS.openLive, data)
    #needs to parse it into a live list
    return r

#get the information of the live
#type, 0 means open live or all, 1 means member live
#liveid is the id of live, could be gotten from pocket48_memberLive or pocket48_openLive
def pocket48_getLiveInfo(liveId, type=0):
    data = {"liveId":liveId, "type":type}
    r = pocket48_post(URLS.getLiveOne, data)
    return r

#get the overview of system
def pocket48_syncSystemOverview():
    data = {
        "videoTypeUtime": "2010-03-24 15:59:11",
        "musicAlbumUtime": "2010-04-18 14:45:37",
        "functionUtime": "2010-10-17 15:00:00",
        "groupUtime": "2010-10-17 17:27:00",
        "memberInfoUtime": "2010-10-20 11:55:09",
        "talkUtime": "2010-05-05 18:04:52",
        "videoUtime": "2010-05-17 18:36:32",
        "musicUtime": "2010-05-05 15:56:11",
        "urlUtime": "2010-07-19 12:10:59",
        "teamUtime": "2010-10-20 10:39:00",
        "memberPropertyUtime": "2010-02-20 18:57:48",
        "periodUtime": "2010-10-14 14:45:00"
    }
    r = pocket48_post(URLS.systemOverview, data)
    return r

#get the overview of room
#friends, todo
def pocket48_roomOverview(friends):
    pass

#get the member's message
#roomID, could be gotten by roomOverview
#limit, the limit of member's message
def pocket48_roomMainMessage(roomID, limit=10):
    pass

#get the board message
#roomID, could be gotten by roomOverview
#limit, the limit of member's message
def pocket48_roomBoardMessage(roomID, limit=10):
    pass

#get the user info
def pocket48_userInfo():
    pass

#for test
def main():
    r = pocket48_getLiveInfo("5be14c810cf27e32089828ac")
    jsonPrint(r)
    # pocket48_syncSystemOverview()
    pass
    # pocket48_memberLive()
    # pocket48_openLive(isReview=0)
    # pocket48_getLiveInfo("5c46ee150cf27e32089829ba")
    # print ("============test api pocket48_login============")
    # print (pocket48_login("",""))
    # print ("============test api pocket48_login pass============")
    #
    # print ("============test api pocket48_punch============")
    # print (pocket48_punch())
    # print ("============test api pocket48_punch pass============")
    #
    # print ("============test api pocket48_memberLive============")
    # print (pocket48_memberLive())
    # print ("============test api pocket48_memberLive pass============")
    #
    # print ("============test api pocket48_openLive============")
    # print (pocket48_openLive())
    # print ("============test api pocket48_openLive pass============")
    #
    # print ("============test api pocket48_getLiveInfo============")
    # print (pocket48_getLiveInfo(""))
    # print ("============test api pocket48_getLiveInfo pass============")
    #
    # print ("============test api pocket48_syncSystemOverview============")
    # print (pocket48_syncSystemOverview())
    # print ("============test api pocket48_syncSystemOverview pass============")
    #
    # print ("============test api pocket48_roomOverview============")
    # print (pocket48_roomOverview(""))
    # print ("============test api pocket48_roomOverview pass============")
    #
    # print ("============test api pocket48_roomMainMessage============")
    # print (pocket48_roomMainMessage(""))
    # print ("============test api pocket48_roomMainMessage pass============")
    #
    # print ("============test api pocket48_roomBoardMessage============")
    # print (pocket48_roomBoardMessage(""))
    # print ("============test api pocket48_roomBoardMessage pass============")
    #
    # print ("============test api pocket48_userInfo============")
    # print (pocket48_userInfo())
    # print ("============test api pocket48_userInfo pass============")

if __name__ == "__main__":
    main()