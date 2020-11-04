# number = 59
#
# while True:
#     guess = int(input("Enter an integer:"))
#     if guess == number:
#         break
#
#     if guess < number:
#         print("NO,the number is higher than that, keep guessing")
#         continue
#
#     else:
#         print("No,the number is a lower than that,keeping guess")
#         continue
#
# print("Bingo!you guessed it right.")
# print("(but you do not win any prizes)")
# print('Done')


a_list = [0, 1, 2]

print("using continue:")
for i in a_list:
    if not i:
        continue
    print(i)

print("using pass")
for i in a_list:
    if not i:
        pass
    print(i)