from avl_tree import *
from List_Of_Employ import read_file_employ
from Ice_Cream import *

class Employee:
    
    def __init__(self, id, name, position):
        self.id = id
        self.name = name
        self.position = position

class Employee_Management:
    
    def __init__(self):
        self.tree = Avl_Tree()
        list_employ = read_file_employ()
        for i in list_employ:
            employ_id = i
            employ__name = list_employ[i][0]
            employ_position = list_employ[i][1]
            employ = Employee(employ_id, employ__name, employ_position)
            self.tree.root = self.tree.add(employ, self.tree.root)
    
    def add_new_employ(self):
        new_employ_id = input("Please enter employee id: ")
        if self.tree.find(int(new_employ_id)):
            print("ID is already existed")
            return
        new_employ_name = input("Please enter employee name: ")
        new_employ_position = input("Please enter employee position: ")
        employ = Employee(new_employ_id, new_employ_name, new_employ_position)
        self.tree.root = self.tree.add(employ, self.tree.root)
        
        
        # Thêm kem vào tệp txt
        file = open('employee_information.txt', 'a')
        file.write(f"\n{new_employ_id}-{new_employ_name}-{new_employ_position}")
        file.close()
        
    '''
    def modify_employ(self):
        self.show_employ()
        print()
        employ_id = int(input("Please enter employee id you want to modify: "))
        print()
        employ = self.tree.find(employ_id)
        if employ:
            print("Current Name:", employ.data.name)
            print()
            change = input("Do you want to modify (y/n)? ")
            print()
            if change == 'y' or change == "Y":
                employ.data.name = input("Please enter a new name: ")
            
            print("Current Position:", employ.data.position)
            print()
            change = input("Do you want to modify (y/n)? ")
            if change == 'y' or change == "Y":
                employ.data.position = input("Please enter a new position: ")
                print()
        
        #print("After change:", employ.data.id, employ.data.name, employ.data.position)
        
        #Modify employ vào txt
        with open('employee_information.txt', 'r') as file:
            lines = file.readlines()
        
        # Cập nhật tên và giá cho dòng có id cần sửa
        updated_lines = []
        for line in lines:
            if line.startswith(f'{employ_id}-'):
                parts = line.strip().split('-')
                updated_line = f"{parts[0]}-{employ.data.name}-{employ.data.position}\n"
                updated_lines.append(updated_line)
            else:
                updated_lines.append(line)
            
            # Ghi dữ liệu đã xử lý vào file mới
        with open('employee_information.txt', 'w') as file:
            file.writelines(updated_lines)
        file.close()
    '''
    
    def modify_employ(self):
        self.show_employ()
        print()
        employ_id = input("Please enter employee id you want to modify: ")
        print()
        employ = self.tree.find(int(employ_id))
        
        if employ:
            print("Current Name:", employ.data.name)
            print()
            change_name = input("Do you want to modify the name (y/n)? ")
            print()
            if change_name.lower() == 'y':
                employ.data.name = input("Please enter a new name: ")
            
            print("Current Position:", employ.data.position)
            print()
            change_position = input("Do you want to modify the position (y/n)? ")
            if change_position.lower() == 'y':
                employ.data.position = input("Please enter a new position: ")
                print()
            
            # Modify employee in the text file
            file_path = 'employee_information.txt'
            
            # Read the file content
            with open(file_path, 'r') as file:
                lines = file.readlines()
            
            # Update the line with the given employee id
            updated_lines = []
            found = False
            for line in lines:
                if line.startswith(f'{employ_id}-'):
                    parts = line.strip().split('-')
                    updated_line = f"{parts[0]}-{employ.data.name}-{employ.data.position}\n"
                    updated_lines.append(updated_line)
                    found = True
                else:
                    updated_lines.append(line)
            
            if not found:
                print(f"Employee ID {employ_id} not found in file.")
            else:
                
                # Write the updated lines back to the file
                with open(file_path, 'w') as file:
                    file.writelines(updated_lines)
                print()
                print("Employee information updated successfully.")
        else:
            print("Employee not found.")
    
    def show_employ(self):
        print("+-----------------------MIXUE EMPLOYEE-----------------------+")
        print("|   ID   |                NAME                 |   POSITION  |")
        print("+------------------------------------------------------------+")
        employ = read_file_employ()
        for i in employ:
            print(f"|   {i}   |  {employ[i][0]}" + " " * (35-len(employ[i][0])) + "|" + f"   {employ[i][1]}" + " " * (10 - len(employ[i][1])) + "|")
        print("+------------------------------------------------------------+")

