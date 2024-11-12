#!/usr/bin/env python

import socket
import os

UDP_IP = os.environ.get("UDP_IP", "O.0.0.0")

UDP_PORT = os.environ.get("UDP_PORT", 9090)

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

message = "bam".encode("UTF-8")
print("sending mesage " % message )
sock.sendto(message,(UDP_IP, UDP_PORT))
