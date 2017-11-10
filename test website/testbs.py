import urllib.request
import re
from bs4 import *

url = input('Enter an URL\n')

html = urllib.request.urlopen(url).read()   #读取网页，放回一系列字符串，是整个页面，包括网页上的所有内容，并且并成一行
soup = BeautifulSoup(html)                 #将HTML放进beautifulsoup，读取并了解HTML，放回到soup

tags = soup('a')                      #查找在soup对象中所有链接标签，全部返回到tags（标签列表）

for tag in tags:
    x = tag.get('href',None)
    for y in x:
        if re.search('^http:',x):
            print(y)
#在文档中循环找出所有的链接标签，并且给出所有标签的href值，缺省值为NONE