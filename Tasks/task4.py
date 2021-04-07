a=[
    {"1":
        {
        "name":["Ram","Kumar","Shrestha"],
        "contact":
            {
            "home":["01-556677"],
            "office":["01-665577"]
            }
        },
        "friends":[
            {"2":
                {
                "name":["shyam","","joshi"],
                "contact":
                    {
                    "home":["01-999999"],
                    "office":[""]
                    }
                }
            }
        ]
    }
]

value1=a[0]["1"]
name=value1["name"]
contact=value1["contact"]["home"][0]
contact2=value1["contact"]["office"][0]
print(f"your name is {name[0]} {name[1]} {name[2]}")
print(f"your home contact is {contact}")
print(f"your office contact is {contact2}")

value2=a[0]["friends"][0]["2"]
friendName=value2["name"]
fcontact1=value2["contact"]["home"][0]
fcontact2=value2["contact"]["office"][0]
print(f"your friend name is {friendName[0]} {friendName[1]} {friendName[2]}")
print(f"your home contact is {fcontact1}")
print(f"your office contact is {fcontact2}")
