#!/usr/bin/env python

import socket
import struct
import logging


logging.basicConfig(
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

UDP_IP = "0.0.0.0"
UDP_PORT = 9090



#sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
#sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
logging.info("start server on %s and port %s",UDP_IP,UDP_PORT)

while True:
    bytesAddressPair = sock.recv(10240)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]

    logging.info(bytesAddressPair.decode("utf8"))

i
