def read_file_customer():
    file = open('customer_information.txt', 'r')
    d = {}
    for line in file:
        l = line.split("-")
        d[l[0]] = l[1] # {id : cart}
    return d