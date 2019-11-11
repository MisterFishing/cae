#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket
import os

s=socket.socket()
s.bind(('127.0.0.1',1111))

s.listen(5)
while True:
    c,addr = s.accept()
    c.send(os.popen(c.recv(1024)).read())
    c.close()
