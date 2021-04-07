# 2. Take five user input, cast into integer. Print count of all the duplicate numbers.
# # a = [1, 2, 3, 4, 5] => {1:1, 2:1, 3:1, 4:1, 5:1}
# # b = [1, 2, 2, 3, 3] => {1:1, 2:2, 3:2}

l=[]
d={}
for i in range(0,5):
    l.append(int(input("enter a number: ")))

for j in range(0,5):
    if d.get(str(l[j]))==None:
        d[str(l[j])]=1
    else:
        d[str(l[j])]=d.get(str(l[j]))+1
                
print(d)