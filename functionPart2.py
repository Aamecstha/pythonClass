# def func(*args):
#     return args
#
# a,b=func(1,2)
# print(a)
# print(b)



# #having dictinary paramter using double *
# def dfunc(**args):
#     print(args)
#
# dfunc(name="amit",contact=9813)


# #referencing function
# def func(args):
#     print(args)
#
# f=func
# f(1)


#example of referencing
def welcome(name):
    print(f"Welcome {name}")

def namaste(name):
    print(f"Namaste {name}")

def Salaam(name):
    print(f"Salaam {name}")

def greet(f_name,name):
    f_name(name)

greet(welcome,"amit")
greet(namaste,"aaron")
greet(Salaam,"achit")
