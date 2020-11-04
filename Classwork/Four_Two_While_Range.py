# while example

# number = 59
# guess_flag = False
#
# while guess_flag == False:
#     guess = int(input("Enter an integer:"))
#     if guess == number:
#         guess_flag = True
#
#     elif guess < number:
#         print("NO,the number is higher than that, keep guessing")
#
#     else:
#         print("No,the number is a lower than that,keeping guess")
#
# print("Bingo!you guessed it right.")
# print("(but you do not win any prizes)")
# print('Done')


# for example

number = 59
num_chances = 5
print("you have only 5 chances to guess")

for i in range(1, num_chances + 1):
    print("chance " + str(i))
    guess = int(input("Enter an integer:"))
    if guess == number:
        print("Bingo! you guessed it right.")
        print("(but you do not win any prizes!")
        break

    elif guess < number:
        print("No, the number is higher than that,keeping guessing,you have " + str(num_chances - i) + " chances left")

    else:
        print("No, the number is lower than that ,keeping guess,you have " + str(num_chances - i) + " chances left")

print('Done')