# 10. Take 15 user input as integer and print sum of all even numbers and odd numbers separately
evenSum=0
oddSum=0
for i in range(15):
    num=int(input("enter a number: "))
    if num%2==0:
        evenSum+=num
    else:
        oddSum+=num

print(f"the sum of even numbers is {evenSum}")
print(f"the sum of odd numbers is {oddSum}")