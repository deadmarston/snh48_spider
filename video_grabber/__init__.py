from helper.wrapped_dict import wrapped_dict
import random

DEBUG_MODE = 1#a debug switch for test

IMEI = str(random.randint(10000000, 99999999))

HEADERS = {
    "os": "android",
    "IMEI": IMEI,
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