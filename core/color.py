#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import ctypes
from termcolor import colored

STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE= -11
STD_ERROR_HANDLE = -12

FOREGROUND_BLACK = 0x0
FOREGROUND_YELLOW = 0x0e # text color contains yellow.
FOREGROUND_BLUE = 0x01 # text color contains blue.
FOREGROUND_GREEN= 0x02 # text color contains green.
FOREGROUND_RED = 0x04 # text color contains red.
FOREGROUND_INTENSITY = 0x08 # text color is intensified.

BACKGROUND_BLUE = 0x10 # background color contains blue.
BACKGROUND_GREEN= 0x20 # background color contains green.
BACKGROUND_RED = 0x40 # background color contains red.
BACKGROUND_INTENSITY = 0x80 # background color is intensified.

class WindowsColor(object):
    ''' See http://msdn.microsoft.com/library/default.asp?url=/library/en-us/winprog/winprog/windows_api_reference.asp
    for information on Windows APIs.'''
    std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    
    def __set_cmd_color(self, color, handle=std_out_handle):
        """(color) -> bit
        Example: __set_cmd_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE | FOREGROUND_INTENSITY)
        """
        bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
        return bool
    
    def __reset_color(self):
        self.__set_cmd_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE | FOREGROUND_YELLOW)
        
    def print_red_text(self, print_text):
        self.__set_cmd_color(FOREGROUND_RED | FOREGROUND_INTENSITY)
        print(print_text)
        self.__reset_color()
        
    def print_yellow_text(self, print_text):
        self.__set_cmd_color(FOREGROUND_YELLOW | FOREGROUND_INTENSITY)
        print(print_text)
        self.__reset_color()
        
    def print_green_text(self, print_text):
        self.__set_cmd_color(FOREGROUND_GREEN | FOREGROUND_INTENSITY)
        print(print_text)
        self.__reset_color()
    
    def print_blue_text(self, print_text): 
        self.__set_cmd_color(FOREGROUND_BLUE | FOREGROUND_INTENSITY)
        print(print_text)
        self.__reset_color()
          
    def print_red_text_with_blue_bg(self, print_text):
        self.__set_cmd_color(FOREGROUND_RED | FOREGROUND_INTENSITY| BACKGROUND_BLUE | BACKGROUND_INTENSITY)
        print(print_text)
        self.__reset_color()    


class Color(object):
    
    def print_red_text(self, text):
        print(colored(text, 'red'))
    
    def print_green_text(self, text):
        print(colored(text, 'green'))

    def print_blue_text(self, text):
        print(colored(text, 'blue'))

    def print_yellow_text(self, text):
        print(colored(text, 'yellow'))

def getColor():
    if os.name == 'nt':
        return WindowsColor()
    else:
        return Color()

if __name__ == "__main__":
    clr = getColor()
    clr.print_red_text('red')
    