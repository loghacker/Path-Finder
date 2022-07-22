import requests

path = input("Enter wordlist (/usr/share/rockyout.txt): ")

sub_list = open(path).read()
directories = sub_list.splitlines()
a = input("Enter URL (http://google.com/):")

for dir in directories:
    dir_enum = a + dir
    r = requests.get(dir_enum)
    if r.status_code == 200:
        print("Directory:", dir_enum)
        print(r.text)
        break
    else:
        pass
