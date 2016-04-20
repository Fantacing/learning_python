#-*- coding:utf-8 -*-
import socket
import threading

HOST = ""
PORT = 9988
BUFFSIZE = 1024
CONNECTNUM = 10
ADDR = (HOST, PORT)
c_sockets = []


# 接收客户端消息 并返回给客户端
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
                        "{0} : {1}".format(str(addr[0]), str(recv)))
                except socket.error, e:
                    del sock

if __name__ == '__main__':
    s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_socket.bind(ADDR)
    s_socket.listen(CONNECTNUM)

    while True:
        c_socket, addr = s_socket.accept()
        print(u"{0}加入房间...".format(addr[0]))
        c_sockets.append(c_socket)
        t1 = threading.Thread(target=get_msg, args=(c_socket, addr))
        t1.start()
