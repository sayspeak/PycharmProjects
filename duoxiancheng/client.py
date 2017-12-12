
import socket
import os
import sys
import math
import time
import threading


def getFileSize(file):
    file.seek(0, os.SEEK_END)
    fileLength = file.tell()
    file.seek(0, 0)
    return fileLength


def getFileName(fileFullPath):
    index = fileFullPath.rindex('\\')
    if index == -1:
        return fileFullPath
    else:
        return fileFullPath[index + 1:]


def transferFile():
    fileFullPath = r"%s" % input("File path: ").strip("\"")
    if os.path.exists(fileFullPath):
        timeStart = time.clock()
        file = open(fileFullPath, 'rb')
        fileSize = getFileSize(file)
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((targetHost, targetPort))
        # send file size
        client.send(str(fileSize))
        response = client.recv(1024)
        # send file name
        client.send(getFileName(fileFullPath))
        response = client.recv(1024)
        # send thread count
        client.send(str(threadCount))
        response = client.recv(1024)
        # send file content
        for i in range(threadCount):
            filePartSender = threading.Thread(target=transferFileSubThread, args=(fileFullPath, i + 1, fileSize))
            filePartSender.start()

        for i in range(threadCount):
            sem.acquire()
        timeEnd = time.clock()
        print("Finished, spent %f seconds" % (timeEnd - timeStart))
    else:
        print("File doesn't exist")


def transferFileSubThread(fileFullPath, threadIndex, fileSize):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((targetHost, targetPort))
        client.send(str(threadIndex))
        client.recv(1024)
        # calculate start position and end position
        filePartSize = fileSize / threadCount
        startPosition = filePartSize * (threadIndex - 1)
        # print "Thread : %d, startPosition: %d" % (threadIndex, startPosition)
        endPosition = filePartSize * threadIndex - 1
        if threadIndex == threadCount:
            endPosition = fileSize - 1
            filePartSize = fileSize - startPosition
        file = open(fileFullPath, "rb")
        file.seek(startPosition)
        sentLength = 0
        while sentLength < filePartSize:
            bufLen = 1024
            lengthLeft = filePartSize - sentLength
            if lengthLeft < 1024:
                bufLen = lengthLeft
            buf = file.read(bufLen)
            client.send(buf)
            sentLength += len(buf)
        file.close()
        sem.release()
        print("Part %d finished, size sent %d" % (threadIndex, sentLength))
    except Exception:
        print(Exception)


targetHost = input("Server IP Address: ")
targetPort = int(input("Server port: "))
threadCount = int(input("Thread count: "))
sem = threading.Semaphore(0)

while True:
    transferFile()