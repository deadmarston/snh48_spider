### grab the video from pocket 48

import requests
import json

from grabber_api import *
memberUrl = 'https://plive.48.cn/livesystem/api/live/v1/memberLivePage'

params = {
    "lastTime": 0,
    "groupId": 0,
    "type": 0,
    "memberId": 0,
    "giftUpdTime": 1498211389003,
    "limit": 20
}

def main():
    r = requests.post(url=memberUrl, headers="", data=json.dumps(params))
    print(r.text)

#for test
if __name__ == "__main__":
    main()