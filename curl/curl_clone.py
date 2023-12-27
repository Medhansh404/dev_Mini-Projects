import sys
import os
from urllib.parse import urlparse
import socket

# Step 1: Parse the URL and check for details, Send and print the text from the get request in HTTP format
input_URL = input()
url = urlparse(input_URL)

# Resolve hostname to IP address using DNS
ip_address = socket.gethostbyname(url.hostname)

port = url.port if url.port else 80
request_headers = f'''GET {url.path} HTTP/1.1\r\n'''
request_headers += f'''Host: {url.hostname}\r\n'''
request_headers += f'''Accept: */*\r\n'''
request_headers += f'''Connection: close\r\n\r\n'''

print(f'''connecting to {url.hostname}
    Sending request {request_headers}''')

# Step 2: Establish a connection with the server and send the above data also print the get request data
try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.connect_ex((ip_address, port))
        s.sendall(request_headers.encode('utf-8'))

        while True:
            data = s.recv(1024)
            if not data:
                break
            else:
                print(data.decode('utf-8'))

except ConnectionError as e:
    print(f"ConnectionError: {e}")

# Step 3: Implementing verbose command functionality and make POST command
