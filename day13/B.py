import math

f = open('data.txt').readlines()
time = int(f[0][:-1])
busses = [int(i) for i in f[1].split(',') if i != 'x']

def lcm(n):  
    ans = 1
    for i in n:  
        ans = int((ans * i)/math.gcd(ans, i))          
    return ans  

def find_offset(m, n, offset):
    i = 1
    while True:
        if i % m == 0 and (i + offset) % n == 0:
            return i
        i += 1

offsets = [find_offset(busses[0], busses[i], i) for i in range(1, len(busses))]
print(offsets)
print(lcm(offsets))
