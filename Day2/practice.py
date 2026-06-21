# student={
#     "name":"Amir Bacha",
#     "marks":33,
#     "Grade":'A'
# }
# print(student)
# print(student["marks"])
# student["remarks"]="pass"
# print(student)
# student.pop("marks")
# print(student)
# print(student.keys())
# print(student.values())
# class Student:
#     def __init__(self,name,marks,grade):
#         self.name=name
#         self.marks=marks
#         self.grade=grade
#     def toShow(self):
#         print(self.name)
#         print(self.marks)
#         print(self.grade)
    
#     def __del__(self):
#         print("Object khattam")

        
# s1=Student("amir",44,'A')
# s1.toShow()

class BackAccount:
    def __init__(self,amount):
        self.amount=amount

    def deposit(self,rupees):
        self.amount+=rupees
    def GetAmount(self):
        return self.amount
    
file=open("demo.txt","w+")


