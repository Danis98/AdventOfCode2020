orig = open("day08.input", "r").read().strip().split("\n")

def run(input):
    acc = 0
    ptr = 0
    vis = [False for i in range(len(input))]
    while ptr < len(input) and ptr >= 0:
        instr = input[ptr]
        code, arg = instr.split(" ")
        arg = int(arg)
        if vis[ptr]:
            return -1
        vis[ptr] = True
        if code == "acc":
            acc += arg
            ptr += 1
        elif code == "jmp":
            ptr += arg
        elif code == "nop":
            ptr += 1
    return acc

for i in range(len(orig)):
    input = orig[:]
    if input[i][:3] == "jmp":
        input[i] = "nop"+input[i][3:]
    elif input[i][:3] == "nop":
        input[i] = "jmp"+input[i][3:]
    res = run(input)
    if res != -1:
        print(res)