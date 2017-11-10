import requests

url = 'http://music.163.com/#/song/?id=468571654'

r = requests.get(url)

print(r.text)