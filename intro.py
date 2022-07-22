#!/usr/bin/python
from os import system
import time
import pyfiglet
from termcolor import colored


a = colored(pyfiglet.figlet_format('DISCLAIMER !', justify='center'), 'red')
system('clear')
for i in a:
    print(i, end='')
    time.sleep(.01)
for i in range(100):
    print('-', end='')
    time.sleep(.01)
print('\n')
b = """This information is provided to assist users of Path-Finder in scanning their own domain,
 for which they have been given permission to scan, in order to determine the security of such domain. 
it is not intended to assist with scanning remote sites with the intention of breaking into or exploiting services on 
those sites,  or for imformation gathering purposes beyond those allowed by law.
"""
b = colored(b, 'green')

c = '''We hereby disclaim any responsibility for actions taken based upon the information in this article,
and urge all who seek information towards a destructive end to reconsider their life,
and do something constructive instead.
'''

c = colored(c, 'yellow')

for i in b:
    print(i, end='')
    time.sleep(.005)
print('\n\n')
for i in c:
    print(i, end='')
    time.sleep(.005)
time.sleep(5)
system('clear')

