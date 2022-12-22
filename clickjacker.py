import requests

filename = input("Enter the name of the file you want to read: ")
with open(filename, 'r') as f:
    contents = f.readlines()
for i in contents:
    print(i)
    if not i.startswith("http://"):
        response = requests.get(f"https://{i.replace('%0a','')}")
        if "X-Frame-Options" in response.headers:
            print("X-Frame-Options header is set")
        else:
            print("X-Frame-Options header is not set and Website might be vulnerable")