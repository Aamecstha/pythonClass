# def decorate_func(func):
#     def wrapper():
#         print("Namaste")
#         func()
#         print("hello again")
#     return wrapper
#
# @decorate_func
# def greet():
#     print("Welcome home")
#
# @decorate_func
# def greetSalaam():
#     print("Salaam rocky bhai")
#
# greetSalaam()





#example2:
def deco_func(f):
    def wrapper(num1,num2):
        if num2==0:
            return "could not divide by zero"
        else:
            return f(num1,num2)
    return wrapper

@deco_func
def division(num1,num2):
    return num1/num2

w=deco_func(division)
print(w(1,8))
print(division(1,0))
