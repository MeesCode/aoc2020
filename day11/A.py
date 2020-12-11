
def adj_occupied(my_x, my_y, data):
    occ = 0
    for y in range(my_y-1, my_y+2):
        if y < 0 or y >= len(data): continue
        for x in range(my_x-1, my_x+2):
            if x == my_x and y == my_y: continue
            if x < 0 or x >= len(data[0]): continue
            if data[y][x] == '#': occ += 1
    return occ

def cycle(data):
    ret_data = copy(data)
    for y in range(0, len(data)):
        for x in range(0, len(data[0])):
            if data[y][x] == 'L' and adj_occupied(x,y, data) == 0: ret_data[y][x] = '#'
            if data[y][x] == '#' and adj_occupied(x,y, data) >= 4: ret_data[y][x] = 'L'
    return ret_data

def copy(data):
    return [i.copy() for i in data]

def equals(data1, data2):
    if len(data1) != len(data2): return False
    for i in range(0, len(data1)):
        if data1[i] != data2[i]: return False
    return True

def cycle_print(data):
    for i in data:
        print(''.join(i))

def count_occupied(data):
    count = 0
    for y in range(0, len(data)):
        for x in range(0, len(data[0])):
            if data[y][x] == '#': count += 1
    return count

def run(data):
    prev_cycle = []
    cur_cyle = copy(data)
    while not equals(prev_cycle, cur_cyle):
        prev_cycle = copy(cur_cyle)
        cur_cyle = cycle(prev_cycle)
    return cur_cyle

final_state = run([list(i[:-1]) for i in open('data.txt')])
cycle_print(final_state)
print("occupied seats:", count_occupied(final_state))