import os
from queue import Queue
from List_Of_Customer import read_file_customer
from List_Of_IceCream import read_file_ice_cream

class IceCream:
    def __init__(self,id, name, price):
        self.id = id
        self.name = name
        self.price = price

class Node:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Avl_Tree:
    
    def __init__(self):
        self.root = None
    
    def add(self, element, root):
        if root == None:
            root = Node(element)
        else:
            if int(root.data.id) > int(element.id):
                root.left = self.add(element, root.left)
            elif int(root.data.id) < int(element.id):
                root.right = self.add(element, root.right)
            else:
                return root
        
        balance = self.get_balance(root)
        if balance > 1:
            #LECH TRAI
            if int(element.id) < int(root.left.data.id):
                #LECH TRAI TRAI
                root = self.rotate_right(root)
            else:
                #LECH TRAI PHAI
                root.left = self.rotate_left(root.left)
                root = self.rotate_right(root)
        elif balance < -1:
            #LECH PHAI
            if int(element.id) > int(root.right.data.id):
                #LECH PHAI PHAI
                root = self.rotate_left(root)
            else:
                #LECH PHAI TRAI
                root.right = self.rotate_right(root.right)
                root = self.rotate_left(root)
        
        return root
    
    def get_balance(self, root):
        if root is None:
            return 0
        return self.update_height(root.left) - self.update_height(root.right)
    
    def rotate_right(self, root : Node):
        temp = root.left
        root.left = temp.right
        temp.right = root
        return temp
    
    def rotate_left(self, root : Node):
        temp = root.right
        root.right = temp.left
        temp.left = root
        return temp
    
    def update_height(self, root):
        if root is None:
            return -1
        return max(self.update_height(root.left), self.update_height(root.right)) + 1

    def max_value(self, node):
        cur = node
        while cur.right:
            cur = cur.right
        return cur
    
    def min_value_node(self, node):
        cur = node
        while cur.left:
            cur = cur.left
        return cur
    
    def rebalance(self, node):
        self.update_height(node)
        balance = self.get_balance(node)
        
        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.rotate_right(node)
        
        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        
        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.rotate_left(node)

        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        
        return node
    
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
            return 
    
    def delete(self, root, id, type):
        if not root:
            return root
        
        if id < int(root.data.id):
            root.left = self.delete(root.left, id, type)
        elif id > int(root.data.id):
            root.right = self.delete(root.right, id, type)
        else:
            if root.left is None and root.right is None:
                root = None
            elif root.left is not None and root.right is not None:
                min_node = self.min_value_node(root.right)
                root.data = min_node.data
                #root.right = self.delete(root.right, int(min_node.data.id), type)
            else:
            
                if root.left is not None:
                    root =  root.left
                else:
                    root = root.right
            
            
            
            # Xóa kem trong tệp txt và sửa id
            # Đọc dữ liệu từ file 
            
            if type == "ice-cream":
                file_path = 'icecream.txt'
            elif type == 'employee':
                file_path = 'Employee.txt'

            with open(file_path, 'r') as file:
                lines = file.readlines()

            # Xóa dòng có id cần xóa
            lines = [line for line in lines if not line.startswith(f'{id}')]


            updated_lines = []
            for i, line in enumerate(lines):
                new_id = str(i + 1).zfill(2)
                updated_line = f"{new_id}-{line.split('-', 1)[1]}"
                updated_lines.append(updated_line)
            
            os.remove(file_path)

            # Ghi dữ liệu đã xử lý vào file mới
            with open(file_path, 'w') as file:
                file.writelines(updated_lines)

            file.close()
            
        return self.rebalance(root)
    
    def clear(self):
        self.root = None
    
    def update(self):
        
        list_ice_cream = read_file_ice_cream()
        for i in list_ice_cream:
            icecream_id = i
            icecream_name = list_ice_cream[i][0]
            icecream_price = list_ice_cream[i][1]
            icecream = IceCream(icecream_id, icecream_name, icecream_price)
            self.root = self.add(icecream, self.root)
    
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
        print()