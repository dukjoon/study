class Car:
    type = "자동차"
        
class Hyundai(Car):
    pass
        
sonata = Hyundai()
print(sonata.type) #자동차

class Pet:
    attr = "cute"
    def cry(self):
        return "멍멍!"

class Dog(Pet):
    pass

maltese = Dog()