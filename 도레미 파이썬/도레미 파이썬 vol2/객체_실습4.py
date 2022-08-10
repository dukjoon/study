class Animal():
    legs = 0
    def walk(self):
        return ""

class Dog(Animal):
    legs = 4
    def walk(self):
        return "살랑살랑"

class Human(Animal):
    legs = 2
    def walk(self):
        return "뚜벅뚜벅"

maltese = Dog()
gildong = Human()
