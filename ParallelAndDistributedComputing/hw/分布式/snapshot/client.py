#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：client.py
 
import socket               # 导入 socket 模块
import time
s = socket.socket()         # 创建 socket 对象
host = socket.gethostname() # 获取本地主机名
port = 12346                # 设置端口号
 
s.connect((host, port))
recv_count = 0
msg_count = 0
while True:
    msg = s.recv(1024).decode()
    print(msg)
    if(msg == 'msg'):
        recv_count +=1
        msg_count += 1
        s.send('msg'.encode()) 
           
    if(msg == 'marker'):
        msg_count = 0
        print('state:',recv_count)
        print('msg:',msg_count)
        s.send('marker'.encode())
    
    time.sleep(0.1)
s.close()
