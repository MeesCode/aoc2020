ins = [(i[0:3], int(i[4:])) for i in open('data.txt')]
acc, ip = 0, 0
executed = []

while ip < len(ins):
    if(ip in executed):
        print('accumilator', acc)
        break
    executed.append(ip)
    (i, n) = ins[ip]
    if i == 'acc': acc += n
    if i == 'jmp': ip += n-1
    ip += 1