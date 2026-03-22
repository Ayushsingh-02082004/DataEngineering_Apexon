
class product:
    def __init__(self , name , price ):
        self.name = name
        self.price = price


    def __repr__(self):
        return f"{self.name} : {self.price}"
    

class shoppingkart:
    def __init__(self , customername):
        self.customer = customername
        self.__items = []

    def add_item(self , product , quantity = 1):
        for _ in range(quantity):
            self.__items.append(product)
        print(f"Added {quantity} x {product.name} to {self.customer}'s cart.")


    def remove_item(self , product_name):
        original_count = len(self.__items)
        self.__items = [item for item in self.__items if item.name != product_name]
        if len(self.__items) < original_count:
            print(f"REmoved all {product_name} from cart.")


    def calculate_total(self):
        total = sum(item.price for item in self.__items)
        return total
    

    def __len__(self):
        """Dunder emthod to use len(cart)"""
        return len(self.__items)
    

    def __str__(self):
        """User-friendly view of the cart"""
        return f"Cart({self.customer}): {len(self.__items)} itmes , Total: ${self.calculate_total()}"
    


# --- using the oop system --------------

#1. Create Products

p1 = product("Laptop" , 1200)
p2 = product("Mouse" , 25)
p3 = product("Keyboard" , 45)


mycart = shoppingkart("Yushi")

mycart.add_item(p1)
mycart.add_item(p2 , 2)

print(mycart)

print(f"Items in cart : {len(mycart)}")
print(f"Total Bill : ${mycart.calculate_total()}")

mycart.remove_item("Mouse")
print(f"Final Total : ${mycart.calculate_total()}")