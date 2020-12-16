rules = []
my_ticket = []
nearby_tickets = []
data_type = 'rules'

for i in [i[:-1] for i in open('data.txt')]:
    if i == '': continue
    if i == 'your ticket:': 
        data_type = 'your ticket'
        continue
    if i == 'nearby tickets:': 
        data_type = 'nearby tickets'
        continue

    if data_type == 'rules':
        rules.append({
            'name': i.split(':')[0],
            'ranges': [
                {
                    'low': int(i.split(':')[1].split(' or ')[0].split('-')[0]),
                    'high': int(i.split(':')[1].split(' or ')[0].split('-')[1])
                },
                {
                    'low': int(i.split(':')[1].split(' or ')[1].split('-')[0]),
                    'high': int(i.split(':')[1].split(' or ')[1].split('-')[1])
                }
            ]
        })

    if data_type == 'your ticket':
        my_ticket = [int(j) for j in i.split(',')]

    if data_type == 'nearby tickets':
        nearby_tickets.append([int(j) for j in i.split(',')])
    
def invalid_values(values):
    invalids = []
    for i in values:
        valid = False
        for r in rules:
            for rule in r['ranges']:
                if i >= rule['low'] and i <= rule['high']:
                    valid = True
                    break
            if valid:
                break
        if not valid:
            invalids.append(i)
    return invalids   

invalids = []
for i in nearby_tickets:
    invalids.extend(invalid_values(i))

print(sum(invalids))