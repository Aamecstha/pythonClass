# num=int(input("enter any no: "))
# if num>0:
#     print("this is positive number")
# else:
#     print("this is negative number")



#even or odd
# num=int(input("enter any number: "))
# value=num%2
# if value==0:
#     print("it is even")
# else:
#     print("it is odd")

# num=int(input("enter a number: "))
#
# if num%3==0:
#     print("it is divided by 3")
# elif num%5==0:
#         print("it is divided by 5")
# elif num%7==0:
#         print("it is divided by 7")


num1=int(input("enter first no: "))
num2=int(input("enter second no: "))
num3=int(input("enter a third no: "))
greater=0
if num1>num2:
    greater=num1
else:
    greater=num2

if greater>num3:
    print(str(greater)+" is greatest")
else:
    print(str(num3)+" is greatest")
