'''
Created on 2018年4月8日

@author: jade
'''
def say_hi():
    print('hi!')
    
say_hi()


def print_sum_two(a, b):
    c = a + b
    print(c)
    
print_sum_two(3, 2)


def hello_some(str):
    print('hello ' + str + '!')

hello_some('china')


def repeat_str(str,times):
    repeated_strs = str * times
    return repeated_strs

repeated_strings = repeat_str('hello!', 3)
print(repeated_strings)


x = 60
 
def foo(x):
    print('x is ' +str(x))
    x = 3
    print('change local x to ' +str(x))
     
foo(x)
print('x is still ' + str(x))


x = 60
 
def fooo():
    global x
    print('x is ' +str(x))
    x = 3
    print('change local x to ' +str(x))
     
fooo()
print('value of x is ' + str(x))


