data = [int(line.split('\n')[0]) for line in open('data.txt')]

for i in data:
    for j in data:
        for k in data:
            if i + j + k == 2020:
                print(i*j*k)
                exit()
print('no combination found')