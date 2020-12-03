a, c, d = [(1,1), (3,1), (5,1), (7,1), (1,2)], 1, [i[:-1] for i in open('data.txt')]
for (ax, ay) in a:
    x, y, cu = 0, 0, 0
    while y < len(d):
        cu += 1 if d[y][x % len(d[0])] == '#' else 0
        x, y = x+ax, y+ay
    c *= cu
print(c)