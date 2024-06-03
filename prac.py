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