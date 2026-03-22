class point:
    def __init__(self , x , y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x} , {self.y}"
    
    def __add__(self , other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return point(new_x , new_y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __sub__(self, other):
        subx = self.x - other.x
        suby = self.y - other.y
        return point(subx , suby)
    
    def __lt__(self , other):
        return {self.x + self.y} < {other.x + other.y}
    
    def __gt__(self, other):
        return {self.x + self.y} > {other.x + other.y}
    


p1 = point(2,3)
p2 = point(5,8)
p4 = point(9, 22)
    
p5 = p1 + p2
print(f"sum of {p1} and {p2} is :  {p5}")

p6 = p4-p1
print(f"sub of {p1} from {p4} is :  {p6}")

print(p4 > p1)



