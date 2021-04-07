# def difference(num1,num2):
#     if num1>num2:
#         diff=num1-num2
#     else:
#         diff=num2-num1
#     return diff
#
# ans=difference(5,10)
# print(ans)




def calculator(num1,num2,type):
    if type=="add":
        sum=num1+num2
        return sum
    elif type=="sub":
        sub=num1-num2
        return sub
    elif type=="prod":
        prod=num1*num2
        return prod
num1=int(input("enter a n0: "))
num2=int(input("enter a no: "))
type=input("enter type of calculation: ")

value=calculator(num1,num2,type)
print(value)
