# def main():
#     def inner_func():
#         print("i am inner function")
#
#     def outer_func():
#         print("i am outer function")
#
#     return inner_func,outer_func
#
# print(main())
# inf,onf=main()
# inf()
# onf()




# def main(n):
#     def add(a,b):
#         return a+b
#     def sub(a,b):
#         return a-b
#
#     if n==1:
#         return add
#     elif n==2:
#         return sub
#
# type=int(input("enter a type: "))
# ref=main(type)
# num1=int(input("enter a no: "))
# num2=int(input("enter a no: "))
# print(ref(num1,num2))



##Immutable obj example
# num=10
#
# def main_func():
#     global num              #using gloabl keyword to link num to the global variable otherwise it would reference to local variable
#     num=num+1
#     print(num)
#
# main_func()
#



# #mutable obj example
# alist=[1,2]
#
# def main():
#     alist.append(5)
#
# print(alist)# main()
# print(alist)



num=5
def main():
    num=10
    def inner_func():
        nonlocal num                #using nonlocal keyword to reference to parenet fucntion variable
        num=num+1
        print(num)
    inner_func()

main()
