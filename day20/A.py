import copy

TILE_WIDTH = 10
TILE_HEIGHT = 10

tiles = []

cur_tile = {}
cur_data = []

for line in [i[:-1] for i in open('data.txt')]:

    if line == '':

        borders = []
        borders.append(cur_data[0])
        borders.append(cur_data[TILE_HEIGHT-1])
        l,r = [],[]
        for y in range(TILE_HEIGHT):
            l.append(cur_data[y][0])
            r.append(cur_data[y][TILE_WIDTH-1])
        borders.append(''.join(l))
        borders.append(''.join(r))
        cur_tile['borders'] = copy.deepcopy(borders)

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
    for b in t['borders']:
        found = False

        for t2 in tiles:
            if t2['id'] == t['id']: continue

            for b2 in t2['borders']:
                if b == b2 or b == b2[::-1]:
                    # print('tile', t['id'], 'and', t2['id'])
                    t['matches'] += 1
                    found = True
                    break

            if found: break
        if found: continue

res = 1
for t in tiles:
    # print('id:', t['id'], '\tmatches:', t['matches'])
    if t['matches'] == 2: 
        res *= t['id']

print('Result:', res)
