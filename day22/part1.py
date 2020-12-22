input = open("day22.input", "r").read().strip().split("\n")

d1, d2 = [], []
cur = 1
for line in input:
    if "Player" in line:
        continue
    if len(line) == 0:
        cur = 2
    else:
        n = int(line)
        if cur == 1:
            d1.append(n)
        else:
            d2.append(n)
d1 = d1[::-1]
d2 = d2[::-1]

idx = 1
while len(d1) > 0 and len(d2) > 0:
    n1, n2 = d1.pop(), d2.pop()
    if n1 > n2:
        d1 = [n2, n1] + d1
    elif n2 > n1:
        d2 = [n1, n2] + d2
    idx += 1
d = d1 + d2
score = 0
for i, card in enumerate(d):
    score += (i+1)*card
print(score)