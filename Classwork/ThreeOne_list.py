'''
Created on 2018年3月19日

@author: jade
'''
print('你好！')

print('What is your name?\nTom')

#create list
number_list = [1, 2, 3, 4]
string_list = ['apple' , 'banana' , 'car']
mixed_list = ['a' , 'b' , 3, 5.99]

# print('number_list: ' + str(number_list))
# print('string_list: ' + str(string_list))
# print('mixed_list: ' + str(mixed_list))
second_num = number_list[1]
third_string = string_list[2]
fourth_mixed = mixed_list[3]
print('second_num: {0}\nthird_string: {1}\nfourth_mixed: {2}'.format(second_num, third_string, fourth_mixed))

number_list[1] = 30
print('number_list after: '+ str(number_list))

del number_list[2]
print('number_list after del' + str(number_list))
print(len([1,2,3]))
print([1,2,3] + [3,2,1])
print(4 in[1,2,3])
print(['yes!'] * 4)

list_one = ['a', 'b', 'c']
list_one.insert(2,'g')
print(list_one[2])
print(list_one[-3])
print(list_one[1:])
print(list_one)