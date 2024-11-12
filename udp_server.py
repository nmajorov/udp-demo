#!/usr/bin/env python

import socket
import struct
import logging

#sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
#sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind(("0.0.0.0", 9090))


while True:
    bytesAddressPair = sock.recv(10240)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]

    print(bytesAddressPair.decode("utf8"))

i
