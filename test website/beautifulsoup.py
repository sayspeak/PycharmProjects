import urllib.request
fhand = urllib.request.urlopen('http://www.baidu.com/robots.txt')
for line in fhand:
    print(line.strip())