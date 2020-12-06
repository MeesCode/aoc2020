gr = [[]]
[gr.append([]) if d == '' else gr[-1].append(set(d)) for d in [i[:-1] for i in open('data.txt')]]
print(sum([len(set.intersection(*g)) if len(g) > 0 else 0 for g in gr]))