
jolts = [int(i[:-1]) for i in open('data.txt')]

jolt_diff = [0, 0, 0, 0]

jolts.append(max(jolts) + 3)
jolts.append(0)
jolts.sort()

for i in range(1, len(jolts)):
    diff = jolts[i] - jolts[i-1]
    jolt_diff[diff] += 1

print("result: ", jolt_diff[1] * jolt_diff[3])