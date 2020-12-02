v = 0
for p in [i.split(' ') for i in open('data.txt')]:
    [mi, ma], le, st = [int(i) for i in p[0].split('-')], p[1][0], p[2][:-1]
    v += 1 if (st[mi-1] == le) + (st[ma-1] == le) == 1 else 0
print(v)