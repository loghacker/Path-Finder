import time
import pyfiglet
import datetime
from os import system
from termcolor import colored
import os.path

if os.path.exists('intro.py'):
    system('./intro.py')


system('clear')	#clears the screen
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


a="""
Choose option:
    1. Directory Traversal
    2. Directory brute force
"""

print(a)
try:
    a = int(input("Enter here: "))
    if a==1:
        system('path_travesal/path.py')
    elif a==2:
        system('path_travesal/directary.py')
    else:
      print("Wrong Entry")
except KeyboardInterrupt:
    print("\n\n")
    back = input("Do you want to EXIT (y/n): ")
    if back == 'n' or back == 'N':
        system('./main.py')

    else:
        print("Exiting...")
except TypeError:
    print("Invalid Type   Exiting....")
except:
    print("Unexpected error occured try again")
