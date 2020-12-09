preamble_len = 25
numbers = [int(i[:-1]) for i in open('data.txt')]

def get_sums(ls):
    sums = []
    for i in ls: 
        for j in ls: sums.append(i+j)
    return sums

def find_number():
    for index in range(preamble_len, len(numbers)):
        sums = get_sums(numbers[index-preamble_len:index])
        if numbers[index] not in sums:
            print("number:", numbers[index])
            return numbers[index]

target = find_number()
search_len = 2
while search_len < len(numbers):
    print(search_len)
    for i in range(search_len, len(numbers)):
        print('target:', target, '\tsum:', sum(numbers[i-search_len:i]), '\tsearch space:', numbers[i-search_len:i])
        if sum(numbers[i-search_len:i]) == target:
            print(max(numbers[i-search_len:i]) + min(numbers[i-search_len:i]))
            exit()
    search_len += 1