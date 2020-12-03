ax, ay, c, d, x, y = 3, 1, 0, [i[:-1] for i in open('data.txt')], 0, 0
while y < len(d):
    c += 1 if d[y][x % len(d[0])] == '#' else 0
    x, y = x+ax, y+ay
print(c)