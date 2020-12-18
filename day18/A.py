
def evaluate(my_expr):
    val = 1
    op = None
    # print('eval:', my_expr)
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