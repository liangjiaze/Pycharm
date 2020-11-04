'''
Created on 2018年3月18日

@author: jade
'''
#This is a string
import sys

age=3
name='tom'
print('{0} was {1} years old!'.format(name, age))
print(name + ' was ' + str(age) + ' years old!')


a = 3
b = 4

c = 5.55
d = 8.32

e = complex(c, d)
f = complex(float(a), float(b))

print(type(a))
print(type(c))
print(type(e))
print(type(f))

print(a + b)
print(d / c)
print(b / a)
print(b // a)
print(b % a)
print(e)
print(e + f)
print(sys.float_info)