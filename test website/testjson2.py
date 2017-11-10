import json
input = '''
[
  {"id": "007",
   "x" : "2",
   "name": "rongsheng"
  },
  {"id": "001",
   "x": "4",
   "name": "ssss"
  }
]'''
another_info = json.loads(input)
print('count',len(another_info))
for items in another_info:
    print('Name',items['name'])
    print('id',items['id'])