# Task 3
# Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function

max_no=int(input("enter the max number: "))

def find_odd_numbers(max_no):
    odd_no_list=[]
    for i in range(1,max_no):
        if i%2!=0:
            odd_no_list.append(i)
    return odd_no_list

print("The odd numbers are: ",find_odd_numbers(max_no))
