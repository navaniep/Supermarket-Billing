class Subcategory:
    def __init__(self, name, discount):
        self.name = name
        self.discount = discount
        self.items = []

    def add_item(self, item):
        self.items.append(item)