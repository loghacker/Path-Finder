#!/usr/bin/python3

import requests
import time
import pyfiglet
import datetime
from os import system
from termcolor import colored
system('clear')
print('-'*60)
path= colored(pyfiglet.figlet_format("P A T H - F I N D E R",'starwars'), 'cyan')
for i in path:
    print(i, end='')
    time.sleep(.001)

print('-'*60)
date = datetime.datetime.now()
print("date", date.date())
print("time", date.time())
print('-'*60, "\n")

path = input("/usr/share/wordlists/dirb/common.txt): ")
print('-', end='')
sub_list = open(path).read()
directories = sub_list.splitlines()
print('-', end='')
a = input("Enter URL (http://google.com/):")

for dir in directories:
    dir_enum = a + dir
    r = requests.get(dir_enum)
    if r.status_code == 404:
        pass
    else:
        print('-', end='')
        print("Directory:", dir_enum)
        print('-', end='')
