 # OOPS => To Map with real world scenarious , we started using objects in code . this is called object oriented programminG.

# CLASS => Class is a blueprint for creating objects.

class Student:  #creating class
     name = "rajveer"
s1 = Student() # creating object(instance)
print(s1.name)

# --init--Function -(CONSTRUCTOR) => All classes have a function called --init--(),which is always being executed when the class is being initiated
class Student:
     def __init__(self ,name ,marks): # self - object ko name dena - self ek default parameter
          self.name = name
          self.marks = marks
          print("adding new student in a database")

s1 = Student("RAJVEER",97)  # constructor object
print(s1.name,s1.marks)

s2 = Student("ARJUN",95)
print(s2.name,s2.marks)

# METHODS => Methoda are function that belongs to objects.
class Student:
     def __init__(self ,name ,marks): # self - object ko name dena - self ek default parameter
          self.name = name
          self.marks = marks
          
     def welcome(self): # methods
               print("welcome student :",self.name)

     def getmarks(self):
                    return self.marks

s1 = Student("RAJVEER",97)  # constructor object
s1.welcome()
print(s1.getmarks())

# STATIC METHOD => Methods that dont use the self parameter(work at class level)
class Student:
     def __init__(self ,name ,marks): # self - object ko name dena - self ek default parameter
          self.name = name
          self.marks = marks
          
     @staticmethod
     def welcome():
               print("welcome student :", self.name)

     @staticmethod
     def getmarks():
            return self.marks

s1 = Student("RAJVEER",97)  # constructor object
s1.welcome()
print(s1.getmarks())

# ABSTRACTION => HIDING THE IMPLEMENTATION DETAILS OF A CLASS AND ONLY SHOWING THE ESSENTIAL FEATURE TO THE USER.
# ENCAPSULATION => WRAPPING DATA AND FUNCTIONS INTO A SINGLE UNIT(object).
class car:
     def __init__(self):
          self.acc = False
          self.brk = False
          self.clutch = False

     def start(self):
               self.clucth = True
               self.acc = True
               print('car satrted')
               
car1 = car()
car1.start()

# DEL KEYWORD => Used to delete object properties or object itself.
class Student:
        def __init__(self,name):
                self.name = name 

s1 = Student("roshni")
del s1

# PRIVATE ATTRIBUTE AND METHODS => Private attributes and methods are meant to be used only within the class and are not accessible from outside the class.
class Account:
       def __init__(self,accno,accpass):
               self.accno = accno
               self.__accpass = accpass # __ is used to make private we cant access the outside the class.

       def reset_pass(self):
               print(self.__accpass)

acc1 = Account("12345","abcdefg")
print(acc1.accno)
# print(acc1.__accpass) the password is private show it throws a error  . we can accesss inside other a class
print(acc1.reset_pass())

# inheritance => when one child(derived) class derives the property and methods of another class parent (base) is called inheritance.
# TYPES => 1) SINGLE INHERITANCE 2) MULTI - LEVEVL INHERITANCE 3) MULTIPLE INHERITANCE

class Car:  # single inheritance
       color = "black"
       @staticmethod
       def start():
              print("car started...")

       @staticmethod
       def stop():
              print("car is stopped..")

class ToyataCar(Car):
       def __init__(self,name):
              self.name = name

car1 = ToyataCar("fortuner")
car2 = ToyataCar("prius")

print(car1.name)
print(car1.color)
print(car1.start())

# multi - level inheritance
class Car:
       color = "black"
       @staticmethod
       def start():
              print("car started...")

       @staticmethod
       def stop():
              print("car is stopped..")

class ToyataCar(Car):
       def __init__(self,brand):
              self.brand = brand
          
class fortuner(ToyataCar):
       def __init__(self,type):
              self.type = type

car1 = fortuner("DIESEL")
car1.start()

# MULTIPE INHERITANCE
class A:
       varA = "welcome to class A"

class B:
       varB = "welcome to class B"

class C(A,B):
       varC = "welcome to class C"

c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA)

# SUPER METHOD => Super() method is used to access methods of the parent class.
class Car:
       def __init__(self,type):
              self.type = type

       @staticmethod
       def start():
              print("car started...")

       @staticmethod
       def stop():
              print("car is stopped..")

class ToyataCar(Car):
       def __init__(self,name,type):
              self.name= name
              super().__init__(type)
              super().start()
          
car1 = ToyataCar("prius","electric")
print(car1.type)
print(car1.name)

# CLASS METHOD => a class method is bound to the class & receives the class as an implicit first argument
# NOTE => Static method cant access or modify class state & generally for utility.
class Person:
       name = "anonmyous"

       @classmethod # decorator
       def changeName(cls,name):
              cls.name = name

p1 = Person()
p1.changeName("rajveer")
print(p1.name)
print(Person.name)

# PROPERTY  DECORATOR=> we use @property  decorator on any method in the class to use the method as property.
class Student:
       def __init__(self,phy,chem,math):
              self.phy = phy
              self.chem = chem
              self.math = math
              
       @property
       def percentage(self):
              return str((self.phy + self.chem + self.math)/3) + "%"


stu1 = Student(90,97,78)
print(stu1.percentage)

stu1.phy = 94
print(stu1.percentage)

# POLYMORPHISM (Operator overloading) => When the same operator is allowed to have different meaning according to context.
# Operator And Dunder functions
# 1) a+b  addition  a.__add__(b)
# 2) a-b  addition  a.__sub__(b)
# 3) a*b  addition  a.__mul__(b)
# 4) a/b  addition  a.__truediv__(b)
# 5) a%b  addition  a.__mod__(b)

class Complex:
       def __init__(self, real ,img):
              self.real = real
              self.img = img

       def showNumber(self):
              print(self.real ,"i +",self.img,"j")

       def __add__(self ,num2): # __a__ polymorphism
              newReal = self.real + num2.real
              newImg = self.img + num2.img
              return Complex(newReal , newImg)

num1 = Complex(1,3)
num1.showNumber()
num2 = Complex(6,4)
num2.showNumber()
num3 = num1 + num2
num3.showNumber()