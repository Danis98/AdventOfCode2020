from functools import reduce
import operator

def mult(a):
    return reduce(operator.mul, a, 1)

input = open("day18.input", "r").read().strip().split("\n")

def eval_expr(expr, pos):
    res = 0
    mode = "+"
    acc = 0
    p = pos
    stack = [0]
    while p < len(expr):
        if expr[p] in "0123456789":
            acc = int(expr[p])
            stack[-1] += acc
        elif expr[p] == "+":
            mode = "+"
        elif expr[p] == "*":
            mode = "*"
            stack.append(0)
        elif expr[p] == ")":
            return mult(stack), p
        elif expr[p] == "(":
            acc, np = eval_expr(expr, p+1)
            stack[-1] += acc
            p = np
        # print(p, stack, mode, acc, expr[p])
        p += 1
    return mult(stack), p

print(sum([eval_expr(line, 0)[0] for line in input]))