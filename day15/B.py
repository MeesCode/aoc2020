numbers =[int(i) for i in open('data.txt').readlines()[0].rsplit()[0].split(',')]

def find_nth(nums, num):
    spoken = {}
    number = nums[-1]
    for i in range(len(nums)):
        spoken[nums[i]] = i
    next_number = 0

    for i in range(len(nums), num):
        if i == num-1:
            return next_number
        n = next_number
        if n not in spoken:
            next_number = 0
        else:
            next_number = i - spoken[n]
        spoken[n] = i

print(find_nth(numbers, 30000000))