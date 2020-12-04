input = open("day04.input", "r").read().strip().split("\n")

def validate(passport):
    for col in cols:
        if col not in passport:
            return 0
    return 1

valid = 0
cols = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
passport = {}
for line in input:
    if len(line) == 0:
        valid += validate(passport)
        passport = {}
    else:
        for keyval in line.split(" "):
            k, v = keyval.split(':')
            passport[k] = v
valid += validate(passport)
print(valid)