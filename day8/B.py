ins = [[i[0:3], int(i[4:])] for i in open('data.txt')]
change = 0

def run(instruction):
    acc, ip = 0, 0
    executed = []

    while ip < len(instruction):
        if(ip in executed):
            return (False, acc)
        executed.append(ip)
        [i, n] = instruction[ip]
        if i == 'acc': acc += n
        if i == 'jmp': ip += n-1
        ip += 1

    return (True, acc)

while True:
    my_ins = [i.copy() for i in ins]
    found = 0
    for index, [i, n] in enumerate(my_ins):
        if i == 'jmp' and found == change:
            my_ins[index][0] = 'nop'
            break
        elif i == 'nop' and found == change:
            my_ins[index][0] = 'jmp'
            break
        elif i == 'jmp' or i == 'nop':
            found += 1
    change += 1
    
    (finised, acc) = run(my_ins)
    if(finised):
        print("finished", acc)
        exit()