class Birds:
    def fly(self):
        print("Most Birds Fly")

class penguin(Birds):
    def fly(self):      # child class have overridden the fly methord of bird
        print("Penguins can not fly penguins can swim only")


p = penguin()
p.fly()