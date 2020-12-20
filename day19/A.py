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

regex = ""

def to_tree(rule):
    global regex
    global rules
    regex += '('
    for p_index, p in enumerate(rule):

        if p_index != 0:
            regex += '|'

        for i_index, i in enumerate(p):

            if i.isalpha(): 
                regex += i
            else:
                to_tree(rules[int(i)])

    regex += ')'

tree = to_tree(rules[0])

regex = '^' + regex + '$'

print(regex)
