numbers =[int(i) for i in open('data.txt').readlines()[0].rsplit()[0].split(',')]

for i in range(len(numbers), 2020):
    # print('turn', i+1)
    # print('numbers', numbers[:-1], 'last number', numbers[i-1])
    if numbers[i-1] not in numbers[:-1]: 
        # print('add 0')
        numbers.append(0)
    else:
        n = numbers[:-1][::-1].index(numbers[i-1]) + 1
        # print(numbers[:-1][::-1], 'find', numbers[i-1], 'plus 1 =', n)
        # print('add', n)
        numbers.append(n)

print(numbers[-1])