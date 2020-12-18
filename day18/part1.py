input = open("day18.input", "r").read().strip().split("\n")

def eval_expr(expr, pos):
    res = 0
    mode = "+"
    acc = 0
    p = pos
    while p < len(expr):
        if expr[p] in "0123456789":
            acc = int(expr[p])
            if mode == "+":
                res += acc
            elif mode == "*":
                res *= acc
        elif expr[p] == "+":
            mode = "+"
        elif expr[p] == "*":
            mode = "*"
        elif expr[p] == ")":
            return res, p
        elif expr[p] == "(":
            acc, np = eval_expr(expr, p+1)
            if mode == "+":
                res += acc
            elif mode == "*":
                res *= acc
            p = np
        # print(p, res, mode, acc, expr[p])
        p += 1
    return res, p

print(sum([eval_expr(line, 0)[0] for line in input]))