import requests
import json
import re
# 找入口，从哪里抓取数据
def download_by_music_id(music_id):
    # http://music.163.com/weapi/song/lyric?csrf_token=
    lrc_url = 'http://music.163.com/api/song/lyric?' + 'id=' + str(music_id) + '&lv=1&kv=1&tv=-1'  #跨过验证

    r = requests.get(lrc_url)
    json_obj = r.text
    print(json_obj)

    j = json.loads(json_obj)     #反序列json_obj

    lrc = j['lrc']['lyric']
    pat = re.compile(r'\[.*\]')   #正则匹配找出【】之间的时间
    lrc = re.sub(pat, " ", lrc)
    lrc = lrc.strip()            #将正则表达式找出的内容进行删除
    return lrc
music_id = input('enter the id of a song\n')
words = download_by_music_id(music_id)
print(words)