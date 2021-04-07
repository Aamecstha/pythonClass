# 1. Make a program which takes user input and display either user input is leap year or not.
# # User input must be 4 digit integer
# # example: 2020 is leap year, 2021 is not
# Note: Program should ask for user input till user input is incorrect


userInput="correct"
while userInput=="correct":
    print("---------------------------------------------")
    try:
        print("enter 4 digit year only")
        year=int(input("enter a year: "))
        if year%4==0:
            if year%100==0:
                if year%400==0:
                    print(f"{year} is a leap year")
                else:
                    print(f"{year} is not a leap year")
            else:
                print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    except ValueError:
        userInput="incorrect"
        print("invaid input. Input must be integer")