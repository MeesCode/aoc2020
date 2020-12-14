def to_binary(val, size=36):
    b = ['0' for i in range(size)]
    for i in range(size):
        cv = 2**(size - (i + 1))
        if cv <= val: 
            val -= cv
            b[i] = '1'
    return b

def to_int(val):
    ret = 0
    for i in range(len(val)):
        if val[i] == '1':
            ret += 2**(len(val) - (i + 1))
    return ret

def apply_mask(binary, mask, size=36):
    my_binary = binary[:]
    for i in range(size):
        if mask[i] != 'X': my_binary[i] = mask[i]
    return my_binary

mem = [0 for i in range(999999)]
cur_mask = ''

for i in [i[:-1] for i in open('data.txt')]:
    if i[:4] == 'mask': cur_mask = list(i.split(' = ')[1])
    else:
        addr = int(i.split('[')[1].split(']')[0])
        val = int(i.split(' = ')[1])
        mem[addr] = to_int(apply_mask(to_binary(val), cur_mask))

print(sum(mem))