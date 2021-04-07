try:
    num1=int(input("enter a number: "))
    num2=int(input("enter a number: "))

    print(n)                #gives name error beacouse n i not defined
except ValueError as ver:
    print(ver)
except NameError as err:
    print(err)
else:
    print(f"the sum is: {num1+num2}")
finally:
    print("completed")

print("printing after exception")
