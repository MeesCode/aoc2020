import copy
import math

TILE_WIDTH = 10
TILE_HEIGHT = 10

tiles = []

cur_tile = {}
cur_data = []

def flip(my_data):
    ret_data = ['' for _ in range(len(my_data[0]))]
    for i in range(len(my_data)):
        ret_data[i] = my_data[i][::-1]
    return ret_data

def rotate(my_data):
    ret_data = ['' for _ in my_data]
    for x in range(len(my_data[0])):
        for y in range(len(my_data)):
            ret_data[x] += my_data[y][x]
    return flip(ret_data)

for line in [i[:-1] for i in open('data.txt')]:

    if line == '':
        borders = []
        borders.append(cur_data[0])
        l,r = [],[]
        for y in range(TILE_HEIGHT):
            r.append(cur_data[y][TILE_WIDTH-1])
        borders.append(cur_data[TILE_HEIGHT-1])
        for y in range(TILE_HEIGHT):
            l.append(cur_data[y][0])
        borders.append(''.join(l))
        borders.append(''.join(r))
        cur_tile['borders'] = copy.deepcopy(borders)

    if line == '':
        cur_tile['data'] = copy.deepcopy(cur_data)
        tiles.append(copy.deepcopy(cur_tile))
        cur_tile = {}
        cur_data = []
        continue

    if line[0] == 'T':
        cur_tile['id'] = int(line.split(' ')[1][:-1])
        continue

    cur_data.append(line)

for t in tiles:
    t['matches'] = 0
    t['top'], t['bottom'], t['left'], t['right'] = False, False, False, False
    match = 'top'
    for b in t['borders']:
        found = False

        for t2 in tiles:
            if t2['id'] == t['id']: continue

            for b2 in t2['borders']:
                if b == b2 or b == b2[::-1]:
                    # print('tile', t['id'], 'and', t2['id'])
                    t['matches'] += 1
                    t[match] = True
                    found = True
                    break

            if found: break
        if match == 'top': match = 'right'
        if match == 'right': match = 'bottom'
        if match == 'bottom': match = 'left'

def match_right(tile1, tile2):
    new_tile2 = copy.deepcopy(tile2)
    tile1_right = ''
    tile2_left = ''
    for i in tile1['data']:
        tile1_right += i[TILE_WIDTH-1]

    for _ in range(2): # flip
        for _ in range(4): #rotate
        
            tile2_left = ''
            for i in new_tile2['data']:
                tile2_left += i[0]

            if tile1_right == tile2_left:
                return True, new_tile2
            
            new_tile2['data'] = rotate(new_tile2['data'])
        new_tile2['data'] = flip(new_tile2['data'])

    return False, new_tile2

def match_bottom(tile1, tile2):
    tile1['data'] = rotate(tile1['data'])
    tile1['data'] = rotate(tile1['data'])
    tile1['data'] = rotate(tile1['data'])

    success, tile2_new = match_right(tile1, tile2)
    tile1['data'] = rotate(tile1['data'])
    tile2_new['data'] = rotate(tile2_new['data'])

    if success: return True, tile2_new
    return False, tile2_new


# print(match_bottom(tiles[1], tiles[7]))
# exit()
    

sidelength = int(math.sqrt(len(tiles)))

grid = [[{} for _ in range(sidelength)] for _ in range(sidelength)]

topleft = {}
for t in tiles:
    if t['matches'] == 2: 
        topleft = t
        break

# rotate topleft until match right and bottom exist
for i in range(3):

    for t in tiles:
        if t['id'] == topleft['id']: continue
        m_right, _ = match_right(topleft, t)
        if m_right: break

    for t in tiles:
        if t['id'] == topleft['id']: continue
        m_bottom, _ = match_bottom(topleft, t)
        if m_bottom: break

    if m_right and m_bottom:
        grid[0][0] = topleft
        break
    else:
        topleft['data'] = rotate(topleft['data'])

def print_grid(grid):
    for y in grid:
        y_str = ''
        for x in y:
            if 'id' in x:
                y_str += str(x['id']) + ' '
            else: 
                y_str += 'xxxx '
        print(y_str)
    print()

def print_graphic(grid):
    for y in grid:
        for line in range(TILE_HEIGHT):
            y_str = ''
            for x in y:
                if 'id' in x:
                    y_str += str(x['data'][line]) + ' '
                else: 
                    y_str += 'xxxxxxxxxx '
            print(y_str)
        print()
    print()

# fill in grid
for y in range(sidelength):
    for x in range(sidelength):
        if x == 0 and y == 0: continue

        for t in tiles:
            if x == 0:
                if t['id'] == grid[y-1][0]['id']: continue
                match, tile_new = match_bottom(grid[y-1][0], t)
            else:
                if t['id'] == grid[y][x-1]['id']: continue
                match, tile_new = match_right(grid[y][x-1], t)
            if match:
                grid[y][x] = tile_new
                break

print_grid(grid)
print_graphic(grid)

removed_borders = ['' for _ in range((TILE_HEIGHT-2) * sidelength)]

for x in range(sidelength):
    for y in range(sidelength):
        for line in range(1, TILE_HEIGHT-1):
            removed_borders[(y*(TILE_HEIGHT-2)) + (line-1)] += grid[y][x]['data'][line][1:-1]

for i in removed_borders:
    print(i)

def roughness(pic):
    d_count = 0
    for y in range(len(pic)-2):
        for x in range(18, len(pic[0]) - 1):
            if (pic[y][x] == '#' and 
                pic[y+1][x-18] == '#' and 
                pic[y+1][x-13] == '#' and 
                pic[y+1][x-12] == '#' and 
                pic[y+1][x-7] == '#' and 
                pic[y+1][x-6] == '#' and 
                pic[y+1][x-1] == '#' and 
                pic[y+1][x] == '#' and 
                pic[y+1][x+1] == '#' and 
                pic[y+2][x-17] == '#' and 
                pic[y+2][x-14] == '#' and 
                pic[y+2][x-11] == '#' and 
                pic[y+2][x-8] == '#' and 
                pic[y+2][x-5] == '#' and 
                pic[y+2][x-2] == '#'):
                d_count += 1

    # print('Dragons:', d_count)

    hashcounter = 0

    for i in pic:
        for j in i:
            if j == '#':
                hashcounter += 1

    hashcounter -= d_count * 15

    # print('roughness:', hashcounter)
    return hashcounter

min_hash = 999999999
for _ in range(2): # flip
    for _ in range(4): #rotate
        min_hash = min(min_hash, roughness(removed_borders))

        removed_borders = rotate(removed_borders)
    removed_borders = flip(removed_borders)

print("result:", min_hash)