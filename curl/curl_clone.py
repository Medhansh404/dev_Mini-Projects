import sys
import os
from urllib.parse import urlparse
import socket
import json

# Step 1: Parse the URL and check for details, Send and print the text from the get request in HTTP format
input_URL = input()
url = urlparse(input_URL)

# Resolve hostname to IP address using DNS
ip_add = socket.gethostbyname(url.hostname)

port = url.port if url.port else 80


# Step 2: Establish a connection with the server and send the above data also print the GET request data
def sock_conn(ip_address, port, request_headers):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

            s.connect_ex((ip_address, port))
            s.sendall(request_headers.encode('utf-8'))

            while True:
                data = s.recv(1024)
                if not data:
                    break
                else:
                    response = (data.decode('utf-8'))
            s.close()
        return response

    except ConnectionError as e:
        print(f"ConnectionError: {e}")


# Step 3: Implementing verbose command functionality and make DELETE method
def get_method():
    method = 'GET'
    request_headers = f'''{method} {url.path} HTTP/1.1\r\n'''
    request_headers += f'''Host: {url.hostname}\r\n'''
    request_headers += f'''Accept: */*\r\n'''
    request_headers += f'''Connection: close\r\n\r\n'''
    get = sock_conn(ip_add, port, request_headers)
    print(get)


get_method()


def post_method(payload, data_header):
    method = 'POST'
    # payload_str = f'{{{", ".join(f"{key}: {json.dumps(value)}" for key, value in payload.items())}}}'
    request_headers = f'''{method} {url.path} HTTP/1.1\r\n'''
    request_headers += f'''Host: {url.hostname}\r\n'''
    request_headers += f'''Content-Length: {len(payload)}\r\n'''
    request_headers += f'''Content-Type: {data_header}\r\n'''
    request_headers += f'''Accept: */*\r\n'''
    request_headers += f'''Connection: close\r\n\r\n'''
    full_request = request_headers + payload
    post = sock_conn(ip_add, port, full_request)
    print(post)


# post_method('{"KEY": "value"}', "application/json")


def delete_method():
    method = 'DELETE'
    request_headers = f'''{method} {url.path} HTTP/1.1\r\n'''
    request_headers += f'''Host: {url.hostname}\r\n'''
    request_headers += f'''Accept: */*\r\n'''
    request_headers += f'''Connection: close\r\n\r\n'''
    delete = sock_conn(ip_add, port, request_headers)
    print(delete)


#delete_method()
