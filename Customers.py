from Ice_Cream import *
from List_Of_Customer import read_file_customer
from avl_tree import *

class Customer:
    
    def __init__(self, id, card = []):
        self.cart = card
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
        new_id = id
        new_cus = Customer(new_id)
        self.tree.root = self.tree.add(new_cus, self.tree.root)
    
    def update_customer_txt(self, id):
        #cap nhat cart cho customer o file txt
        cus = self.tree.find(int(id))
        new_cart = cus.data.cart
        line = ""
        for i in new_cart:
            for j in i:
                if type(j) != int:
                    line += j + ', '
                else:
                    line += str(j)
                
            line += '-'
        line = line[:-1]
        file = open('customer_information.txt', 'a')
        file.write(f"\n{id}-{line}")
        file.close()
        
    
    def show_cart(self, id):
        cus = self.tree.find(int(id))
        if cus:
            print("+----------------Your Order---------------------------------------+")
            print("|                NAME                 |    PRICE    |   QUANTITY  |")
            print("+-----------------------------------------------------------------+")
            for i in cus.data.cart:
                print(f"|  {i[0]}" + " " * (35 - len(i[0])) + "|" + f"     {i[1]}      " + "|" + f"      {i[2]}" + " "*(7 - len(str(i[2]))) +"|")
            print("+-----------------------------------------------------------------+")
    
    def total(self, id):
        cus = self.tree.find(int(id))
        cash = 0
        if cus:
            for i in cus.data.cart:
                cash += int(i[1]) * int(i[2])
        return cash
            
    def generate_invoice(self, id):
        cus = self.tree.find(int(id))
        if cus:
            
            
            cash = self.total(int(id))
            
            print("+--------------------------MIXUE ICE-CREAM------------------------+")
            print("|                                                                 |")
            print(f"|                            ID: {cus.data.id}                          |")
            print("|                                                                 |")
            print("+-----------------------------------------------------------------+")
            print("|                NAME                 |    PRICE    |   QUANTITY  |")
            print("+-----------------------------------------------------------------+")
            for i in cus.data.cart:
                print(f"|  {i[0]}" + " " * (35 - len(i[0])) + "|" + f"     {i[1]}      " + "|" + f"      {i[2]}" + " "*(7 - len(str(i[2]))) +"|")
            print("+-----------------------------------------------------------------+")
            print(f"|                                           Total:  {cash} " + " " * (13-len(str(cash))) + "|")
            print("+-----------------------------------------------------------------+")
        else:
            print("Id customer not found!!!")
            
    
    def order(self, id):
        i = Ice_Cream_Management()
        menu = i.show_menu()
        o = 'y'
        cus = self.tree.find(int(id))
        while o == 'y' or o == 'Y':
            sub_cart = self.add_to_cart()
            cus.data.cart.append(sub_cart)
            
            #[NAME, PRICE, QUANTITY]
            print()
            o = input("Continue to order(y/n)? ")
            print()
    
    def add_to_cart(self):
        i = Ice_Cream_Management()
        sub_cart = []
        order_id = int(input("Please choose your ice-cream/drink you want by id: "))
        print()
        ice_cream = i.tree.find(order_id)
        quantity = int(input("How many do you want: "))
        print()
        sub_cart.append(ice_cream.data.name)
        sub_cart.append(ice_cream.data.price)
        sub_cart.append(quantity)
        
        #[NAME, PRICE, QUANTITY]
        print(f"{ice_cream.data.name} was added to your cart.")
        return sub_cart