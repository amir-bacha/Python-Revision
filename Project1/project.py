 # Student Management system


  #Student class
class Student:
    Students=[]
    def __init__(self,rollNum,name,cnic,CGPA):
        self.rollNum=rollNum
        self.name=name
        self.cnic=cnic
        self.CGPA=CGPA
    def ShowStud(self):
        print("============================")
        print("Roll NO = ",self.rollNum)
        print("name = ",self.name)
        print("CNIC   = ",self.cnic)
        print("CGPA = ",self.CGPA)
        print("============================")


class StudentManagement:
         
        def __init__(self):
            self.students=[]


        #Adding student function
        def Add(self):
            rollNum=int(input("Enter student rollNum : "))
            name=input("Enter student name : ")
            cnic=int(input("Enter student cnic : "))
            CGPA=int(input("Enter student CGPA"))
            student=Student(rollNum,name,cnic,CGPA)
            self.students.append(student)
             
        def ShowStudent(self):
             for student in self.students:
                student.ShowStud()

                # object 
system=StudentManagement()
while True:
     
    print(" -----Welcome to Student Management System---")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Exits : ")
    option=int(input("Enter your choice : "))
    if option==1:
        system.Add()
    elif option==2:
        system.ShowStudent()

    elif option==3:
        break

    else:
        print("Invalid credintional")
