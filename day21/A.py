
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

# print('labels', labels)
# print('words', words)
# print('allergens', allergens)
# print('options', options)
# print()

for i in labels:
    for allergen in i['allergens']:
        options[allergen] = options[allergen] & i['words']

# print('filtered options', options)

filtered = set()
for w in words:
    found = False
    for a in options:
        if w in options[a]:
            found = True
    if not found:
        filtered.add(w)

# print('without alleregens', filtered)

count_words = 0
for i in labels:
    for w in i['words']:
        if w in filtered:
            count_words += 1

print('result:', count_words)