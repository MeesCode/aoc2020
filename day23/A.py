string = "942387615"

cups = []

for i in string.strip():
    cups.append(int(i))


def cycle(cups):
    print('cups:\t\t', cups)

    cups = cups.copy()
    current_cup = cups.pop(0)
    picked_cups = cups[:3]
    cups = cups[3:]

    search = current_cup - 1
    index = 0
    while True:
        try:
            index = cups.index(search)
            break
        except:
            search -= 1
            if search < min(cups): search = max(cups)
            continue

    print('picked:\t\t', picked_cups)
    print('destiantion:\t', cups[index])
    
    cups = cups[:index+1] + picked_cups + cups[index+1:]
    cups.append(current_cup)
    return cups

for i in range(100):
    print('-- Move', i, '---')
    cups = cycle(cups)
    print()

print('-- final --')
print('cups:\t\t', cups)