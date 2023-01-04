""" This is the main Python file which will do all the Work. """
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
    if not (i.startswith("http://") or i.startswith("https://")):
        response = requests.get(f"http://{i}", verify=False)
        if "X-Frame-Options" in response.headers:
            print("X-Frame-Options header is set")
        else:
            print("X-Frame-Options header is not set and Website might be Vulnerable")
    else:
        response = requests.get(i, verify=False)
        if "X-Frame-Options" in response.headers:
            print("X-Frame-Options header is set")
        else:
            print("X-Frame-Options header is not set and Website might be vulnerable")
print("====================================================================================================================")
print("In case of Any issues please create an issue over Github or contact me on Twitter @0zk3y")
print("====================================================================================================================")
