#-*- coding:utf-8 -*-
import socket
import time
import threading

HOST = ""
PORT = 9988
BUFFSIZE = 1024
CONNECTNUM = 10
ADDR = (HOST, PORT)
c_sockets = []

# 返回当前时间


def get_datetime():
    format = '%Y-%m-%d %H:%M:%S'
    value = time.localtime()
    dt = time.strftime(format, value)
    return dt


def get_msg(s, addr):
    while True:
        try:
            recv = s.recv(BUFFSIZE)
        except socket.error, e:
            break
        if not recv:
            break
        else:
            for sock in c_sockets:
                try:
                    sock.send(
                        "[{0}] 用户{1}:{2}".format(get_datetime(), addr[0], recv))
                except socket.error, e:
                    del sock


s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_socket.bind(ADDR)
s_socket.listen(CONNECTNUM)

while True:
    c_socket, addr = s_socket.accept()
    print("{0}加入房间...".format(addr[0]))
    c_sockets.append(c_socket)
    t1 = threading.Thread(target=get_msg, args=(c_socket, addr))
    t1.start()
