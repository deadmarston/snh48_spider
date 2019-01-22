
_verbose = True

#error print, the font is bold and the color will be red
def error_print(message):
    print(message)

#message print, will change the color later
def information_print(message):
    if _verbose:
        print(message)