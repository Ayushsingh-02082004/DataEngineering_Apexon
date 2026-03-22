class Dog:
    def speak(self):
        return "Woof!"
    
class Cat:
    def speak(self):
        return "Meow!"
    
class Duck:
    def speak(self):
        return "Quack!"
    

    #--- The Polymorphic Function ---

def animal_sound(animal):

        #This funciton doesn't care if animal is Dog , cat , or Duck.
        #It just cares that the object HAS  a spesk() method.
        print(animal.speak())

    
my_dog = Dog()
my_cat = Cat()
duck = Duck()

animal_sound(my_dog)
animal_sound(my_cat)
animal_sound(duck)