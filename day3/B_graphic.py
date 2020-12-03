data = [i[:-1] for i in open('data.txt')]
a = [(1,1), (3,1), (5,1), (7,1), (1,2)]
c=1

for (ax, ay) in a:
    d = [list(i) for i in data.copy()]
    x,y=0,0
    cu = 0
    while y < len(d):
        if d[y][x % len(d[0])] == '#':
            d[y][x % len(d[0])] = 'X'
            cu += 1
        else:
            d[y][x % len(d[0])] = 'O'
        print(''.join(d[y]), x, y)
        x += ax
        y += ay
    c *= cu
    print()

print('\nanswer:', c)