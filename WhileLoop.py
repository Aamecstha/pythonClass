#two types of Loop
#-bounded Loop
    #-which have fix boundary of starting and ending
#-unnbounded Loop
    #-which do not have fix boundary for starting and ending


# choice='y'
# while choice=='y':
#     num1=int(input("enter a no: "))
#     num2=int(input("enter a second no: "))
#     print(f"the sum of {num1} and {num2} is {num1+num2}")
#     choice=input("do u want to continue(y/n) ")


# value=True
# while value==True:
#     password=input("enter a password: ")
#     if password=="abc1234":
#         print("correct password")
#         value=False
#     else:
#         print("invalid password")
#         value=True
#     print("-------------------------------")
#

def doMaths(num1,num2,type):
    if type==1:
        return num1+num2
    elif type==2:
        return num1-num2
    elif type==3:
        return num1*num2
    elif type==4:
        return num1/num2

valueList=[]
continu='y'
while continu=='y':
    num1=int(input("enter a no: "))
    num2=int(input("enter a no: "))
    type=int(input("enter a type: "))
    value=doMaths(num1,num2,type)
    print(value)
    valueList.append(value)
    continu=input("do u  want to continue(y/n) ")

print(valueList)
