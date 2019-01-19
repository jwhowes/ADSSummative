k2 = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
k3 = [0, 1, 8, 27, 64, 125, 343, 512, 729]
k4 = [0, 1, 16, 81, 256, 625, 196, 2401, 4096, 6561]

'''def k_child(n, k):
    num = 0
    for char in str(n):
        num += int(char)**k
    return num'''

def k_child(n, k):
    global k2
    global k3
    global k4
    result = 0
    if k == 2:
        ks = k2
    elif k == 3:
        ks = k3
    else:
        ks = k4
    for i in str(n):
        result += ks[int(i)]
    return result

def k_ephemeral(n, k, prev = {}, all_p = {}):
    '''Evaluates whether or not a given number is k ephemeral'''
    #If n is a previously checked value, it can be immediately evaluated
    if n in all_p:
        for i in prev:
            all_p[i] = all_p[n]
        return all_p[n]
    #If n is in the dictionary of previously checked values (for this n), it is k eternal
    if n in prev:
        all_p.update(prev)
        return False
    #n is added to and prev so that future values can be checked to see if they are k eternal
    prev[n] = False
    #If n fails the base cases the function recurses with the k child of n
    return k_ephemeral(k_child(n, k), k, prev, all_p)

def count_ephemeral(n1, n2, k):
    num = 0
    #All p is set up as a dictionary of previous values with 1 instantly passing
    all_p = {}
    all_p[1] = True
    #loop through all values from n1 to n2 counting the number that are k ephemeral
    for i in range(n1, n2):
        if k_ephemeral(i, k, {}, all_p):
            num += 1
    return num
