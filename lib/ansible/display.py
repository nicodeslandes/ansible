#-------------------------------------------------------------------------------
# Name:        display
# Purpose:
#
# Author:      Nicolas
#
# Created:     19/07/2014
# Copyright:   (c) Nicolas 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os

if (os.name == "nt"):
    import win32.display
    return

def display_on_screen(msg, color, stderr):
    if color:
        msg = stringc(msg, color)
    if not stderr:
        try:
            print msg
        except UnicodeEncodeError:
            print msg.encode('utf-8')
    else:
        try:
            print >>sys.stderr, msg
        except UnicodeEncodeError:
            print >>sys.stderr, msg.encode('utf-8')