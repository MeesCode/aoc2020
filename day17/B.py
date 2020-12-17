import copy 

cube = [[[list(j) for j in [i[:-1] for i in open('data.txt')]]]]

active = 0
for y in cube[0][0]:
    for x in y: 
        if x == '#': active += 1

def expand_cube():
    for w in cube:
        for z in w:
            for y in z:
                y.insert(0, '.')
                y.append('.')
            z.insert(0, ['.' for _ in range(len(z[0]))])
            z.append(['.' for _ in range(len(z[0]))])
        w.insert(0, [['.' for _ in range(len(w[0][0]))] for _ in range(len(w[0]))] )
        w.append([['.' for _ in range(len(w[0][0]))] for _ in range(len(w[0]))] )
    cube.insert(0, [[['.' for _ in range(len(cube[0][0][0]))] for _ in range(len(cube[0][0]))] for _ in range(len(cube[0]))] )
    cube.append([[['.' for _ in range(len(cube[0][0][0]))] for _ in range(len(cube[0][0]))] for _ in range(len(cube[0]))] )

def print_cube():
    for w_index, w in enumerate(cube):
        print('w =', int(-((len(cube) - 1)/2) + w_index))
        for z_index, z in enumerate(w):
            print('z =', int(-((len(w) - 1)/2) + z_index))
            for y in z:
                print(''.join(y))
            print()

def count_neighbours(x,y,z,w):
    counter = 0
    for dw in [w-1, w, w+1]:
        for dz in [z-1, z, z+1]:
            for dy in [y-1, y, y+1]:
                for dx in [x-1, x, x+1]:
                    if dx == x and dy == y and dz == z and dw == w: continue
                    if dx < 0 or dy < 0 or dz < 0 or dw < 0: continue
                    if dw >= len(cube) or dz >= len(cube[dw]) or dy >= len(cube[dw][dz]) or dx >= len(cube[dw][dz][dy]): continue

                    if cube[dw][dz][dy][dx] == '#': counter += 1
    return counter

def cycle(my_cube):
    global active
    for dw, w in enumerate(cube):
        for dz, z in enumerate(w):
            for dy, y in enumerate(z):
                for dx, x in enumerate(y):
                    neighbours = count_neighbours(dx,dy,dz,dw)

                    if x == '#' and neighbours not in [2,3]:
                        active -= 1
                        my_cube[dw][dz][dy][dx] = '.'
                        continue
                    if x == '.' and neighbours == 3:
                        active += 1
                        my_cube[dw][dz][dy][dx] = '#'
                        continue
    return my_cube

# print_cube()

for _ in range(6):
    expand_cube()
    cube = cycle(copy.deepcopy(cube))
    # print_cube()

print(active)