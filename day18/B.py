
def remove_plusses(my_expr):
    counter = 0
    for i in my_expr: 
        if i == '+': counter += 1

    for _ in range(counter):
        splits = my_expr.split(' ')
        for i in range(1, len(splits)-1):
            v1, op, v2 = splits[i-1], splits[i], splits[i+1]
            if op == '+':
                my_expr = my_expr.replace(' '.join([v1, op, v2]), str(int(v1) + int(v2)))
                break
    
    return my_expr


def evaluate(my_expr):
    val = 1
    # print('eval:', my_expr)
    op = None
    my_expr = remove_plusses(my_expr)
    # print('plusses removed:', my_expr)
    for i in my_expr.split(' '):
        if i in ['+', '*']: op = i
        else:
            if op == None: val = int(i)
            if op == '+': val += int(i)
            if op == '*': val *= int(i)
    # print('ret eval:', val)
    return val

def reduce_expression(my_expr):
    exp = my_expr[:]
    cur_exp = ''
    for i in exp:

        cur_exp += i

        if i == '(':
            cur_exp = '('
            start = i
            continue

        if i == ')':
            # print("start evaluation:", cur_exp[1:-1])
            repl = str(evaluate(cur_exp[1:-1]))
            # print('replace', cur_exp, 'with', repl)
            exp = exp.replace(cur_exp, repl)
            return exp

# print(remove_plusses("1 + 2 * 3 + 4 * 5 + 6"))

results = []

for expression in [i[:-1] for i in open('data.txt') if len(i) > 1]:
    count_reduce = 0
    for i in expression:
        if i == ')': count_reduce += 1

    exp = expression[:]
    for i in range(count_reduce):
        exp = reduce_expression(exp)
        # print(exp)

    results.append(evaluate(exp))

print(sum(results))