class User:
    def __init__(self,_id,username,password):
        self._id=_id
        self.username=username
        self.password=password
    
    def login(self,uname,pw):
        #student and teacher object should be able to log in
        if self.username==uname and self.password==pw:
            print(f"Logging in {self.username}")
            return True
        else:
            print("Invalid login")
            return False

class Person(User):
    def __init__(self,_id,username,password,name,contact,address):
        super().__init__(_id,username,password)
        self.name=name
        self.contact=contact
        self.address=address

    def display_Profile(self):
        #_id,username,contact,adderss,name
        #course if person is Student
        #designation if person is Teacher
        print(f"Id: {self._id}")
        print(f"UserName: {self.username}")
        print(f"Name: {self.name}")
        print(f"Contact: {self.contact}")
        print(f"Address: {self.address}")

class Student(Person):
    def __init__(self,_id,username,password,name,contact,address,course):
        super().__init__(_id,username,password,name,contact,address)
        self.course=course
    
    def display_Profile(self):
        super().display_Profile()
        print(f"Course: {self.course}")
        print("---------------------------------------")

class Teacher(Person):
    def __init__(self,_id,username,password,name,contact,address,designation):
        super().__init__(_id,username,password,name,contact,address)
        self.designation=designation    

    def display_Profile(self):
        super().display_Profile()
        print(f"Designation: {self.designation}")  


s=Student("1","Heisenberg","aamec","amit","98137123","Ktm","python")
t=Teacher("3","Itachi","uchiha","naruto","123717321","konoha","Python teacher")

student_uname=input("enter student username: ")
student_pw=input("enter student password: ")
if s.login(student_uname,student_pw):
    s.display_Profile()

teacher_uname=input("enter teacher username: ")
teacher_pw=input("enter teacher password: ")
if t.login(teacher_uname,teacher_pw):
    t.display_Profile()


