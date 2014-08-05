#-------------------------------------------------------------------------------
# Name:        screen
# Purpose:
#
# Author:      Nicolas
#
# Created:     19/07/2014
# Copyright:   (c) Nicolas 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys
from ansible.color import stringc

if sys.platform == 'win32':
    from .windows.screen import display_on_screen as dos
    def display_on_screen(msg, color, stderr):
        dos(msg, color, stderr)

else:
    def display_on_screen(msg, color = None, stderr = false):
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