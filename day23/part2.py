def lmap(func, x):
    return list(map(func, x))

input = open("day23.input", "r").read().strip().split("\n")

class Cup:
    def __init__(self, v):
        self.val = v

cups = lmap(int, list(input[0]))
N = 1000000
cups += [a for a in range(len(cups)+1, N+1)]
cups_n = cups[::]
cup_obj = [Cup(a) for a in range(0, N+2)]
for i, cupv in enumerate(cups):
    cups[i] = cup_obj[cups[i]]
    nprev = (cups_n[i]+N-1)%N
    if nprev == 0:
        nprev = N
    cups[i].nprev = cup_obj[nprev]
    cups[i].nnext = cup_obj[(cups_n[i]+1)%N]
for i in range(len(cups)):
    cups[i].prev = cups[(i+N-1)%N]
    cups[i].next = cups[(i+1)%N]

cur = cups[0]
one = cups[cups_n.index(1)]
for i in range(10000000):
    # if i % 1000000 == 0:
    #     print(i)
    tak = [cur.next, cur.next.next, cur.next.next.next]
    cur.next = tak[-1].next
    tak[-1].next.prev = cur

    prev_v = [c.val for c in tak]
    dest = cur
    for j in range(6):
        dest = dest.nprev
        if dest.val not in prev_v:
            break

    dest.next.prev = tak[-1]
    tak[-1].next = dest.next
    tak[0].prev = dest
    dest.next = tak[0]

    # temp = cur
    # s = ""
    # for j in range(N):
    #     s += "%d " % temp.val
    #     temp = temp.next
    # print(s)

    cur = cur.next
print(one.next.val * one.next.next.val)
