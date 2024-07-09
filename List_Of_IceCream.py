def read_file_ice_cream():
    file = open('icecream.txt', 'r')
    list_of_ice_cream = {}
    for line in file:
        l = line.split("-")
        l[2] = l[2].replace("\n", "")
        list_of_ice_cream[l[0]] = [l[1], l[2]] # {id: [name, price]}
    return list_of_ice_cream