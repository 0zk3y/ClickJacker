import requests

filename = input("Enter the name of the file you want to read: ")
try:
    with open(filename, 'r') as f:
        contents = f.read()
    print(contents)
except FileNotFoundError:
    print("The file you entered does not exist.")
response = requests.get()
# Check if the X-Frame-Options header is set
if "X-Frame-Options" in response.headers:
    print("X-Frame-Options header is set")
else:
    print("X-Frame-Options header is not set")
