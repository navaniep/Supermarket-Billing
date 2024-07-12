from category import Category
from subcategory import Subcategory
from item import Item
from invoice import Invoice


class Supermarket:
    def __init__(self):
        self.categories = []
    def run(self):
        produce = Category("Produce", 10)
        
        fruits = Subcategory("Fruits", 18)
        veg = Subcategory("Veg", 5)
        
        apple = Item("Apple", 0, "Kg", 50, "3+1", "getfree")
        orange = Item("Orange", 0, "Kg", 80, "20", "percentage")
        potato = Item("Potato", 0, "Kg", 30, "5+2", "getfree")
        tomato = Item("Tomato", 0, "Kg", 70, "10", "percentage")
        
        fruits.add_item(apple)
        fruits.add_item(orange)
        
        veg.add_item(potato)
        veg.add_item(tomato)
        
        produce.add_subcategory(fruits)
        produce.add_subcategory(veg)
        
        self.categories.append(produce)
        
        dairy = Category("Dairy", 15)
        
        milk = Subcategory("Milk", 20)
        cheese = Subcategory("Cheese", 20)
        
        cow_milk = Item("Cow Milk", 0, "Lt", 50, "3+1", "getfree")
        soy_milk = Item("Soy Milk", 0, "Lt", 40, "10", "percentage")
        cheddar = Item("Cheddar", 0, "Kg", 50, "2+1", "getfree")
        gouda = Item("Gouda", 0, "Kg", 80, "10", "percentage")
        
        milk.add_item(cow_milk)
        milk.add_item(soy_milk)
        
        cheese.add_item(cheddar)
        cheese.add_item(gouda)
        
        dairy.add_subcategory(milk)
        dairy.add_subcategory(cheese)
        
        self.categories.append(dairy)
    
    def query_item(self, item_name):
        for category in self.categories:
            for subcategory in category.subcategories:
                for item in subcategory.items:
                    if item.name == item_name:
                        return item, subcategory, category
        
    def generate_invoice(self, customer_name, items):
        invoice = Invoice(customer_name)
        
        for item in items:
            db_item, subcategory, category = self.query_item(item.name)
            if db_item:
                item.price_per_unit = db_item.price_per_unit
                item.discount = db_item.discount
                item.discount_type = db_item.discount_type
                max_discount = max(int(item.discount), subcategory.discount, category.discount) if item.discount_type == "percentage" else 0
                discounted_price = item.calculate_discounted_price(max_discount)
                original_price = item.calculate_original_price()
                saved = original_price - discounted_price
                
                invoice.add_item(item, discounted_price, saved)
                
        return invoice