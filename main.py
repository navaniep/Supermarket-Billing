from supermarket import Supermarket
from item import Item


def main():
    supermarket = Supermarket()
    supermarket.run()
    
    customer_name = input("Enter customer name: ")
    number_of_items = int(input("Enter number of items: "))
    items = []
    for i in range(number_of_items):
        item_name = input("Enter item name: ")
        item_quantity, unit = input("Enter item quantity: ").split(" ")
        items.append(Item(item_name, int(item_quantity), unit))
    
    invoice = supermarket.generate_invoice(customer_name, items)
    invoice.print_invoice()
    
if __name__ == '__main__':
    main()