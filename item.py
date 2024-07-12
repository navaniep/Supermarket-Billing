class Item:
    def __init__(self, name, quantity, unit, price_per_unit=0, discount="", discount_type=""):
        self.name = name
        self.price_per_unit = price_per_unit
        self.unit = unit
        self.discount = discount
        self.discount_type = discount_type
        self.quantity = quantity
    
    def calculate_discounted_price(self, maxdiscount = 0):
        if self.discount_type == "getfree":
            return self.calculate_price()
        elif self.discount_type == "percentage":
            return self.calculate_price(maxdiscount)
            
    def calculate_price(self, maxdiscount = 0):
        if self.discount_type == "getfree":
            buy, free = map(int, self.discount.split("+"))
            return (self.quantity // (buy + free)) * buy * self.price_per_unit + (self.quantity % (buy + free)) * self.price_per_unit
        elif self.discount_type == "percentage":
            return self.quantity * self.price_per_unit * (1 - int(maxdiscount) / 100)
        
    def calculate_original_price(self):
        return self.quantity * self.price_per_unit