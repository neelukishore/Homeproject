#!/usr/bin/python

########## by using the class method and static method using decorator#########

# class Student:
#     counter = 0
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#         Student.counter = Student.counter+1
#     def msg(self):
#         print(self.name + " got " + self.marks)

#     @classmethod
#     def object_counter(cls):
#         return cls.counter

# s1 = Student("riyan",100)
# s2 = Student("neelu",200)
# print(Student.object_counter())                


class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def msg(self):
        print(self.name + " got" + self.marks,"%")

    @classmethod
    def get_per(cls,name,marks):
        return cls(name,str((int(marks)/600)*100))
    @staticmethod
    def get_age(age):
        if age<17:
            print("belongs to school")
        else:
            print("don't belongs to school")        

name = str(input(" enter the username:"))
marks = str(int(input(" enter the marks:")))
#name = "neelu"
#marks = "400"
s =Student.get_per(name,marks)
Student.get_age(18)
s.msg()




