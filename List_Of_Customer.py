def read_file_customer():
    file = open('customer_information.txt', 'r')
    d = {}
    for line in file:
        l = line.split("-")
        cart = []
        for i in range(1, len(l)):
            l[i] = l[i].replace('\n', '')
            sl = l[i].split(", ")
            
            cart.append(sl)
            
        d[l[0]] = cart # {id : cart}
    return d