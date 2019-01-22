'''
### this is a spider program to monitor the pocket48
### and grab the video from pocket48
### todo: need to monitor the information on bilibili
### and other video or social networks to get a full understanding
### of popularity of particular member
'''

### pocket48 grabber
### begin on 20190118

from optparse import OptionParser
from video_grabber import *

default_download_path = "./download"
'''
 argv: -u/--user membername explaination:qurry the information of member(like member id)
       -t/--team teamname explaination:qurry the information of team(like team id)
       #-c/--clock account psw explaination:clock on
       -d/--download filepath explaination:download the record or live today according to the member id or team id in the file
                              example: -d target.txt
                              example of target.txt:
                              1001(id of team sii)
                              402857(id of member)
       -o/--output path explaination:cooperate wth -d, download the record or live to the appointed path, otherwise
                                     it will be saved in the default path ./download
'''
def setup_parser():
    parser = OptionParser()
    parser.add_option("-u", "--user", action="store", dest="memberName", help="qurry the information of member")
    parser.add_option("-t","--team",action="store", dest="teamName", help="qurry the information of team")
    parser.add_option("-d", "--download", action="store", dest="idPath", help="download the record or live today according to the member id or team id in the file")
    parser.add_option("-o", "--output", action="store", dest="outputPath", help="cooperate wth -d, download the record or live to the appointed path")
    return parser

def main():
    parser = setup_parser()
    (option, args) = parser.parse_args()
    if option.memberName:
        pass
    if option.teamName:
        pass
    if option.idPath:
        #download the record, check the outputpath
        if option.outputPath:
            pass
        else:
            pass

main()

