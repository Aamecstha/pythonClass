# 6. Suppose, we have given list:
# a = [
# {“username”: “ram@gmail.com”, “last_login”: “157950”},
# {“username”: “ shyam @gmail.com”, “last_login”: “157659”},
# {“username”: “hari@gmail.com”, “last_login”: “157680”},
# {“username”: “krishna@gmail.com”, “last_login”: “157880”}
# ]
# # Sort the above given list according to their last_login in ascending order.

a = [
{'username': 'ram@gmail.com', 'last_login': '157950'},
{'username': 'shyam @gmail.com', 'last_login': '157659'},
{'username': 'hari@gmail.com', 'last_login': '157680'},
{'username': 'krishna@gmail.com', 'last_login': '157880'}
]

for i in range(4):
    if i>0:
        for j in range(i):
            if int(a[i]["last_login"])>int(a[j]["last_login"]):
                a.insert(j,a.pop(i))

print(a)

