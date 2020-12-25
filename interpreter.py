class Interpreter:
    def __init__(self, code):
        self.code = code
        self.ip = 0
        self.accum = 0
        self.op_map = {
            'nop': self.nop,
            'acc': self.acc,
            'jmp': self.jmp
        }

    def run(self):
        # vis = set()
        while self.ip >= 0 and self.ip < len(self.code):
            # if self.ip in vis:
            #     break
            # vis.add(self.ip)
            op, arg = self.code[self.ip].split(" ")
            arg = int(arg)
            self.op_map[op](arg)
            self.ip += 1
        print(self.accum)

    def nop(self, arg):
        return

    def acc(self, arg):
        self.accum += arg

    def jmp(self, arg):
        self.ip += arg - 1
