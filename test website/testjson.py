import json
data = '''{
  "name": "rongsheng",
  "phone": {
    "type": "intl",
    "number": "13059011616"
   },
   "email": {
     "myemail": "806786849@qq.com"
   }
}'''

info = json.loads(data)            #反序列化步骤，将序列串反序列化成统一结构
print('Name:',info["name"])
print('myemail:',info["email"]["myemail"])