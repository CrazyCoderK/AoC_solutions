import math

with open("2022\input.txt") as f:
    data = f.read().splitlines()

t = 0
l = 0

for line in data:
    if line == '':
        l.append(t)
        t = 0
    else:
        t += int(line)
l.append(t)
a = max(l)
l.remove(a)
b = max(l)
l.remove(b)
c = max(l)
l.remove(c)
print(a,b,c,+a+b+c)