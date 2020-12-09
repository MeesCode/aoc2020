n = [int(i[:-1]) for i in open('data.txt')]

def get_sums(ls):
    return sum([[i+j for j in ls] for i in ls], [])

def find_number(pl):
    for i in range(pl, len(n)):
        if n[i] not in get_sums(n[i-pl:i]):
            return n[i]

def find_answer(t):
    for sl in range(2, len(n)):
        for i in range(sl, len(n)):
            if sum(n[i-sl:i]) == t: return max(n[i-sl:i]) + min(n[i-sl:i])

print(find_answer(find_number(25)))