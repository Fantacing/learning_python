#-*- coding:utf-8 -*-
import socket
import time
import threading

HOST = "127.0.0.1"
PORT = 9988
ADDR = (HOST, PORT)

# 返回当前时间
def get_datetime():
    format = '%Y-%m-%d %H:%M:%S'
    value = time.localtime()
    dt = time.strftime(format, value)
    return str(dt)

# 接收用户输入
def send_msg(s):
    while True:
        msg = raw_input()
        s.send(msg)

# 接收服务器端消息
def get_msg(s):
    while True:
        try:
            reply = s.recv(1024)
            print("[{0}] {1}".format(get_datetime(),reply))
        except socket.error, e:
            print(u"与服务器断开连接...")
            s.close()
            break


if __name__ == '__main__':
    c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c_socket.connect(ADDR)

    t1 = threading.Thread(target=send_msg, args=(c_socket,))
    t2 = threading.Thread(target=get_msg, args=(c_socket,))
    t1.start()
    t2.start()
