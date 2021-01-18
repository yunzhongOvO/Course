#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：server.py
 
import socket               # 导入 socket 模块
import time
import threading

s = socket.socket()         # 创建 socket 对象
host = socket.gethostname() # 获取本地主机名
port = 12346              # 设置端口
s.bind((host, port))        # 绑定端口
 
s.listen(5)                 # 等待客户端连接
c,addr = s.accept()     # 建立客户端连接
print('连接地址：', addr)
c.send('msg'.encode())
time.sleep(2)

start_count = 101
recv_count = 0
msg_count = 0
keep_count = 0

while True:
    msg = c.recv(1024).decode()
    print(msg)
    if(msg == 'msg'):
        recv_count +=1
        msg_count += 1
        c.send('msg'.encode())

    if(msg == 'marker'):
        print('state:',keep_count)
        print('msg:',msg_count)
        exit()

    if recv_count == start_count:
        c.send('marker'.encode())
        print('state:',recv_count)
        keep_count = recv_count
        msg_count = 0
        print('msg:',msg_count)   
    
    time.sleep(0.1)

c.close()                # 关闭连接
