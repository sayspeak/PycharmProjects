import requests
import json
import re

def download_by_music_id(music_id):
    lrc_url = 'http://music.163.com/api/song/lyric?' + 'id=' + str(music_id) + '&lv=1&kv=1&tv=-1'

    r = requests.get(lrc_url)
    json_obj = r.text

    j = json.loads(json_obj)

    lrc = j['lrc']['lyric']
    pat = re.compile(r'\[.*\]')
    lrc = re.sub(pat, "", lrc)
    lrc = lrc.strip()
    return lrc
music_id = input('enter the id of a song ')
words = download_by_music_id(music_id)
print(words)