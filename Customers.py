from Ice_Cream import *
from List_Of_Customer import read_file_customer
from avl_tree import *

class Customer:
    
    def __init__(self, id, cart):
        self.cart = cart
        self.id = id

class Customer_Management:
    
    def __init__(self):
        self.tree = Avl_Tree()
        list_customer = read_file_customer()
        for i in list_customer:
            cus_id = i
            cus_cart = list_customer[i]
            cus = Customer(cus_id, cus_cart)
            self.tree.root = self.tree.add(cus, self.tree.root)
    
    def generate_id(self):
        return '0'*(7-len(str(int(self.tree.max_value(self.tree.root).data.id) + 1))) + str(int(self.tree.max_value(self.tree.root).data.id) + 1)
    
    def insert_new_customer(self, id):
        new_cart = self.order()
        new_id = id
        new_cus = Customer(new_id, new_cart)
        self.tree.root = self.tree.add(new_cus, self.tree.root)
    
    def show_cart(self, id):
        cus = self.tree.find(int(id))
        if cus:
            print("+----------------Your Order---------------------------------------+")
            print("|                NAME                 |    PRICE    |   QUANTITY  |")
            print("+-----------------------------------------------------------------+")
            for i in cus.data.cart:
                print(f"|  {i[0]}" + " " * (35 - len(i[0])) + "|" + f"     {i[1]}      " + "|" + f"      {i[2]}" + " "*(7 - len(str(i[2]))) +"|")
            print("+-----------------------------------------------------------------+")
    
    def order(self):
        i = Ice_Cream_Management()
        menu = i.show_menu()
        cart = []
        o = 'y'
        while o == 'y' or o == 'Y':
            order_id = int(input("Please choose your ice-cream/drink you want by id: "))
            print()
            ice_cream = i.tree.find(order_id)
            quantity = int(input("How many do you want: "))
            print()
            cart.append([ice_cream.data.name, ice_cream.data.price, quantity])
            #[NAME, PRICE, QUANTITY]
            print(f"{ice_cream.data.name} was added to your cart.")
            print()
            o = input("Continue to order(y/n)? ")
            print()
        return cart