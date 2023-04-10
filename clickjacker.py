""" This is the main Python file which will do all the Work. """
import requests
import urllib3
urllib3.disable_warnings()

 

try:
    filename = input("Enter the name of the file you want to read: ")
    if not filename:
        print("File name cannot be empty")
        exit()
    with open(filename, 'r') as f:
        contents = f.read()
        if not contents:
            print("File is empty")
            exit()
        contents = contents.split("\n")
        for i in contents:
            i = i.strip()
            if not i:
                print("Hostname cannot be empty")
                continue
            try:
                if not (i.startswith("http://") or i.startswith("https://")):
                    i = f"http://{i}"
                response = requests.get(i, verify=False, timeout=5)
                if "X-Frame-Options" in response.headers:
                    print(f"{i}: X-Frame-Options header is set")
                else:
                    print(f"{i}: X-Frame-Options header is not set and website might be vulnerable")
            except requests.exceptions.RequestException as e:
                print(f"Error connecting to {i}: {e}")
            except requests.exceptions.Timeout:
                print(f"Connection timed out for {i}")
except FileNotFoundError as e:
    print(f"File not found: {e}")
except ValueError as e:
    print(f"Error in file contents: {e}")

print("====================================================================================================================")
print("In case of Any issues please create an issue over Github or contact me on Twitter @0zk3y")
print("====================================================================================================================")
