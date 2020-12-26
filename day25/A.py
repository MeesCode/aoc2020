
file = open('data.txt')
card_pub_key = int(next(file).strip())
door_pub_key = int(next(file).strip())

print('card key:', card_pub_key)
print('door key:', door_pub_key)

value = 1
devider = 20201227
subject_number = 7

def calc_loop_size(pub_key, subject_number):
    value = 1
    loop_size = 1
    while True:
        value *= subject_number
        value = value % devider

        if value == pub_key:
            return loop_size
        
        loop_size += 1

def transform(pub_key, loop_size):
    value = 1
    for _ in range(loop_size):
        value *= pub_key
        value = value % devider
    return value


loop_size_card = calc_loop_size(card_pub_key, subject_number)
loop_size_door = calc_loop_size(door_pub_key, subject_number)

print('loop size card:', loop_size_card)
print('loop size door:', loop_size_door)

encryption_key = transform(door_pub_key, loop_size_card)
print('encryption key:', encryption_key)