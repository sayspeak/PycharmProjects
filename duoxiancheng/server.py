import socket
import threading
import os
import sys
import math
import time

bindIp = "0.0.0.0"
bindPort = 9999
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bindIp, bindPort))
server.listen(20)
print("Listening on %s:%d" % (bindIp, bindPort))


def getFileSize(file):
    file.seek(0, os.SEEK_END)
    fileLength = file.tell()
    file.seek(0, 0)
    return fileLength


def writeFilePart(threadCount, fileName, fileSize, clientSocket):
    try:
        threadIndex = int(clientSocket.recv(1024))
        clientSocket.send("Received")
        filePartName = fileName + str(threadIndex)
        filePartSize = fileSize / threadCount
        lengthToWrite = filePartSize
        if threadIndex == threadCount:
            lengthToWrite = fileSize - filePartSize * (threadCount - 1)
        file = open(filePartName, "wb")
        receivedLength = 0
        while receivedLength < lengthToWrite:
            bufLen = 1024
            buf = clientSocket.recv(bufLen)
            file.write(buf)
            receivedLength += len(buf)
        file.close()
        sem.release()
        # print("thread %d finished, size received %d") % (threadIndex, receivedLength)
    except Exception:
        print(Exception)


def checkFileName(originalFileName):
    extensionIndex = originalFileName.rindex(".")
    name = originalFileName[:extensionIndex]
    extension = originalFileName[extensionIndex + 1:]

    index = 1
    newNameSuffix = "(" + str(index) + ")"
    finalFileName = originalFileName
    if os.path.exists(finalFileName):
        finalFileName = name + " " + newNameSuffix + "." + extension
    while os.path.exists(finalFileName):
        index += 1
        oldSuffix = newNameSuffix
        newNameSuffix = "(" + str(index) + ")"
        finalFileName = finalFileName.replace(oldSuffix, newNameSuffix)
    return finalFileName


def writeFile(fileName, threadCount):
    file = open(fileName, "wb")
    for i in range(threadCount):
        filePartName = fileName + str(i + 1)
        # print "Reading file %s" % filePartName
        filePart = open(filePartName, "rb")
        filePartSize = getFileSize(filePart)
        lengthWritten = 0
        while lengthWritten < filePartSize:
            bufLen = 1024
            buf = filePart.read(bufLen)
            file.write(buf)
            lengthWritten += len(buf)
        filePart.close()
        os.remove(filePartName)
    file.close()


sem = threading.Semaphore(0)

while True:
    client, addr = server.accept()
    print("[*] Accepted connection from: %s:%d" % (addr[0], addr[1]))

    # receive file size
    fileSize = int(client.recv(1024))
    client.send("Received")
    # receive file name
    fileName = client.recv(1024)
    client.send("Received")
    fileName = checkFileName(fileName)
    print("[==>] Saving file to %s" % fileName)
    # receive client thread count
    clientThreadCount = int(client.recv(1024))
    client.send("Received")
    for i in range(clientThreadCount):
        clientPartSocket, addrTmp = server.accept()
        filePartWriter = threading.Thread(target=writeFilePart,
                                          args=(clientThreadCount, fileName, fileSize, clientPartSocket,))
        filePartWriter.start()

    for i in range(clientThreadCount):
        sem.acquire()
    writeFile(fileName, clientThreadCount)
    print("[==>] Saved to file %s" % fileName)