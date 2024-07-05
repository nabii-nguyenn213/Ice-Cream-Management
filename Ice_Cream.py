from List_Of_IceCream import *
from avl_tree import *


class IceCream:
    def __init__(self,id,  name, price):
        self.id = id
        self.name = name
        self.price = price

class Ice_Cream_Management:
    def __init__(self):
        self.tree = Avl_Tree()
        list_ice_cream = read_file()
        for i in list_ice_cream:
            icecream_id = i
            icecream_name = list_ice_cream[i][0]
            icecream_price = list_ice_cream[i][1]
            icecream = IceCream(icecream_id, icecream_name, icecream_price)
            self.tree.root = self.tree.add(icecream, self.tree.root)
    
    def add_new_ice_cream(self):
        new_icecream_id = input("Please enter ice-cream id: ")
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
    
    def modify_ice_cream(self):
        self.show_menu()
        print()
        ice_cream_id = int(input("Please enter ice-cream id you want to modify: "))
        ice_cream = self.tree.find(ice_cream_id)
        if ice_cream:
            print("Current Name:", ice_cream.data.name)
            change = input("Do you want to modify (y/n)? ")
            if change == 'y' or change == "Y":
                ice_cream.data.name = input("Please enter a new name: ")
            
            print("Current Price:", ice_cream.data.price)
            change = input("Do you want to modify (y/n)? ")
            if change == 'y' or change == "Y":
                ice_cream.data.price = input("Please enter a new price: ")
        
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
    
    def show_menu(self):
        print("+-----------------------Ice Cream Menu-----------------------+")
        print("|   ID   |                NAME                 |    PRICE    |")
        print("+------------------------------------------------------------+")
        ice_cream = read_file()
        for i in ice_cream:
            print(f"|   {i}   |  {ice_cream[i][0]}" + " " * (35-len(ice_cream[i][0])) + "|" + f"      {ice_cream[i][1]}     |")
        print("+------------------------------------------------------------+")