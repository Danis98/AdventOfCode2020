input = open("day07.input", "r").read().strip().split("\n")

G_inv = {}

for line in input:
    parts = line.split(" bags contain ")
    par = parts[0]
    if par not in G_inv:
        G_inv[par] = {}
    for comp in parts[1].split(", "):
        if comp == 'no other bags.':
            continue
        q, w1, w2, _ = comp.split(" ")
        q = int(q)
        dst = w1+" "+w2
        if dst not in G_inv:
            G_inv[dst] = {}
        G_inv[dst][par] = q

stack = ['shiny gold']
outer = set()

while len(stack) > 0:
    n = stack.pop()
    for p in G_inv[n]:
        stack.append(p)
        outer.add(p)
print(len(outer))