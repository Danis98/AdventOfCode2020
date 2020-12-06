input = open("day05.input", "r").read().strip().split("\n")

seats = []
for line in input:
    acc = 0
    for c in line:
        acc *= 2
        if c in "BR":
            acc += 1
    seats.append(acc)
seats = sorted(seats)
for i in range(len(seats)-1):
    if seats[i+1] != seats[i]+1:
        print(seats[i]+1)