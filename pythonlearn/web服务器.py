import socket
mysocket = socket.socket(socket.AF_INET,socket.SOCk_STREAM)
mysocket.connect(('wwww.pythonlearn.com', 80))

mysocket.send('GET')