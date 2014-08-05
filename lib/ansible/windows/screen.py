#-------------------------------------------------------------------------------
# Name:        windows/screen.py
# Purpose:
#
# Author:      Nicolas
#
# Created:     19/07/2014
# Copyright:   (c) Nicolas 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import color_console
import sys

def display_on_screen(msg, color, stderr):
    if color:
        if not color in codeCodes:
            raise Exception, "Unable to find color ", color
        oldColor = color_console.get_text_attr()
        color_console.set_text_attr(codeCodes[color])

    try:
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
    finally:
        if color:
            color_console.set_text_attr(oldColor)

codeCodes = {
    'black':         color_console.FOREGROUND_BLACK,
    'dark gray':     color_console.FOREGROUND_GREY,
    'bright gray':   color_console.FOREGROUND_GREY | color_console.FOREGROUND_INTENSITY,
    'blue':          color_console.FOREGROUND_BLUE | color_console.FOREGROUND_INTENSITY,
    'bright blue':   color_console.FOREGROUND_BLUE | color_console.FOREGROUND_INTENSITY,
    'green':         color_console.FOREGROUND_GREEN,
    'bright green':  color_console.FOREGROUND_GREEN | color_console.FOREGROUND_INTENSITY,
    'cyan':          color_console.FOREGROUND_CYAN,
    'bright cyan':   color_console.FOREGROUND_CYAN | color_console.FOREGROUND_INTENSITY,
    'red':           color_console.FOREGROUND_RED,
    'bright red':    color_console.FOREGROUND_RED | color_console.FOREGROUND_INTENSITY,
    'purple':        color_console.FOREGROUND_MAGENTA,
    'bright purple': color_console.FOREGROUND_MAGENTA | color_console.FOREGROUND_INTENSITY,
    'yellow':        color_console.FOREGROUND_YELLOW,
    'bright yellow': color_console.FOREGROUND_YELLOW | color_console.FOREGROUND_INTENSITY,
    'white':         color_console.FOREGROUND_GREY | color_console.FOREGROUND_INTENSITY,
    'normal':        color_console.get_text_attr() & 0x11
}