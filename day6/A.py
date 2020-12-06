al = [set()]
[al.append(set()) if d == '' else al[-1].update(set(d)) for d in [i[:-1] for i in open('data.txt')]]
print(sum([len(i) for i in al]))