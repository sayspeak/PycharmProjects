empty_dict = { }
a_dict = {'one':1, 'two':2, 'three':3}
print("Output #102: {}".format(a_dict))  #输出原始字典列表
print("Output #103: a_dict has {!s} elements".format(len(a_dict)))  #输出字典长度
another_dict = {'x':'printer', 'y':5, 'z':['star', 'circle', 9]}   #字典中含有列表时输出
print("Output #104: {}".format(another_dict))
print("Output #105: another_dict also has {!s} elements"\
.format(len(another_dict)))
print("Output #106: {}".format(a_dict['two']))   #查找并输出对应键的值
print("Output #107: {}".format(another_dict['z']))   #查找'z'所对应的值
a_new_dict = a_dict.copy()                         #列表的复制
print("Output #108: {}".format(a_new_dict))
print("Output #109: {}".format(a_dict.keys()))    #.key输出字典的键
dict_copy = a_dict.copy()
ordered_dict1 = sorted(dict_copy.items(), key=lambda item: item[0])
print("Output #120 (order by keys): {}".format(ordered_dict1))    #按键的顺序排序
ordered_dict2 = sorted(dict_copy.items(), key=lambda item: item[1])
print("Output #121 (order by values): {}".format(ordered_dict2))   #按值的顺序排序
ordered_dict3 = sorted(dict_copy.items(), key=lambda x: x[1], reverse=True)
print("Output #122 (order by values, descending): {}".format(ordered_dict3))   #从大到小
ordered_dict4 = sorted(dict_copy.items(), key=lambda x: x[1], reverse=False)
print("Output #123 (order by values, ascending): {}".format(ordered_dict4))    #从小到大
a_dict_keys = a_dict.keys()
print("Output #110: {}".format(a_dict_keys))
print("Output #111: {}".format(a_dict.values()))
print("Output #112: {}".format(a_dict.items()))
if 'y' in another_dict:
	print("Output #114: y is a key in another_dict: {}."\
    .format(another_dict.keys()))                                  #如果'y'在字典中，则输出该字典的键

if 'c' not in another_dict:
	print("Output #115: c is not a key in another_dict: {}."\
    .format(another_dict.keys()))                                  #如果'c'没有在字典中，输出该字典的键（在字典中查找键值）


#获取字典中键对对应的值
print("Output #116: {!s}".format(a_dict.get('three')))
print("Output #117: {!s}".format(a_dict.get('four')))
print("Output #118: {!s}".format(a_dict.get('four', 'Not in dict')))
