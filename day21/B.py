
# get all labels
labels = []
for line in [i[:-2] for i in open('data.txt')]:
    [words, ingredients] = line.split(' (contains ')
    labels.append({'words': set(words.split(' ')), 'allergens': set(ingredients.split(', '))})

# get a set of all words and allergens
allergens = set()
words = set()
for i in labels:
    for a in i['allergens']:
        allergens.add(a)
    for a in i['words']:
        words.add(a)

# options
options = {}
for i in allergens:
    options[i] = words.copy()

print('labels', labels)
print('words', words)
print('allergens', allergens)
print('options', options)
print()

for i in labels:
    for allergen in i['allergens']:
        options[allergen] = options[allergen] & i['words']

print('filtered options', options)

selected = {}

changes = True
while changes:
    changes = False
    for o in options:
        if len(options[o]) == 1:
            changes = True
            target = list(options[o])[0]
            selected[o] = target
            newdict = options.copy()
            del newdict[o]

            for o2 in options:
                if target in options[o2]:
                    options[o2].remove(target)
            break

    if changes: 
        options = newdict.copy()
        continue

print(selected)

keys = selected.keys()
keys = sorted(keys)

string = ''
for k in keys:
    string += selected[k] + ','

string = string[:-1]

print(string)

