all_p = {}

def k_child(n, k):
    num = 0
    for char in str(n):
        num += int(char)**k
    return num

def k_ephemeral(n, k, prev = {}, all_p = {}):
    if n in all_p:
        if all_p[n]:
            all_p.update(prev)
        return all_p[n]
    if n in prev:
        return False
    all_p[n] = False
    prev[n] = True
    return k_ephemeral(k_child(n, k), k, prev, all_p)

def count_ephemeral(n1, n2, k):
    num = 0
    all_p = {}
    all_p[1] = True
    for i in range(n1, n2):
        if k_ephemeral(i, k, {}, all_p):
            num += 1
    return num
