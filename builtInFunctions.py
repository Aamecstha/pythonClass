# a= lambda x1,x2,x3:x1+x2+x3
# print(a(5,2,7))
#
# b=lambda a,c:a+c
# print(b(5,8))





# #example2
# #map(fucntion,iterable_obj)
#
# a=[2,3,4,5,6,7,9]
# #def increase_by_one(n):
#     #return n=n+1
#
# b=map(lambda n:n+1,a)
# b=list(b)
# print(b)




# #task1
# namelist=["ram","shyam","hari","geeta","harry"]
#
# result=map(lambda n:n.capitalize(),namelist)
# result=list(result)
# print(result)



# #task2
# email_list=["i-gmail.com","2-gmail.com","3-gmail.com","4-gmail.com"]
# mail_list=list(map(lambda email:email.replace("-","@"),email_list))
# print(mail_list)





# #filer(func,iiterable_obj)
# a=[1,2,3,4,5,6,7,8,9,10]
# even=filter(lambda n:n%2==0,a)
# print(list(even))





#task3
email_list=["i@gmail.com","2@gmail.com","3@gmail.com","4@hotmail.com","5@yahoo.com","6@gmail.com","7@yahoo.com"]

glist=filter(lambda email:email.find("gmail")!=None,email_list)
print(list(glist))
