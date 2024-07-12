class Category:
    def __init__(self, name, discount):
        self.name = name
        self.discount = discount
        self.subcategories = []
        
    def add_subcategory(self, subcategory):
        self.subcategories.append(subcategory)