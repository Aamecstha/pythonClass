# 9. Find out all prime numbers between 1 to 100.
primeNumbers=[]
for i in range(1,100):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
        if count>2:
            break
    if count==2:
        primeNumbers.append(i)

print(primeNumbers)