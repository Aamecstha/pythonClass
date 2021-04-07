# 5. Print the sum of given lists:
# a) [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# b) [1, 2, ‘3’, 4, 5, ‘6’, 7, 8, 9, 10]
# Note: Both lists should have same sum


a=[1,2,3,4,5,6,7,8,9,10]
b=[1,2,'3',4,5,'6',7,8,9,10]
sumA=0
sumB=0
for i in range(len(a)):
    sumA+=a[i]
print(f"the sum of list a is: {sumA}")

for j in range(len(b)):
    if type(b[j])==str:
        sumB+=int(b[j])
    else:
        sumB+=b[j]

print(f"the sum of list b is: {sumB}")