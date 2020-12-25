
flipped = set()

def getNeighbours(tile):
    (x,y) = tile
    return [
        (x+1, y),
        (x+.5, y+1),
        (x-.5, y+1),
        (x-1, y),
        (x-.5, y-1),
        (x+.5, y-1)
    ]

for line in [i.strip() for i in open('data.txt')]:

    x, y, i = 0, 0, 0
    while i < len(line):
        if line[i] == 'e':
            x += 1
            i += 1
            continue

        if line[i] == 's' and line[i+1] == 'e':
            x += .5
            y += 1
            i += 2
            continue

        if line[i] == 's' and line[i+1] == 'w':
            x -= .5
            y += 1
            i += 2
            continue

        if line[i] == 'w':
            x -= 1
            i += 1
            continue

        if line[i] == 'n' and line[i+1] == 'w':
            x -= .5
            y -= 1
            i += 2
            continue

        if line[i] == 'n' and line[i+1] == 'e':
            x += .5
            y -= 1
            i += 2
            continue

    if (x, y) in flipped:
        flipped.remove((x,y))
    else:
        flipped.add((x,y))

def getBlackNeigbours(tile):
    global flipped
    count = 0
    for i in getNeighbours(tile):
        if i in flipped:
            count += 1
    return count

def cycle():
    global flipped
    ret = flipped.copy()
    for tile in flipped:
        alltiles = getNeighbours(tile)
        alltiles.append(tile)
        for n in alltiles:
            bn = getBlackNeigbours(n)

            if n in flipped and (bn == 0 or bn > 2):
                if n in ret: ret.remove(n)

            if n not in flipped and bn == 2:
                ret.add(n)

    return ret

for i in range(100):
    print(i, len(flipped))
    flipped = cycle()

print(i, len(flipped))