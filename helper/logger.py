import json

_verbose = True

def jsonPrint(contents):
    if not _verbose and not contents:
        return
    print(json.dumps(contents, sort_keys=True, indent=4, separators=(',',":"), ensure_ascii=False).encode('utf8'))

#error print, the font is bold and the color will be red
#the program will stop
def error_print(message):
    print(message)

#warning print, the font is yellow
#there is some problems but the program could work
def warning_print(message):
    print(message)

#message print, will change the color later
def information_print(message):
    if _verbose:
        print(message)