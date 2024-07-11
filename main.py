from Ice_Cream import *
from Customers import *
from employee import *

def employee_menu():
    print("+------MIXUE ICE-CREAMING SALE MANAGEMENT------+")
    print("|    1. Show all Ice-cream                     |")
    print("|    2. Add new Ice-cream                      |")
    print("|    3. Delete Ice-cream                       |")
    print("|    4. Modify Ice-cream                       |")
    print("|    5. Modify Employee                        |")
    print("|    6. Add Employee                           |")
    print("|    7. Delete Employee                        |")
    print("|    8. Show Employee                          |")
    print("|    9. Show Invoice                           |")
    print("|    0. Return to Main Menu                    |")
    print("+----------------------------------------------+")
    option = int(input("Choose an option (0-9): "))
    while option < 0 or option > 9:
        option = int(input("Choose an option (0-9): "))
    return option

def customer_menu():
    print("+------MIXUE ICE-CREAMING SALE MANAGEMENT------+")
    print("|    1. Order                                  |")
    print("|    2. Show your order                        |")
    print("|    3. Submit your order                      |") 
    print("|    0. Return to Main Menu                    |")
    print("+----------------------------------------------+")
    option = int(input("Choose an option(1-3): "))
    while option < 0 or option > 3:
        option = int(input("Choose an option(1-3): "))
    return option

def choose_menu():
    print("+------------MENU-------------+")
    print("|  1. Employee                |")
    print("|  2. Customer                |")
    print("|  0. Exit                    |")
    print("+-----------------------------+")
    option = int(input("Choose an option(1-3): "))
    while option > 2 or option < 0:
        option = int(input("Choose an option(1-3): "))
    return option

def main():
    option = choose_menu()
    while option != 0:
        if option == 1:
            employee_option = employee_menu()
            management = Ice_Cream_Management()
            employee = Employee_Management()
            while employee_option != 0:
                if employee_option == 1:
                    management.show_menu()
                    print()
                    
                    employee_option = employee_menu()
                    print()
                elif employee_option == 2:
                    management.add_new_ice_cream()
                    print()
                    
                    print("New ice-cream was added successfully!!!")
                    
                    print()
                    
                    employee_option = employee_menu()
                    print()
                elif employee_option == 3:
                    management.show_menu()
                    ice_cream_id = int(input("Please enter ice-cream id you want to delete: "))
                    if management.tree.find(ice_cream_id):
                        management.tree.root = management.tree.delete(management.tree.root, ice_cream_id, 'ice-cream')
                        management.tree.update('ice-cream')
                        print()
                        print("Ice-cream was deleted successfully!!!")
                        print()
                        
                    else:
                        print("Ice-cream id not found!!!")
                    print()
                    
                    
                    employee_option = employee_menu()
                    print()
                elif employee_option == 4:
                    management.modify_ice_cream()
                    print()
                    print("Ice-cream was changed successfully!!!")
                    
                    employee_option = employee_menu()
                    print()
                elif employee_option == 5:
                    employee.modify_employ()
                    print()
                    employee_option = employee_menu()
                    print()
                    
                elif employee_option == 6:
                    employee.add_new_employ()
                    print()
                    
                    employee_option = employee_menu()
                    print()
                elif employee_option == 7:
                    employee.show_employ()
                    employ_id = int(input("Please enter employee id you want to delete: "))
                    if employee.tree.find(employ_id):
                        employee.tree.root = employee.tree.delete(employee.tree.root, employ_id, 'employee')
                        management.tree.update('employee')
                    else:
                        print("Employee id not found!!!")
                    print()
                    
                    employee_option = employee_menu()
                    
                elif employee_option == 8:
                    employee.show_employ()
                    print()
                    
                    employee_option = employee_menu()
                    print()
                elif employee_option == 9:
                    pass
            else:
                option = choose_menu()
        elif option == 2:
            customer_option = customer_menu()
            customer = Customer_Management()
            customer_id = customer.generate_id()
            while customer_option != 0:
                if customer_option == 1:
                    customer.insert_new_customer(customer_id)
                    print()
                    customer_option = customer_menu()    
                    print()
                elif customer_option == 2:
                    customer.show_cart(customer_id)
                    print()
                    customer_option = customer_menu()    
                    print()
                elif customer_option == 3:
                    customer.generate_invoice(customer_id)
                    print()
                    customer_option - customer_menu()
                    print()
            else:
                option = choose_menu()
            
    else:
        print("Exiting program...")
        e = input("Type any key to exit")

if __name__ == "__main__":
    main()