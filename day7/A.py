bags = []

data = [i[:-1] for i in open('data.txt')]

for d in data:
    parts = d.split(" ")
    name = ' '.join(parts[0:2])
    contain_str = parts[4:]
    co = []
    for i in range(len(contain_str)):
        if(not contain_str[i].isnumeric()): continue
        b = {}
        b['cap'] = int(contain_str[i])
        b['name'] = ' '.join(contain_str[i+1:i+3])
        co.append(b)
    bags.append({'name': name, 'contains': co})

def can_contain(name, bag_set=set()):
    names = []
    for b in bags:
        for c in b['contains']:
            if c['name'] == name:
                bag_set.add(b['name'])
                names.append(b['name'])
    if len(names) == 0:
        return bag_set
    return set.union(*[can_contain(n) for n in names])

print(len(can_contain('shiny gold')))


    