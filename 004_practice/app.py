# #class=> multiple objects bnaayenge -> objects mein more like dynamic properties chahiyein obj1= maxMarks=10

class Animal:
    def __init__(self,arg_no_of_eyes, arg_no_of_legs, speaking_way):
        self.no_of_eyes= arg_no_of_eyes
        self.no_of_legs=arg_no_of_legs
        self.speaking_way=speaking_way

    def __len__(self):
        return 10

    def __str__(self):
        return f"Hi I have {self.no_of_eyes} eyes and I have {self.no_of_legs} legs and I speak {self.speaking_way}"

    def speak(self):
        print(self.speaking_way)

        

# # __init__() __method_name__ Double UNDERscore => DUNDER method ya MAGIC method 

# class Human(Animal):
#     def __init__(self,arg_no_of_eyes, arg_no_of_legs, speaking_way, clothes):
#         super().__init__(arg_no_of_eyes,arg_no_of_legs, speaking_way)
#         self.clothes= clothes

#     def intro(self):
#         print(f"Hi I have {self.no_of_eyes} eyes and I have {self.no_of_legs} legs and I speak {self.speaking_way}. ANd I am wearing {self.clothes}")


# dog= Animal(2,4,"bark")

# cat= Animal(2, 4,"meow")

# human= Human(2,2,"Test Speak", "Blue shirt")

# # human.speak()

# # dog.intro()
# # cat.intro()
# # human.intro()
# #str(dog)


# print(str(dog)) 


# # print(len(dog)) 
# print(dog.__len__())

# standard follow isliye self ==> rule ->  1st argument obj itself

# class School:
#     def __init__(kuch_bhi,list_of_students, list_of_teachers, list_of_rooms):
#         kuch_bhi.list_of_students= list_of_students
#         kuch_bhi.list_of_teachers= list_of_teachers
#         kuch_bhi.list_of_rooms= list_of_rooms

#     def __len__(self):
#         return len(self.list_of_rooms)

#     def __str__(self):
#         return f"I am a school consisting {len(self.list_of_students)} students, {len(self.list_of_teachers)} teachers and {len(self.list_of_rooms)} rooms"
    
#     def do_something(self):
#         print(self.list_of_students)

#     @staticmethod
#     def announce_holidays():
#         print("announce holidays")

#     @classmethod
#     def example(cls):
#         print("I am a", cls)

    
# aps= School(['aman2', 'aman'], ['teacher1', 'teacher2'], [1,2,3,101,102,103])
# dog= Animal(2,4,"bark")
# # print(aps)

# # print(len(aps))

# # aps.do_something()

# # aps.announce_holidays()


# School.do_something(aps)
# School.announce_holidays()

# aps.example()


# #Inheritence Polymorphism Class --> ToDo==> Diamond Problem in Inheritence


# class A:
#     def speak(self):
#         print("Hi I am AAAAAAAAAAAAAAAAAAAAA")

# class B:
#     def speak(self):
#         print("Hi I am BBBBBBBBBBBBBBBBBBBBBBBBBBBB")


# def some_function(some_object):
#     some_object.speak()


# a= A()
# b= B()

# some_function(a)
# some_function(b)



# class Animal():
#     @classmethod
#     def speak(cls):
#         cls.do_something()


# class A(Animal):
#     def do_something(self):
#         print("A did something")

# class B(Animal):
#     def do_something(self):
#         print("B did something")



# a= A()

# b=B()


# a.speak()
# b.speak()



class Parent:
    def speak(self):
        print("parent bolne lgaa")

class Child(Parent):
    def speak(self):
        print("Child bolne lgaa")

class Other_child(Parent):
    def run():
        pass

p= Parent()

c= Child()

o= Other_child()

p.speak()

c.speak()

o.speak()


#MRO -> method resolution order 

print(Parent.__mro__)



"""
a
|
b
|
c
|
d


d.function()




"""

class A:
    def hello():
        pass



class GrandParent:
    def dance1(self):
        print("Buddho waala dance")


class NormalParent(GrandParent):
    def run(self):
        print("Normal Dance")


class ChildClass(NormalParent, A):
    def xyz():
        pass


obj123= ChildClass()

# obj123.dance()

print(ChildClass.__mro__)

#diamond problem solved using python ==> diamond problem not an issue in python 



