#-*- coding:utf-8 -*-
import socket
import sys
import struct
import time
import thread
import threading

#定义房间ID
ROOMID=586900

#返回当前时间
def get_datetime():
    format = '%Y-%m-%d %H:%M:%S'
    value = time.localtime()
    dt = time.strftime(format, value)
    return dt

#根据时间字符串返回时间戳
def get_timestamp(dt):
     time.strptime(dt, '%Y-%m-%d %H:%M:%S')
     s = time.mktime(time.strptime(dt, '%Y-%m-%d %H:%M:%S'))
     return str(int(s))

#根据主机名称 返回对应的IP地址
def get_host_ip(host):
    try:
        remote_ip = socket.gethostbyname(host)
        return remote_ip
    except e:
        print '找不到主机！'
        sys.exit()

#返回tcp头
def getbyte(data):
    a = struct.pack('i', len(data)+8)
    b = struct.pack('h', 689)
    c = struct.pack('b', 0)
    return a*2+b+c*2+data

#发送心跳包
def send_heartbeat(c_sock):
    while True:
        time.sleep(10)
        msg = 'type@=keeplive/tick@='+get_timestamp(get_datetime())+'/'
        c_sock.send(getbyte(message))
        time.sleep(30)

#接受socket返回
def recv_sock(c_sock):
    print('开始读取弹幕信息：')
    print('------------------------------------------------')
    while True:
        reply = c_sock.recv(4096)
        get_str(reply)
        time.sleep(0.5)

#解析收到的字符串
def get_str(strcon): 
    if 'chatmsg' in strcon:
        strs=str(strcon).split('/')
        for s in strs:
            if 'nn@=' in s:
                cons=s.split('@=')
                username=cons[1]
            if 'txt@=' in s:
                cons=s.split('@=')
                strtext=cons[1]
        print username+" : "+strtext
        



if __name__ == '__main__':

    # 1.创建socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print '创建socket成功！'
    except e:
        print '创建socket失败！'
        sys.exit()

    # 2.连接到远程服务器
    try:
        s.connect((get_host_ip('openbarrage.douyutv.com'), 8601))
        print '已连接到弹幕服务器'
    except Exception, e:
        print e

    # 3.发送登录请求
    message = 'type@=loginreq/roomid@='+str(ROOMID)+'/\0'
    try:
        s.send(getbyte(message))
    except e:
        print '登录失败'
    print '登录成功'

    # 4.加入房间
    message = 'type@=joingroup/rid@='+str(ROOMID)+'/gid@=-9999/\0'
    try:
        s.send(getbyte(message))
    except e:
        print '加入房间失败'
    print '加入房间成功'

    # 5.开始发送心跳包线程 和 接收消息线程
    t1 = threading.Thread(target=send_heartbeat,args=(s,))
    t2 = threading.Thread(target=recv_sock,args=(s,))
    t1.start()
    t2.start()

