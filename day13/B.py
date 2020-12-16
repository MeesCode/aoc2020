f = open('data.txt').readlines()
time = int(f[0][:-1])
times = [i for i in f[1].split(',')]
indexes = []
busses = []

for i in range(len(times)):
    if times[i] != 'x':
        busses.append(int(times[i]))
        indexes.append(i)

offset = 0
cycle = 1

for i in range(len(busses)):
    while True:
        offset += cycle
        if (offset + indexes[i]) % busses[i] == 0: break
    cycle *= busses[i]

print('result: ', offset)
