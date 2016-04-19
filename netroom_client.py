#-*- coding:utf-8 -*-
import socket
import time
import threading

HOST = "127.0.0.1"
PORT = 9988
ADDR = (HOST, PORT)


def send_msg(s):
    while True:
        msg = raw_input()
        s.send(msg)


def get_msg(s):
    while True:
        reply = s.recv(1024)
        print(reply)

c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c_socket.connect(ADDR)

t1 = threading.Thread(target=send_msg, args=(c_socket,))
t2 = threading.Thread(target=get_msg, args=(c_socket,))
t1.start()
t2.start()
