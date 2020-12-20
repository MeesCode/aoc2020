import copy

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

all_rules = []
print(rules)
print(strings)

regex = ""

def to_tree(rule):
    global rules
    p_res = []
    for p_index, p in enumerate(rule):
        i_res = []
        for i_index, i in enumerate(p):

            if i.isalpha(): 
                i_res.append(i)
            else:
                i_res.append(to_tree(rules[int(i)]))

        if len(i_res) == 1:
            p_res.append(i_res[0])
        else:
            p_res.append(i_res)

    if len(p_res) == 1:
        return p_res[0]

    return p_res
            


tree = to_tree(rules[0])
print(tree)

tree = str(tree)
tree = tree.replace('[', '(')
tree = tree.replace(']', ')')
tree = tree.replace(', ', '')
tree = tree.replace('\'', '')
tree = tree.replace(')(', ')|(')
tree = '^' + tree[1:-1] + '$'

print(tree)
