# def welcome(name):  #name is parameter
#     print("Welcome",name)
#
# welcome("aamec")        #aamec is argument
# welcome("ram")
# welcome("chyam")
# welcome("damn")

# def display_profile(name,number,address,country="Nepal"):       #country paramter having default value nepal if no argument in given
#     print("Name",name)
#     print("Number:",number)
#     print("Adddress:",address)
#     print("Country:",country)
#
# display_profile("amit",9123124,"ktm","America")      #positional argument
# print("-------------------------------------------------------")
# display_profile(name="ram",address="pokhara",number=98435)       #keyword argument


def sum_product(num1,num2,num3):
    sum=num1+num2+num3
    product=num1*num2*num3
    print("Sum:",sum)
    print("Product:",product)

num1=int(input("enter num1: "))
num2=int(input("enter num2: "))
num3=int(input("enter num3: "))
sum_product(num1,num2,num3)
