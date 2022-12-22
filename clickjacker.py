import requests

filename = input("Enter the name of the file you want to read: ")
try:
    with open(filename, 'r') as f:
        contents = f.readlines()
    for i in contents:
        print(i)
        response = requests.get(url)
        if "X-Frame-Options" in response.headers:
            print("X-Frame-Options header is set")
        else:
            print("X-Frame-Options header is not set and Website might be vulnerable")
except FileNotFoundError:
    print("The file you entered does not exist.")