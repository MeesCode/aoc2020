v = 0
for p in [i.split(' ') for i in open('data.txt')]:
    [mi, ma], le, st, co = [int(i) for i in p[0].split('-')], p[1][0], p[2][:-1], 0
    for c in st: co += 1 if c == le else 0     
    if co >= mi and co <= ma: v += 1
print(v)