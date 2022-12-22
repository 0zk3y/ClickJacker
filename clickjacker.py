import requests
import urllib3
urllib3.disable_warnings()

filename = input("Enter the name of the file you want to read: ")
with open(filename, 'r') as f:
    contents = f.read()
    print(contents)
contents = contents.split("\n")[0:-1]
for i in contents:
    print(i)
    i.rstrip()
    if not i.startswith("http://" or "https://"):
        response = requests.get(f"https://{i}", verify=False)
        if "X-Frame-Options" in response.headers:
            print("X-Frame-Options header is set")
        else:
            print("X-Frame-Options header is not set and Website might be vulnerable")
    elif i.startswith("http"):
        i = i[7:]
        response = requests.get(f"http://{i}", verify=False)
        if "X-Frame-Options" in response.headers:
            print("Set")
        else:
            print("Not Set")
