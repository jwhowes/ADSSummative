def hash_quadratic(keys):
    table = ["-"]*19
    for key in keys:
        h = (6*key + 3) % 19
        i = h
        count = 1
        #Continue to look for a position until either one is found or more than 19 checks have been made
        while table[i] != "-" and count <= 19:
            i = (h + (count**2)) % 19
            count += 1
        #If less than or equal to 19 checks were made, a space was found and the key should be inserted
        if count <= 19:
            table[i] = key
    return table

def hash_double(keys):
    table = ["-"]*19
    for key in keys:
        h = (6*key + 3) % 19
        i = h
        #If a space can be found immediately, the key should be added
        if table[i] == "-":
            table[i] = key
        else:
            count = 1
            #Continue to check new spaces until one is found or more than 19 checks have been made
            while table[i] != "-" and count <= 19:
                i = (i + (11 - (key % 11))) % 19
                count += 1
            #If less than or equal to 19 checks were made, a space was found and the key should be inserted
            if count <= 19:
                table[i] = key
    return table
