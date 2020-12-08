input = open("day07.input", "r").read().strip().split("\n")

G = {}

for line in input:
    parts = line.split(" bags contain ")
    par = parts[0]
    if par not in G:
        G[par] = {}
    for comp in parts[1].split(", "):
        if comp == 'no other bags.':
            continue
        q, w1, w2, _ = comp.split(" ")
        q = int(q)
        dst = w1+" "+w2
        if dst not in G:
            G[dst] = {}
        G[par][dst] = q

stack = [('shiny gold', 1)]
quant = 0

while len(stack) > 0:
    n = stack.pop()
    quant += n[1]
    for p in G[n[0]]:
        stack.append((p, n[1]*G[n[0]][p]))
print(quant-1)