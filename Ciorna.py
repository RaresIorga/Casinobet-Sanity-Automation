def queue_time(customers, n):
    tills = []
    for _ in range(len(customers)):
        row = [0 for _ in range(1)]
        tills.append(row)
    time = 0
    # making a dictionary with the number of used tills and assigned them each a value from the customer list
    try:
        minim = tills[0][0]
    except:
        return 0
    for i in range(0, min(n, len(customers))):
        tills[i][0] = customers[0]
        minim = min(tills[i][0], minim)
        customers.pop(0)
    time = time + minim
    # substacting the time from all the cashiers
    for i in range(0, len(tills)):
        tills[i][0] = tills[i][0] - minim
    # adding another customer to the empty line and calculating until there are no customers waiting
    try:
        minim = tills[0][0]
    except:
        return 0
    while len(customers) > 0:
        for i in range(0, len(tills)):
            if tills[i][0] == 0:
                tills[i][0] = customers[0]
                customers.pop(0)
            minim = min(tills[i][0], minim)
        time = time + minim
        for i in range(0, len(tills)):
            tills[i][0] = tills[i][0] - minim
    # if there are no customers in line, the till will close if they have no one to serve
    try:
        minim = tills[0][0]
    except:
        return 0
    while len(tills) > 0:
        zero_tiles = []
        for i in range(0, len(tills)):
            if tills[i][0] == 0:
                zero_tiles.append(i)
        for i in range(0, len(zero_tiles)):
            cashier = zero_tiles[i]
            tills.remove(tills[i])
        for i in range(0, len(tills)):
            minim = min(tills[i][0], minim)
        time = time + minim
        for i in range(0, len(tills)):
            tills[i][0] = tills[i][0] - minim

    return time

