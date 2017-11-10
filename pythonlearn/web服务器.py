#socket
import socket
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(('www.baidu.com',80))

mysocket.send('GET https://www.baidu.com/robots.txt HTTP/1.0\n\n')

while True:
    data = mysocket.recv(1024)
    if (len(data) < 1):
        break
    print(data)
mysocket.close
