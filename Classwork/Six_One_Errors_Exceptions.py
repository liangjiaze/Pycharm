# while True:
#     try:
#         x = int(input("Please enter a number"))
#         break
#     except ValueError:
#         print("Not valid input, try again...")


try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error:{0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")