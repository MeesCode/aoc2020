
flipped = set()

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

print(len(flipped))