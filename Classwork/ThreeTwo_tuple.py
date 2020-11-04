'''
Created on 2018年3月19日

@author: jade
'''
a_tuple = (2,)
mixed_tuple = (1, 2, ['a', 'b'])
print(a_tuple)
print(str(mixed_tuple))

mixed_tuple[2][0] = 'c'
mixed_tuple[2][1] = 'd'
print(str(mixed_tuple))
print(2 in mixed_tuple)

v = ('a', ' b', 'c')

(x, y, z) = v
print(v)
print((x, y, z))
# del a_tuple
# print(a_tuple) 
print(len((1,2,3)))
print((1,2,3) + (3,2,1))
print(4 in(1,2,3))
print(('yes!') * 4)

abcd_tuple = ('a', 'b', 'c')
print(abcd_tuple[2])
print(abcd_tuple[-3])
print(abcd_tuple[1:])
print(abcd_tuple)