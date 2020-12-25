input = open("day25.input", "r").read().strip().split("\n")

puba, pubb = int(input[0]), int(input[1])
numa, numb = 7, 7
keya, keyb = puba, pubb
while True:
    numa = (numa * 7) % 20201227
    numb = (numb * 7) % 20201227
    keya = (keya * puba) % 20201227
    keyb = (keyb * pubb) % 20201227
    if numa == puba:
        print(keyb)
        break
    if numb == pubb:
        print(keya)
        break