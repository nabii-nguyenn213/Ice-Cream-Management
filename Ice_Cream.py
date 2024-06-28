from List_Of_IceCream import *
from queue import Queue

class IceCream:
    def __init__(self,id,  name, price, quantity = 1, topping = None):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.topping = topping

class Node:
    
    def __init__(self, data : IceCream):
        self.data = data
        self.left = None
        self.right = None

class Management:
    def __init__(self):
        self.root = None
        list_ice_cream = read_file()
        for i in list_ice_cream:
            icecream_id = i
            icecream_name = list_ice_cream[i][0]
            icecream_price = list_ice_cream[i][1]
            icecream = IceCream(icecream_id, icecream_name, icecream_price)
            self.root = self.add_ice_cream(icecream, self.root)
    
    def add_ice_cream(self, ice_cream : IceCream, root : Node):
        if root == None:
            root = Node(ice_cream)
        else:
            if int(root.data.id) > int(ice_cream.id):
                root.left = self.add_ice_cream(ice_cream, root.left)
            elif int(root.data.id) < int(ice_cream.id):
                root.right = self.add_ice_cream(ice_cream, root.right)
            else:
                return root
        
        balance = self.get_balance(root)
        if balance > 1:
            #LECH TRAI
            if int(ice_cream.id) < int(root.left.data.id):
                #LECH TRAI TRAI
                root = self.rotate_right(root)
            else:
                #LECH TRAI PHAI
                root.left = self.rotate_left(root.left)
                root = self.rotate_right(root)
        elif balance < -1:
            #LECH PHAI
            if int(ice_cream.id) > int(root.right.data.id):
                #LECH PHAI PHAI
                root = self.rotate_left(root)
            else:
                #LECH PHAI TRAI
                root.right = self.rotate_right(root.right)
                root = self.rotate_left(root)
        
        return root
    
    def add_new_ice_cream(self):
        new_icecream_id = input("Please enter ice-cream id: ")
        new_icecream_name = input("Please enter ice-cream name: ")
        new_icecream_price = input("Please enter ice-cream price: ")
        icecream = IceCream(new_icecream_id, new_icecream_name, new_icecream_price)
        self.root = self.add_ice_cream(icecream, self.root)
    
    def get_balance(self, root : Node):
        return self.height(root.left) - self.height(root.right)
    
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
    
    def height(self, root : Node):
        if root is None:
            return -1
        return max(self.height(root.left), self.height(root.right)) + 1
    
    def delete_ice_cream(self, ice_cream : IceCream):
        pass
    
    def find(self, id : int):
        cur = self.root
        while cur and int(cur.data.id) != id:
            if int(cur.data.id)  < id:
                cur = cur.right
            elif int(cur.data.id) > id:
                cur = cur.left
        if cur:
            return cur
        else:
            print("Ice-cream id not found!!!")
            return 
    
    def modify_ice_cream(self):
        self.show_menu()
        print()
        ice_cream_id = int(input("Please enter ice-cream id you want to modify: "))
        ice_cream = self.find(ice_cream_id)
        if ice_cream:
            print("Current Name:", ice_cream.data.name)
            change = input("Do you want to modify (y/n)? ")
            if change == 'y' or change == "Y":
                ice_cream.data.name = input("Please enter a new name: ")
            
            print("Current Price:", ice_cream.data.price)
            change = input("Do you want to modify (y/n)? ")
            if change == 'y' or change == "Y":
                ice_cream.data.price = input("Please enter a new price: ")
    
    def show_menu(self):
        print("+-----------------------Ice Cream Menu-----------------------+")
        print("|   ID   |                NAME                 |    PRICE    |")
        print("+------------------------------------------------------------+")
        ice_cream = read_file()
        for i in ice_cream:
            print(f"|   {i}   |  {ice_cream[i][0]}" + " " * (35-len(ice_cream[i][0])) + "|" + f"      {ice_cream[i][1]}     |")
        print("+------------------------------------------------------------+")
        
    
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

if __name__ == "__main__":
    management = Management()
    management.show_menu()
    management.bfs()