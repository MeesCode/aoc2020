
jolts = [int(i[:-1]) for i in open('data.txt')]

jolts.append(max(jolts) + 3)
jolts.append(0)
jolts.sort()

points = [0 for i in jolts]
points[0] = 1

for index in range(len(jolts)):
    for i in range(index-3, index):
        if i < 0: continue
        if jolts[index] - jolts[i] <= 3: 
            points[index] += points[i]

print("result: ", points[-1])