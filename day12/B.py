x, y, dx, dy = 0, 0, 10, -1
for i in [{'ins': l[0], 'val': int(l[1:-1])} for l in open('data.txt') if len(l) > 1]:
    if i['ins'] == 'N': dy -= i['val']
    if i['ins'] == 'S': dy += i['val']
    if i['ins'] == 'E': dx += i['val']
    if i['ins'] == 'W': dx -= i['val']
    if i['ins'] == 'L': 
        for _ in range(int(i['val']/90)): dx, dy = dy, -dx
    if i['ins'] == 'R': 
        for _ in range(int(i['val']/90)): dx, dy = -dy, dx
    if i['ins'] == 'F': x, y = x + i['val'] * dx, y + i['val'] * dy
print(x + y)