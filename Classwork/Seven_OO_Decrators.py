# class Student:
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade
#
#     def introduce(self):
#         print("Hi! I'm " + self.name)
#         print("my grade is: " + str(self.grade))
#
#     def improve(self, amount):
#         self.grade = self.grade + amount
#
#     def update(self, grade):
#         self.grade = grade
#
# jim = Student("jim", 86)
# jim.introduce()
#
# jim.improve(10)
# jim.introduce()
#
# jim.update(99)
# jim.introduce()


# def add_candles(cake_func):
#     def insert_candles():
#         return cake_func + " candles"
#     return insert_candles
#
# def make_cake():
#     return "cake"
#
# gift_func = add_candles(make_cake())
#
# print(make_cake())
# print(gift_func())


# def add_candles(cake_func):
# #     def insert_candles():
# #         return cake_func + " candles"
# #     return insert_candles
# #
# # def make_cake():
# #     return "cake"
# #
# # make_cake = add_candles(make_cake())
# #
# # print(make_cake())


def add_candles(cake_func):
    def insert_candles():
        return cake_func() + " and candles"
    return insert_candles

@add_candles
def make_cake():
    return "cake"

print(make_cake())