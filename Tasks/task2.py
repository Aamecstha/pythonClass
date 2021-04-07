# Task 2
# You have a list of your favourite marvel super heros.

# heros=['spider man','thor','hulk','iron man','captain america']

# Using this find out,

# 1. Length of the list
# 2. Add 'black panther' at the end of this list
# 3. You realize that you need to add 'black panther' after 'hulk',
#     so remove it from the list first and then add it after 'hulk'
# 4. Now you don't like thor and hulk because they get angry easily :)
#     So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#     Do that with one line of code.
# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)


#1
heros=["spider man","thor","hulk","iron man","captain america"]
print("the length of the list is {}".format(len(heros)))
print("----------------------------------------------------")


#2
heros.append("black panther")
print("Heroes list after adding black panther: ",heros)
print("----------------------------------------------------")


#3
heros.remove("black panther")
heros.insert(heros.index("hulk")+1,"black panther")
print("Heroes list after adding black panther after hulk: ",heros)
print("----------------------------------------------------")


#4
heros.remove("thor"),heros.remove("hulk"),heros.insert(1,"doctor strange")
print("Heroes list after removing hulk and thor with doctor strange: ",heros)
print("----------------------------------------------------")


#5
heros.sort()
print("Heros list after sorting in ascending orser: ",heros)
