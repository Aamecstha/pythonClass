# 3. Write a program to calculate simple interest. Take principal, time and rate as user input.
# 4. Write a program to calculate Compound Interest and Compound Amount. Take principal, time 
# and rate as user input.


#task3
principal=int(input("enter principal amount: "))
time=int(input("enter time : "))
rate=int(input("enter rate percent: "))
simple_interest=(principal*time*rate)//100
print(f"the simple interest is {simple_interest}")


#task4
compound_interest=principal*(1+rate//12)**(12*time)
print(f"the compund interest is {compound_interest}")