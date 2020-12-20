import re

rules = {}
strings = []

s = False
for i in [i[:-1] for i in open('data.txt')]:
    if i == '':
        s = True
        continue
    
    if not s:
        rule = i.split(': ')[1]
        sects = rule.split(' | ')
        comp = [i.split(' ') for i in sects]
        rules[int(i.split(': ')[0])] = comp
    else:
        strings.append(i)

for r in rules:
    for i in rules[r]:
        if i[0][0] == '"': 
            i[0] = i[0][1:-1]

def regex_rec(rule, max_depth, depth=0):

    if depth > max_depth:
        return ''

    global rules
    my_regex = '('
    for p_index, p in enumerate(rule):

        if p_index != 0: my_regex += '|'

        for i_index, i in enumerate(p):

            if i.isalpha(): return i
            else: my_regex += regex_rec(rules[int(i)], max_depth, depth + 1)

    my_regex += ')'
    return my_regex

def to_regex(rule, max_depth):
    return '^' + regex_rec(rule, max_depth) + '$'

regex = to_regex(rules[0], 100)

print(regex)

counter = 0
for i in strings:
    if re.search(regex, i): 
        # print('match:', i)
        counter += 1

print(counter)
