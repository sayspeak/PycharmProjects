#!/usr/bin/env python
# coding:utf8
import datetime
import itchat
from itchat.content import *
# 申明相关的属性
def __init__(self):
    print(u'已经启动爬虫')

    # 自动回复文本等类别的群聊消息
    # isGroupChat=True表示为群聊消息
@itchat.msg_register([TEXT, SHARING], isGroupChat=True)
def group_reply_text(msg):
    # 消息来自于哪个群聊
    chatroom_id = msg['FromUserName']
    # 发送者的昵称
    username = msg['ActualNickName']
    if msg['Type'] == TEXT:
        content = msg['Content']
    elif msg['Type'] == SHARING:
        content = msg['Text']
    # 加载页面数据到数组中
    datas.append(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '---' + content + '\n')
    # 打开本地文件
    f = open('./outputweixin/' + 'test' + '.txt', 'w+', encoding='utf-8')  # 注意要有一个outputweixin的文件夹
    f.writelines(datas)
    f.close()
    print(u'爬虫报告：文件已下载到本地并打包成txt文件')

    # 自动回复图片等类别的群聊消息
@itchat.msg_register([PICTURE, ATTACHMENT, VIDEO], isGroupChat=True)
def group_reply_media(msg):
    # 如果为gif图片则不转发
    if msg['FileName'][-4:] == '.gif':
        return
    # 下载图片等文件
    msg['Text'](msg['FileName'])
    # 扫二维码登录
    itchat.auto_login(hotReload=True)
    # 获取所有通讯录中的群聊
    # 需要在微信中将需要同步的群聊都保存至通讯录
    chatrooms = itchat.get_chatrooms(update=True, contactOnly=True)
    chatroom_ids = [c['UserName'] for c in chatrooms]
    print('正在监测的群聊：', len(chatrooms), '个')
    print(' '.join([item['NickName'] for item in chatrooms]))
    datas = []
# 开始监测
itchat.run()