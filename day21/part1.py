input = open("day21.input", "r").read().strip().split("\n")

allergen_map = {}
freq = {}
for line in input:
    ingr, allerg = line[:-1].split(" (contains ")
    ingr = ingr.split(" ")
    allerg = allerg.split(", ")
    for ingred in ingr:
        if ingred not in freq:
            freq[ingred] = 0
        freq[ingred] += 1
    for allergen in allerg:
        if allergen not in allergen_map:
            allergen_map[allergen] = set(ingr)
        allergen_map[allergen] = allergen_map[allergen].intersection(set(ingr))

allerg_ingr = set()
for allerg in allergen_map:
    allerg_ingr = allerg_ingr.union(allergen_map[allerg])
res = 0
for ingr in freq:
    if ingr not in allerg_ingr:
        res += freq[ingr]
print(res)