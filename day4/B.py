fields, people, person, valids, count = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'], [], {}, 0, 0

for i in [i[:-1] for i in open('data.txt')]:
    if i == '':
        people.append(person.copy())
        person = {}
        continue
    for entry in i.split(' '): person[entry.split(':')[0]] = entry.split(':')[1]
people.append(person.copy())

for p in people:
    for f in fields:
        if f not in p: continue
        count += 1 if f == 'byr' and len(p[f]) == 4 and int(p[f]) >= 1920 and int(p[f]) <= 2020 else 0
        count += 1 if f == 'iyr' and len(p[f]) == 4 and int(p[f]) >= 2010 and int(p[f]) <= 2020 else 0
        count += 1 if f == 'eyr' and len(p[f]) == 4 and int(p[f]) >= 2020 and int(p[f]) <= 2030 else 0
        count += 1 if (f == 'hgt' and p[f][-2:] == 'cm' and int(p[f][:-2]) >= 150 and int(p[f][:-2]) <= 193) else 0
        count += 1 if (f == 'hgt' and p[f][-2:] == 'in' and int(p[f][:-2]) >= 59 and int(p[f][:-2]) <= 76) else 0
        count += 1 if f == 'hcl' and p[f][0] == '#' and p[f][1:].lower().isalnum() else 0
        count += 1 if f == 'pid' and p[f].isnumeric() and len(p[f]) == 9 else 0
        count += 1 if f == 'ecl' and p[f] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] else 0
    valids += 1 if count == 7 else 0
    count = 0

print(valids)