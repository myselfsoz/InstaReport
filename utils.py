# coding=utf-8
#!/usr/bin/env python3

from colorama import Fore, Back, Style
from os import path
import re
import random
from requests import get
from sys import exit
import time
import os
        
def print_success(message, *argv):
    print(Fore.GREEN + "[ OK ] " + Style.RESET_ALL + Style.BRIGHT, end="")
    print(message, end=" ")
    for arg in argv:
        print(arg, end=" ")
    print("")

def print_error(message, *argv):
    print(Fore.RED + "[ ERR ] " + Style.RESET_ALL + Style.BRIGHT, end="")
    print(message, end=" ")
    for arg in argv:
        print(arg, end=" ")
    print("")

def print_status(message, *argv):
    print(Fore.BLUE + "[ * ] " + Style.RESET_ALL + Style.BRIGHT, end="")
    print(message, end=" ")
    for arg in argv:
        print(arg, end=" ")
    print("")

def clearConsole():
    os.system('clear')

def parse_proxy_file(link):
    proxies = []
    r=get(link)
    t=(r.text).split("\n")
    iterator=1
    for line in t:
            line = line.replace(" ", "")
            line = line.replace("\r", "")
            line = line.replace("\n", "")
            
            if (line ==  ""):
                continue
            
            proxies.append(line)
            #if(iterator==50): #limited to 50 proxies
                #break
            iterator=iterator+1
        
    print("")
    print_success(str(len(proxies)) + " Proxies have been installed!")

    return proxies
