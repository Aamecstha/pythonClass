#writing in file
f=open("test.txt",'w')
f.write("Ram: whats up keds!!!")
f.close()



#appending in file
f=open("test.txt","a")
f.write("\nShyam: i am fine thank you ser")
f.close()



#reading whole file
f=open("test.txt","r")
print(f.read())
f.close()

#reading line by line
f=open("test.txt","r")
print(f.readline())
f.close()

#reading all lines and returing in lsit
f=open("test.txt","r")
print(f.readlines())
f.close()
