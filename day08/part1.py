input = open("day08.input", "r").read().strip().split("\n")

acc = 0
ptr = 0
vis = [False for i in range(len(input))]
while ptr < len(input) and ptr >= 0:
    instr = input[ptr]
    code, arg = instr.split(" ")
    arg = int(arg)
    if vis[ptr]:
        break
    vis[ptr] = True
    if code == "acc":
        acc += arg
        ptr += 1
    elif code == "jmp":
        ptr += arg
    elif code == "nop":
        ptr += 1
print(acc)