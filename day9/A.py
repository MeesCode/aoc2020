n = [int(i[:-1]) for i in open('data.txt')]

def get_sums(ls):
    return sum([[i+j for j in ls] for i in ls], [])

def find_answer(pl):
    for i in range(pl, len(n)):
        if n[i] not in get_sums(n[i-pl:i]): return n[i]

print(find_answer(25))