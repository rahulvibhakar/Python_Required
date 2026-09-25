#Polymorphism is same method with different behavior or one interface with many forms.
class Dog:
    def sound(self):
        print("Bark!!")
class Cat:
    def sound(self):
        print("Meow!!")
Animals=[Dog(),Cat()]
for Animal in Animals:
    Animal.sound()