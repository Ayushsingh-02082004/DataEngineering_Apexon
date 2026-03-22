
# inheritance which involves more than one type is called hybrid inheritance . 

class person:
    def info(self):
        print("This is a person.")

class Employee(person):                        #hierarichal
    def work(self):
        print("Employee Works")

class Student(person):                        #hierarichal
    def study(self):
        print("Student Studies")

                           
class Intern(Employee , Student):          #multilevel (hybrid) + multiple 
    def role(self):
        print("INtern learn and works")



i = Intern()

i.info()
i.work()
i.study()
i.role()