y = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct',
'Nov', 'Dec']
z = ['Annie', 'Betty', 'Claire', 'Daphne', 'Ellie', 'Franchesca', 'Greta',
'Holly', 'Isabel', 'Jenny']
another_dict = {'x':'printer', 'y':5, 'z':['star', 'circle', 9]}

print("Output #129:")
for month in y:
    print("{!s}".format(month))

print("Output #130: (index value: name in list)")
for i in range(len(z)):
    print("{0!s}: {1:s}".format(i, z[i]))

print("Output #131: (access elements in y with z's index values)")
for j in range(len(z)):
    if y[j].startswith('J'):
        print("{!s}".format(y[j]))

print("Output #132:")
for key, value in another_dict.items():
    print("{0:s}, {1}".format(key, value))
my_data = [[1,2,3], [4,5,6], [7,8,9]]
kick = [row for row in my_data if row[2] > 5]
print("Output #133 (list comprehension): {}".format(kick))
my_data = [(1,2,3), (4,5,6), (7,8,9), (7,8,9)]
set_of_tuples1 = {x for x in my_data}
print("Output #134 (set comprehension): {}".format(set_of_tuples1))
set_of_tuples2 = set(my_data)
print("Output #135 (set function): {}".format(set_of_tuples2))