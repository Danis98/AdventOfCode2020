def lmap(func, x):
    return list(map(func, x))

def combat(d1, d2):
    prev1 = set()
    prev2 = set()
    idx = 1
    while len(d1) > 0 and len(d2) > 0:
        s1, s2 = lmap(lambda x: ','.join(lmap(str, x)), [d1, d2])
        if s1 in prev1 or s2 in prev2:
            return 1, d1
        prev1.add(s1)
        prev2.add(s2)
        n1, n2 = d1.pop(), d2.pop()
        if len(d1) >= n1 and len(d2) >= n2:
            winner, d = combat(d1[-n1:], d2[-n2:])
            if winner == 1:
                d1 = [n2, n1] + d1
            elif winner == 2:
                d2 = [n1, n2] + d2
        else:
            if n1 > n2:
                d1 = [n2, n1] + d1
            elif n2 > n1:
                d2 = [n1, n2] + d2
        idx += 1
    return (2, d2) if len(d1) == 0 else (1, d1)

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
winner, d = combat(d1, d2)
score = 0
for i, card in enumerate(d):
    score += (i+1)*card
print(score)