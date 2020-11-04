# number = 59
# guess = int(input("Enter an integer:"))
# print("guess is:" + str(guess))
#
# if guess == number:
#     print("Bingo!you guess it right.")
#     print("(but you bo not win any prizes!")
#
# elif guess < number:
#     print("No, the number is higher than that")
#
# else:
#     print("No, the number is lower than that")
#
# print("Done")

# for i in range(1, 10):
#     print(i)
# else:
#     print("The for loop is over")

# a_list = [1, 3, 5, 7, 9]
# for i in a_list:
#     print(i)

# a_tuple = [1, 3, 5, 7, 9]
# for i in a_tuple:
#     print(i)

a_dict = {'Tom':'111', 'Jerry':'222', 'Cathy':'333'}
for ele in a_dict:
    print(ele)
    print(a_dict[ele])

for key, elem in a_dict.items():
    print(key,elem)