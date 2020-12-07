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

def can_contain(name):
    for b in bags:
        if b['name'] == name:
            res = 1
            if len(b['contains']) == 0:
                return 1
            for c in b['contains']:
                res += c['cap']*can_contain(c['name'])
                # print(c['name'], c['cap'], '*', can_contain(c['name']))
            return res
    return 1

print(can_contain('shiny gold')-1)