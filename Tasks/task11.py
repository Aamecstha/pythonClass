# Task for question 8:
# # 1)Print all friends name, contact and address for user Ram.
# # 2)Find out which user have less friends
# # 3)Find out which user have most friend in common.


users=[
        {
        "name":"Ram",
        "contact":"987654321",
        "address":"Ktm",
        "friends":[
                {"name":"Shyam","contact":"98765154","address":"Ktm"},
                {"name":"Krishna","contact":"98765890","address":"Pkr"},
                {"name":"Hari","contact":"98765154","address":"Bkt"}
            ]
        },
        {
        "name":"Shyam",
        "contact":"98765154",
        "address":"Ktm",
        "friends":[
                {"name":"Ram","contact":"987654321","address":"Ktm"},
                {"name":"Krishna","contact":"98765890","address":"Pkr"},
            ]
        },
        {
        "name":"Hari",
        "contact":"98765154",
        "address":"Ktm",
        "friends":[
                {"name":"Ram","contact":"987654321","address":"Ktm"}
            ]
        }
]


ramInfos=users[0]
ramFriends=ramInfos["friends"]

shyanInfos=users[1]
shyamFriends=shyanInfos["friends"]

hariInfos=users[2]
hariFriends=hariInfos["friends"]

# task1
for i in range(len(ramFriends)):
    print(f'Name: {ramFriends[i]["name"]}')
    print(f'contact: {ramFriends[i]["contact"]}')
    print(f'Address: {ramFriends[i]["address"]}')


#task2
if len(shyamFriends)>len(ramFriends)<len(hariFriends):
    print("ram has less friends")
elif len(ramFriends)>len(shyamFriends)<len(hariFriends):
    print("shyam has less friends")
elif len(ramFriends)>len(hariFriends)<len(shyamFriends):
    print("hari has less friends")


#task3
ramFriend=[ramFriends[0]['name'],ramFriends[1]['name'],ramFriends[2]['name']]
shyamFriend=[shyamFriends[0]['name'],shyamFriends[1]['name']]
hariFriend=[hariFriends[0]['name']]
ramCommonFriends=0
shyamCommonFriends=0
hariCommonFriends=0

def findCommonFriends(userFriend,friends):
    cf=0
    for i in range(2):
        for j in range(len(userFriend)):
            if userFriend[j] in friends[i]:
                cf+=1
    return cf

ramCommonFriends=findCommonFriends(ramFriend,(shyamFriend,hariFriend))
shyamCommonFriends=findCommonFriends(shyamFriend,(ramFriend,hariFriend))
hariCommonFriends= findCommonFriends(hariFriend,(shyamFriend,ramFriend))

if shyamCommonFriends<ramCommonFriends>hariCommonFriends:
    print("Ram has most common friends")
elif ramCommonFriends<shyamCommonFriends>hariCommonFriends:
    print("Shyam has most common friends")
elif ramCommonFriends<hariCommonFriends>shyamCommonFriends:
    print("Hari has most common friends")

