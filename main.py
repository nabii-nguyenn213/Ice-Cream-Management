from Ice_Cream import *

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
    while option < 1 and option > 8:
        option = int(input("Choose an option (1-8): "))
    return option

def customer_menu():
    pass

def choose_menu():
    print("+------------MENU-------------+")
    print("|  1. Employee                |")
    print("|  2. Customer                |")
    print("+-----------------------------+")
    option = int(input("Choose an option(1-2): "))
    while option > 2 or option < 1:
        option = int(input("Choose an option(1-2): "))
    return option

def main():
    option = choose_menu()
    if option == 1:
        employee_option = employee_menu()
        management = Ice_Cream_Management()
        if employee_option == 1:
            management.show_menu()
        elif employee_option == 2:
            management.add_new_ice_cream()
        elif employee_option == 3:
            management.show_menu()
            ice_cream_id = int(input("Please enter ice-cream id you want to delete: "))
            if management.find(ice_cream_id):
                management.root = management.delete_ice_cream(management.root, ice_cream_id)
        elif employee_option == 4:
            management.modify_ice_cream()
        elif employee_option == 5:
            pass
        elif employee_option == 6:
            pass
        elif employee_option == 7:
            pass
        else:
            pass
    else:
        customer_option = customer_menu()

if __name__ == "__main__":
    main()