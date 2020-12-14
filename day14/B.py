def to_binary(val, size=36):
    b = ['0' for i in range(size)]
    for i in range(size):
        cv = 2**(size - (i + 1))
        if cv <= val: 
            val -= cv
            b[i] = '1'
    return b

def to_int(binary):
    ret = 0
    for i in range(len(binary)):
        if binary[i] == '1':
            ret += 2**(len(binary) - (i + 1))
    return ret

def apply_mask(binary, mask, size=36):
    my_binary = binary[:]
    for i in range(size):
        if mask[i] != '0': my_binary[i] = mask[i]
    return my_binary

def get_permutations(binary):
    perms = [binary]
    res = []
    while len(perms) != 0:
        p = perms.pop(0)
        for i in range(len(p) + 1):
            if i == len(p): 
                res.append(p)
                break
            if p[i] == 'X':
                p[i] = '1'
                perms.append(p.copy())
                p[i] = '0'
                perms.append(p.copy())
                break
    return res

mem = {}
cur_mask = ''

for i in [i[:-1] for i in open('data.txt')]:
    if i[:4] == 'mask': cur_mask = list(i.split(' = ')[1])
    else:
        addr = int(i.split('[')[1].split(']')[0])
        val = int(i.split(' = ')[1])
        rng = apply_mask(to_binary(addr), cur_mask)
        # print('', ''.join(to_binary(val)), '\n', ''.join(cur_mask), '\n', ''.join(rng))
        perms = get_permutations(rng)
        # print([''.join(i) for i in perms])
        # print([to_int(i) for i in perms])
        for i in [to_int(i) for i in perms]:
            mem[i] = val

res = 0
for i in mem:
    res += mem[i]
print(res)