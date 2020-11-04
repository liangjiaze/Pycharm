# def repeat_str(s, times = 1):
#     return s * times
#
# repeated_strings_1 = repeat_str("Happy Birthday!")
# print(repeated_strings_1)
#
# repeated_strings_2 = repeat_str("Happy Birthday!" , 4)
# print(repeated_strings_2)

# def func(a, b = 4, c = 8):
#     print('a is', a, 'and b is', b, 'and c is', c)
#
# func(13,17)
# func(125,  c = 24)
# func(c = 40, a = 80)

def print_paras(fpara, *nums, **words):
    print("fpara: " + str(fpara))
    print("nums:" + str(nums))
    print("words: " + str(words))

print_paras('hello', 1,2,3,4, word = 'python', another_word = 'java')