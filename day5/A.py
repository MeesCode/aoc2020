import math
def decode(s, l, h):
    if len(s) == 0: return l
    if s[0] in ['B', 'R']: return decode(s[1:], math.ceil((l + h)/2), h)
    return decode(s[1:], l, math.floor(h - ((h-l)/2)))
print(max([decode(i[:7], 0, 127) * 8 + decode(i[-3:], 0, 7) for i in [i[:-1] for i in open('data.txt')]]))