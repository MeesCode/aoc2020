rules = []
my_ticket = []
nearby_tickets = []
data_type = 'rules'

# parse data
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
    
# return a list of invalid values that fit in no rule
# given a list of values
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

# check if all values on a ticket are valid
def valid_ticket(t):
    if len(invalid_values(t)) > 0:
        return False
    return True
    
# return a list of possible properies given a list of values
def find_property(values):
    valid_properties = []
    for r in rules:
        valid = True
        for i in values:
            valid = (i >= r['ranges'][0]['low'] and i <= r['ranges'][0]['high']) or (i >= r['ranges'][1]['low'] and i <= r['ranges'][1]['high'])
            if not valid: break
        if valid: valid_properties.append(r['name'])
    return valid_properties

valid_tickets = []
properties = []
property_values = []

# remove invalid tickets
for i in nearby_tickets:
    if valid_ticket(i):
        valid_tickets.append(i)

# make a set of lists where every list contains all values for a given property
for i in range(len(valid_tickets[0])):
    pv = []
    for t in valid_tickets:
        pv.append(t[i])
    property_values.append(pv)

# create a list of possible properties for each set of values
for i in property_values:
    properties.append(find_property(i))

# reduce list of possible properties by values so that every set of values
# corresponds to only a single property
for _ in properties:
    for i in properties:
        if len(i) == 1:
            for j in properties:
                if j == i:
                    continue
                if i[0] in j:
                    j.remove(i[0])

# list of lists into list of strings
properties = [i[0] for i in properties]

# find the product of departure properties 
res = 1
for i in range(len(properties)):
    if len(properties[i]) >= 9 and properties[i][0:9] == 'departure':
        res *= my_ticket[i]

print(res)