data = [int(line.split('\n')[0]) for line in open('data.txt')]

for i in data:
    for j in data:
        if i + j == 2020:
            print(i*j)
            exit()
print('no combination found')