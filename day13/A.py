
f = open('data.txt').readlines()
time = int(f[0][:-1])
busses = [int(i) for i in f[1].split(',') if i != 'x']

wait_times = [t - time % t if time % t != 0 else 0 for t in busses]
wait_time = min(wait_times)
bus_id = busses[wait_times.index(wait_time)]

print(wait_time, bus_id, wait_time*bus_id)