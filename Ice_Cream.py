from List_Of_IceCream import *
from avl_tree import *


class IceCream:
    def __init__(self,id, name, price):
        self.id = id
        self.name = name
        self.price = price

class Ice_Cream_Management:
    
    def __init__(self):
        self.tree = Avl_Tree()
        list_ice_cream = read_file_ice_cream()
        for i in list_ice_cream:
            icecream_id = i
            icecream_name = list_ice_cream[i][0]
            icecream_price = list_ice_cream[i][1]
            icecream = IceCream(icecream_id, icecream_name, icecream_price)
            self.tree.root = self.tree.add(icecream, self.tree.root)
    
    def check_valid_id(self, id):
        if id == 'q' or id == 'Q':
            return id
        try:
            if int(id) > 0:
                return int(id)
            else:
                print("ID INVALID PLEASE ENTER AGAIN")
                return
        except:
            print("ID INVALID PLEASE ENTER AGAIN")
            return 
    
    def add_new_ice_cream(self):
        new_icecream_id = input("Please enter ice-cream id (press 'q' to quit): ")
        
        while self.check_valid_id(new_icecream_id) == None:
            new_icecream_id = input("Please enter ice-cream id (press 'q' to quit): ")
        
        if new_icecream_id == 'q' or new_icecream_id == "Q":
            return
        
        if self.tree.find(int(new_icecream_id)):
            print("ID is already existed")
            return
        new_icecream_name = input("Please enter ice-cream name: ")
        new_icecream_price = input("Please enter ice-cream price: ")
        icecream = IceCream(new_icecream_id, new_icecream_name, new_icecream_price)
        self.tree.root = self.tree.add(icecream, self.tree.root)
        # Thêm kem vào tệp txt
        file = open('icecream.txt', 'a')
        file.write(f"\n{new_icecream_id}-{new_icecream_name}-{new_icecream_price}")
        file.close()
        print("New ice-cream was added successfully!!!")

    
    def modify_ice_cream(self):
        self.show_menu()
        print()
        ice_cream_id = input("Please enter ice-cream id you want to modify (press 'q' to quit):")
        
        while self.check_valid_id(ice_cream_id) == None:
            ice_cream_id = input("Please enter ice-cream id you want to modify (press 'q' to quit): ")
        
        if ice_cream_id == 'q' or ice_cream_id == "Q":
            return
        
        ice_cream = self.tree.find(int(ice_cream_id))
        
        if ice_cream:
            m = input("Please enter what field you want to modify (name, price): ")
            f = m.split(', ')
            while f != ['name'] and f != ['price'] and f != ['name', 'price']:
                m = input("Please enter what field you want to modify (name, price): ")
                f = m.split(', ')
            
            if len(f) == 2:
                change = input("Please enter new name or price (name, price): ")
                c = change.split(', ')
                while len(c) != 2:
                    print("Please enter 2 argument!")
                    change = input("Please enter new name or price (name, price): ")
                    c = change.split(', ')
                    
                ice_cream.data.name = c[0]
                ice_cream.data.price = c[1]
            elif f == ['name']:
                change = input("Please enter new name or price (name, price): ")
                c = change.split(", ")
                while len(c) != 1:
                    print("Please enter 1 argument")
                    change = input("Please enter new name or price (name, price): ")
                    c = change.split(", ")
                ice_cream.data.name = change
            else:
                change = input("Please enter new name or price (name, price): ")
                c = change.split(", ")
                while len(c) != 1:
                    print("Please enter 1 argument")
                    change = input("Please enter new name or price (name, price): ")
                    c = change.split(", ")
                ice_cream.data.price = change
            print()
            print("Ice-cream was modify successfully!!!")
        
        
        #Modify kem vào txt
        with open('icecream.txt', 'r') as file:
            lines = file.readlines()
            
        # Cập nhật tên và giá cho dòng có id cần sửa
        updated_lines = []
        for line in lines:
            if line.startswith(f'{ice_cream_id}-'):
                parts = line.strip().split('-')
                updated_line = f"{parts[0]}-{ice_cream.data.name}-{ice_cream.data.price}\n"
                updated_lines.append(updated_line)
            else:
                updated_lines.append(line)
            
            # Ghi dữ liệu đã xử lý vào file mới
        with open('icecream.txt', 'w') as file:
            file.writelines(updated_lines)
        file.close()
    
    '''
    tim kem theo ten
    '''
    
    def show_menu(self):
        print("+-----------------------Ice Cream Menu-----------------------+")
        print("|   ID   |                NAME                 |    PRICE    |")
        print("+------------------------------------------------------------+")
        ice_cream = read_file_ice_cream()
        for i in ice_cream:
            print(f"|   {i}   |  {ice_cream[i][0]}" + " " * (35-len(ice_cream[i][0])) + "|" + f"      {ice_cream[i][1]}     |")
        print("+------------------------------------------------------------+")