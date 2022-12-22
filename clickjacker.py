import requests

# Send a request to the URL
response = requests.get("http://example.com")

# Check if the X-Frame-Options header is set
if "X-Frame-Options" in response.headers:
    print("X-Frame-Options header is set")
else:
    print("X-Frame-Options header is not set")
