import string

input = open("day04.input", "r").read().strip().split("\n")

def validate(passport):
    for col in cols:
        if col not in passport:
            return 0
        v = passport[col]
        if col == 'byr':
            if not (len(v) == 4 and int(v) >= 1920 and int(v) <= 2002):
                return 0
        if col == 'iyr':
            if not (len(v) == 4 and int(v) >= 2010 and int(v) <= 2020):
                return 0
        if col == 'eyr':
            if not (len(v) == 4 and int(v) >= 2020 and int(v) <= 2030):
                return 0
        if col == 'hgt':
            if len(v) not in [4, 5]:
                return 0
            val = int(v[:-2])
            unit = v[-2:]
            if not ((unit == 'cm' and val >= 150 and val <= 193)
                    or (unit == 'in' and val >= 59 and val <= 76)):
                return 0
        if col == 'hcl':
            if not (len(v) == 7 and v[0] == '#'
                    and all([d in "abcdef0123456789" for d in v[1:]])):
                return 0
        if col == 'ecl':
            if v not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                return 0
        if col == 'pid':
            if not (len(v) == 9 and v.isnumeric()):
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