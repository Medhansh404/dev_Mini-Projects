# Objective: to build a CLI tool for sending HTTP requests.
# Type 1. send n no. of requests synchronously, Type 2. send n no. of requests with c of them concurrently
# Test success rate of requests and success rate
# Time for each request to be fulfilled
# check for all the requests inside the text file

import os
import sys
from urllib.parse import urlparse
import socket
import selectors
import types

ex_url = "ccload -u http://localhost:8000 -n 100 -c 10"
x = sys.argv
print(x)


def url_ident(arg) -> str:
    # method 1: access the url directly
    if arg == 'u':
        url = x[2]
    # method 2: access the file that has the urls
    if arg == 'f':
        file = x[2]

    return url


url = url_ident(x[1:])
url = urlparse(url)
ip_add = socket.gethostbyname(url.hostname)
port = url.port if url.port else 80


def method_ident(arg):
    if arg == 'n':
        count = x[4]

    if arg == 'c':
        conc_count = x[6]

    return (count, conc_count)


n, c = method_ident(x[1:])

method = 'GET'
request_headers = f'''{method} {url.path} HTTP/1.1\r\n'''
request_headers += f'''Host: {url.hostname}\r\n'''
request_headers += f'''Accept: */*\r\n'''
request_headers += f'''Connection: close\r\n\r\n'''


def network_setup(arg: bool):
    # sending multiple requests
    if arg:
        sel = selectors.DefaultSelector()

        def start_connections(host, port, num_conns):
            server_addr = (host, port)
            for i in range(0, num_conns):
                connid = i + 1
                print(f"Starting connection {connid} to {server_addr}")
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.setblocking(False)
                sock.connect_ex(server_addr)
                events = selectors.EVENT_READ | selectors.EVENT_WRITE
                data = types.SimpleNamespace(
                    connid=connid,
                    msg_total=sum(len(request_headers)),
                    recv_total=0,
                    messages=request_headers.copy(),
                    outb=b"",
                )
                sel.register(sock, events, data=data)

        def service_connection(key, mask):
            sock = key.fileobj
            data = key.data
            if mask & selectors.EVENT_READ:
                recv_data = sock.recv(1024)  # Should be ready to read
                if recv_data:
                    data.outb += recv_data
                    print(f"Received {recv_data!r} from connection {data.connid}")
                    data.recv_total += len(recv_data)
                else:
                    print(f"Closing connection {data.connid}")
                if not recv_data or data.recv_total == data.msg_total:
                    print(f"Closing connection {data.connid}")
                    sel.unregister(sock)
                    sock.close()

            if mask & selectors.EVENT_WRITE:

                if not data.outb and data.messages:
                    data.outb = data.messages.pop(0)
                if data.outb:
                    print(f"Echoing {data.outb!r} to {data.addr}")
                    print(f"Sending {data.outb!r} to connection {data.connid}")
                    sent = sock.send(data.outb)  # Should be ready to write
                    data.outb = data.outb[sent:]
