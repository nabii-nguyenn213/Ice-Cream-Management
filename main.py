from Ice_Cream import *
from Customers import *

def employee_menu():
    print("+------MIXUE ICE-CREAMING SALE MANAGEMENT------+")
    print("|    1. Show all Ice-cream                     |")
    print("|    2. Add new Ice-cream                      |")
    print("|    3. Delete Ice-cream                       |")
    print("|    4. Modify Ice-cream                       |")
    print("|    5. Generate Invoice                       |")
    print("|    6. Add Employee                           |")
    print("|    7. Delete Employee                        |")
    print("|    8. Return to Main Menu                    |")
    print("+----------------------------------------------+")
    option = int(input("Choose an option (1-8): "))
    while option < 1 or option > 8:
        option = int(input("Choose an option (1-8): "))
    return option

def customer_menu():
    print("+------MIXUE ICE-CREAMING SALE MANAGEMENT------+")
    print("|    1. Order                                  |")
    print("|    2. Show your order                        |")
    print("|    3. Return to Main Menu                    |")
    print("+----------------------------------------------+")
    option = int(input("Choose an option(1-3): "))
    while option < 1 or option > 3:
        option = int(input("Choose an option(1-3): "))
    return option

def choose_menu():
    print("+------------MENU-------------+")
    print("|  1. Employee                |")
    print("|  2. Customer                |")
    print("|  3. Exit                    |")
    print("+-----------------------------+")
    option = int(input("Choose an option(1-3): "))
    while option > 3 or option < 1:
        option = int(input("Choose an option(1-3): "))
    return option

def main():
    option = choose_menu()
    while option != 3:
        if option == 1:
            employee_option = employee_menu()
            management = Ice_Cream_Management()
            while employee_option != 8:
                if employee_option == 1:
                    management.show_menu()
                    print()
                    employee_option = employee_menu()
                    
                elif employee_option == 2:
                    management.add_new_ice_cream()
                    print()
                    employee_option = employee_menu()
                    
                elif employee_option == 3:
                    management.show_menu()
                    ice_cream_id = int(input("Please enter ice-cream id you want to delete: "))
                    if management.find(ice_cream_id):
                        management.root = management.delete_ice_cream(management.root, ice_cream_id)
                    print()
                    employee_option = employee_menu()
                    
                elif employee_option == 4:
                    management.modify_ice_cream()
                    print()
                    employee_option = employee_menu()
                    
                elif employee_option == 5:
                    pass
                elif employee_option == 6:
                    pass
                elif employee_option == 7:
                    pass
            else:
                option = choose_menu()
        elif option == 2:
            customer_option = customer_menu()
            customer = Customer_Management()
            customer_id = customer.generate_id()
            while customer_option != 3:
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
            else:
                option = choose_menu()
            
    else:
        print("Exiting program...")
        e = input("Type any key to exit")

if __name__ == "__main__":
    main()