class Invoice:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []
        self.total_amount = 0
        self.total_saved = 0
    
    def add_item(self, item, discounted_price, saved):
        self.items.append((item, discounted_price))
        self.total_amount += discounted_price
        self.total_saved += saved
    
    def print_invoice(self):
        print(f"Customer: {self.customer_name}")
        print("Item\t\tQty\t\tAmount")
        for item, price in self.items:
            print(f"{item.name}\t\t{item.quantity}\t\t{price}")        
        print("-" * 40)
        print(f"Total Amount\t\t\t{self.total_amount:.2f} Rs")
        print(f"You saved\t\t\t{self.total_saved:.2f} Rs")
        