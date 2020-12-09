preamble_len = 25
numbers = [int(i[:-1]) for i in open('data.txt')]

def get_sums(ls):
    sums = []
    for i in ls: 
        for j in ls: sums.append(i+j)
    return sums

for index in range(preamble_len, len(numbers)):
    sums = get_sums(numbers[index-preamble_len:index])
    if numbers[index] not in sums:
        print(numbers[index])
        exit()
