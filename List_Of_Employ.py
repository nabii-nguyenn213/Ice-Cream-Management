def read_file_employ():
    file = open('employee_information.txt', 'r')
    list_of_employ = {}
    for line in file:
        l = line.split("-")
        l[2] = l[2].replace("\n", "")
        list_of_employ[l[0]] = [l[1], l[2]] # {id: [name, position]}
    return list_of_employ