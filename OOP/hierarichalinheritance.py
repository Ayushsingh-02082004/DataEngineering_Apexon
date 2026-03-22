
#👉 When one parent class is inherited by multiple child classes - - hierarichal inheritance

class Electronics:
    def chips(self):
        print("Electronics devices is made up of electornic chips.")

class MobilePhone(Electronics):
    def call(self):
        print("Mobiles is electronic and can make call")

class Television(Electronics):
    def showmovie(self):
        print("Televisions are electronic and can show us movies.")



m = MobilePhone()
t = Television()

m.chips()
m.call()

t.chips()
t.showmovie()