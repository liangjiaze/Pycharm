'''
Created on 2018年4月2日

@author: jade
'''
phone_book = {'tom':123, 'jerry':456, 'kim':789}
mixed_dict = {"tom":'boy', 11:23.5}

print("tom has phone number:" + str(phone_book['tom']))

phone_book['tom'] = 999
print("tom has phone number:" + str(phone_book['tom']))

phone_book['heath'] = 888
print("the phone_book is:" +str(phone_book))

del phone_book['tom']
print("the phone_book after del is:" +str(phone_book))

phone_book.clear()
print("the phone_book after clear is:" +str(phone_book))

del phone_book
# print("the phone_book after delall is:" +str(phone_book))

list_dict = {('name'):'john', 'age':13}
# list_dict = {['name']:'john', 'age':13}

rep_test = {'name':'aa', "age":17, "name":'bb'}
print("rep_test:" + str(rep_test))