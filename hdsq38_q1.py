def hash_quadratic(keys):
    table = ["-"]*19
    for key in keys:
        h = (6*key + 3) % 19
        i = h
        count = 1
        while table[i] != "-" and count != 19:
            i = (h + (count**2)) % 19
            count += 1
        if count == 1 or count != 19:
            table[i] = key
    return table

def hash_double(keys):
    table = ["-"]*19
    for key in keys:
        h = (6*key + 3) % 19
        i = h
        if table[i] == "-":
            table[i] = key
        else:
            count = 1
            while table[i] != "-" and count <= 19:
                i = (i + (11 - (key % 11))) % 19
                count += 1
            if count <= 19:
                table[i] = key
    return table
