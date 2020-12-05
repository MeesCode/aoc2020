# read file
data = [i[:-1] for i in open('data.txt')]

# init variables
people = []
person = {}
fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

# parse data
for i in data:
    if i == '':
        people.append(person.copy())
        person = {}
        continue
    for entry in i.split(' '):
        person[entry.split(':')[0]] = entry.split(':')[1]
people.append(person.copy())

# validate
valids = 0
count = 0
for p in people:
    for f in fields:
        if f in p:
            count += 1
    if count == 7:
        valids += 1
    count = 0

print(valids)