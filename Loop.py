# range(100):
#         start=0,stop=99,step=1
# range(1,100):
#         start=1,stop=99,step=1
# range(1,100,2):
#         start=1,stop=99,step=2

#
# for item in range(100,0,-1):
#     print(item)


# l=[]
# for i in range(0,10):
#     value=input("enter a value: ")
#     l.append(value)
# print(l)
#


# num_list=[]
# sum=0
# for i in range(10):
#     value=int(input("enter a no: "))
#     sum+=value
# print(f"the sum is {sum}")

##Task
# mainlist=[]
# duplicatelist=[]
# oddlist=[]
# evenlist=[]
#
# for i in range(15):
#     value=int(input("enter a no: "))
#     mainlist.append(value)
#
#     if value%2==0:
#         evenlist.append(value)
#     else:
#         oddlist.append(value)
#
#     if duplicatelist.count(value)<1:
#         if mainlist.count(value)>1:
#             duplicatelist.append(value)
#
# print("mainList: ",mainlist)
# print("duplicatelist: ",duplicatelist)
# print("even list: ",evenlist)
# print("odd list: ",oddlist)


# #Task
# for i in range(1,101):
#     if i%3==0:
#         if i%5==0:
#             print("flipflop")
#         else:
#             print("flip")
#     elif i%5==0:
#         print("flop")
#     else:
#         print(i)


# #Task
# num_divisible_by_3=0
# for i in range(1,101):
#    if i%3==0:
#        num_divisible_by_3+=1
#
# print(num_divisible_by_3)


#break,continue
for i in range(1,25):
    if i%7==0:
        break
    print(i)

print("-----------------------------------------------")

for i  in range(25):
    if i%7==0:
        continue
    print(i)
