#!/usr/bin/python

####### using property decorators #######

# class Student:
#     def __init__(self,name,grade):
#         self.name = name
#         self.grade = grade

#     def msg(self):    
#         return self.name + " got grade" + self.grade

# stud1 = Student("riyan","A")
# stud1.grade = "B"
# print("name:",stud1.name)
# print("grade:",stud1.grade)
# print(stud1.msg())        


# class Student:
#     def __init__(self,name,grade):
#         self.name = name
#         self.grade = grade
    
#     @property
#     def msg(self):
#         return self.name + " got grade"  +  self.grade
#     @msg.setter
#     def msg(self,msg):
#         sent = msg.split(" ")
#         print(sent)
#         self.name = sent[0]
#         self.grade = sent[-1] 

# stud1 = Student("riyan","A")
# stud1.msg = "riyan got grade B"
# print("name:",stud1.name)
# print("grade:",stud1.grade)
# print(stud1.msg)            




# class Student:
#     def __init__(self,marks):
#         self.__marks = marks
#     def per(self):
#         return (self.__marks/600)*100
#     @property
#     def marks(self):
#         print("getting the value:",end=" ")
#         return self.__marks
#     @marks.setter
#     def marks(self,value):
        
#         if value<0 or value>600:
#             print("to print the previous value")
#         else:
#             print("setting the value:",value)     
#             self.__marks = value


# s = Student(400)
# s.marks = 601
# print(s.marks)
# print(s.per(),"%")            



class Student:
    def __init__(self,marks):
        self.__marks = marks
    def per(self):
        return (self.__marks/600)*100
    def getter(self):
        print("getting the value:",end=" ")
        return self.__marks
    def setter(self,value):
        if value>0 or value<600:
            print("to print the previous value")
        else:
            print("setting the value:",value)
            self.__marks = value
    marks = property(getter,setter)        

s =Student(400)
s.marks = 500
print(s.marks)
print(s.per(),"%")

        


        