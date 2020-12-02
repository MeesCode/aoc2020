data = [int(line) for line in open('data.txt')]

for i in data:
    for j in data:
        if i + j == 2020:
            print(i*j)
            exit()
print('no combination found')