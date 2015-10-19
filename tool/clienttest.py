# coding:utf8

import time

from socket import AF_INET, SOCK_STREAM, socket
from thread import start_new
import struct
HOST = 'magnus1k.com'
PORT = 1000
BUFSIZE = 1024
ADDR = (HOST, PORT)
client = socket(AF_INET, SOCK_STREAM)
client.connect(ADDR)


def send_data(sendstr, command_id):
    head_0 = chr(0)
    head_1 = chr(0)
    head_2 = chr(0)
    head_3 = chr(0)
    proto_version = chr(0)
    server_version = 0
    sendstr = sendstr
    data = struct.pack('!sssss3I', head_0, head_1, head_2,
                       head_3, proto_version, server_version,
                       len(sendstr)+4, command_id)
    senddata = data+sendstr
    return senddata


def resolve_recvdata(data):
    head = struct.unpack('!sssss3I', data[:17])
    length = head[6]
    data = data[17:17+length]
    return data

s1 = time.time()


def start():
    for num in xrange(10):
        client.sendall(send_data('asdfe', 1))

for i in range(10):
    start_new(start, ())
while True:
    pass

