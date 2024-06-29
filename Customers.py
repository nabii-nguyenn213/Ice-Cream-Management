from Ice_Cream import *
from List_Of_Customer import read_file

class Customer:
    
    def __init__(self, id, cart):
        self.cart = cart
        self.id = id

class Node:
    
    def __init__(self, data : Customer):
        self.data = data
        self.left = None
        self.right = None

class Customer_Management:
    
    def __init__(self):
        self.root = None
        list_customer = read_file()
        for i in list_customer:
            cus_id = i
            cus_cart = list_customer[i]
            cus = Customer(cus_id, cus_cart)
            self.root = self.insert_customer(cus, self.root)
                
    def insert_customer(self, customer : Customer, root : Node):
        if root == None:
            root = Node(customer)
        else:
            if int(root.data.id) > int(customer.id):
                root.left = self.insert_customer(customer, root.left)
            
            elif int(root.data.id) < int(customer.id):
                root.right = self.insert_customer(customer, root.right)
            
            else:
                return root
        
        balance = self.get_balance(root)
        if balance > 1:
            #LECH TRAI
            if int(customer.id) < int(root.left.data.id):
                #LECH TRAI TRAI
                root = self.rotate_right(root)
            else:
                #LECH TRAI PHAI
                root.left = self.rotate_left(root.left)
                root = self.rotate_right(root)
        elif balance < -1:
            #LECH PHAI
            if int(customer.id) > int(root.right.data.id):
                #LECH PHAI PHAI
                root = self.rotate_left(root)
            else:
                #LECH PHAI TRAI
                root.right = self.rotate_right(root.right)
                root = self.rotate_left(root)
        
        return root
    
    def max_value_node(self, node):
        cur = node
        while cur.right:
            cur = cur.right
        return cur
    
    def generate_id(self):
        return '0'*(7-len(str(int(self.max_value_node(self.root).data.id) + 1))) + str(int(self.max_value_node(self.root).data.id) + 1)
    
    def insert_new_customer(self, id):
        new_cart = self.order()
        new_id = id
        new_cus = Customer(new_id, new_cart)
        self.root = self.insert_customer(new_cus, self.root)
    
    def get_balance(self, root : Node):
        return self.update_height(root.left) - self.update_height(root.right)

    def update_height(self, root : Node):
        if root is None:
            return -1
        return max(self.update_height(root.left), self.update_height(root.right)) + 1
    
    def rotate_left(self, root : Node):
        temp = root.right
        root.right = temp.left
        temp.left = root
        
        return temp
    
    def rotate_right(self, root : Node):
        temp = root.left
        root.left = temp.right
        temp.right = root
        
        return temp
    
    def bfs(self):
        q = Queue()
        q.put(self.root)
        while not q.empty():
            current = q.get()
            print(current.data.id, end = " ")
            if current.left:
                q.put(current.left)
            if current.right:
                q.put(current.right)
    
    def find(self, id : int):
        cur = self.root
        while cur and int(cur.data.id) != id:
            if int(cur.data.id) < id:
                cur = cur.right
            elif int(cur.data.id) > id:
                cur = cur.left
        if cur:
            return cur
        else:
            print("PLEASE ORDER FIRST")
            return 
    
    def show_cart(self, id):
        cus = self.find(int(id))
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
            ice_cream = i.find(order_id)
            quantity = int(input("How many do you want: "))
            print()
            cart.append([ice_cream.data.name, ice_cream.data.price, quantity])
            #[NAME, PRICE, QUANTITY]
            print(f"{ice_cream.data.name} was added to your cart.")
            print()
            o = input("Continue to order(y/n)? ")
            print()
        return cart