import requests
import json
from video_grabber import *

### wrap the api for the video grabber

#login the pocket48
def pocket48_login(account, psw):
    pass

#everyday punch
def pocket48_check():
    pass

#check the member live
#groupID could be found above
#memberID, 0 means all
#limit, the limit of response
def pocket48_memberLive(grounpID=0, memberID=0, limit=20):
    pass

#check the live information
#isReveiw, 0 means live, 1 means review
#limit, the limit of response
def pocket48_openLive(isReview=0, groupID=0, limit=20):
    pass

#get the information of the live
#type, 0 means open live, 1 means member live
#liveid is the id of live, could be gotten from pocket48_memberLive or pocket48_openLive
def pocket48_getLiveInfo(liveid, type=0):
    pass

#get the overview of system
#todo
def pocket48_syncSystemOverview():
    pass

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
    print ("============test api pocket48_login============")
    print (pocket48_login("",""))
    print ("============test api pocket48_login pass============")

    print ("============test api pocket48_check============")
    print (pocket48_check())
    print ("============test api pocket48_check pass============")

    print ("============test api pocket48_memberLive============")
    print (pocket48_memberLive())
    print ("============test api pocket48_memberLive pass============")

    print ("============test api pocket48_openLive============")
    print (pocket48_openLive())
    print ("============test api pocket48_openLive pass============")

    print ("============test api pocket48_getLiveInfo============")
    print (pocket48_getLiveInfo(""))
    print ("============test api pocket48_getLiveInfo pass============")

    print ("============test api pocket48_syncSystemOverview============")
    print (pocket48_syncSystemOverview())
    print ("============test api pocket48_syncSystemOverview pass============")

    print ("============test api pocket48_roomOverview============")
    print (pocket48_roomOverview(""))
    print ("============test api pocket48_roomOverview pass============")

    print ("============test api pocket48_roomMainMessage============")
    print (pocket48_roomMainMessage(""))
    print ("============test api pocket48_roomMainMessage pass============")

    print ("============test api pocket48_roomBoardMessage============")
    print (pocket48_roomBoardMessage(""))
    print ("============test api pocket48_roomBoardMessage pass============")

    print ("============test api pocket48_userInfo============")
    print (pocket48_userInfo())
    print ("============test api pocket48_userInfo pass============")

if __name__ == "__main__":
    main()