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

matches = {}
for i in range(len(allergen_map)):
    for a in allergen_map:
        for m in matches:
            if matches[m] in allergen_map[a]:
                allergen_map[a].remove(matches[m])
        if len(allergen_map[a]) == 1:
            matches[a] = list(allergen_map[a])[0]
all_list = [a for a in matches]
can_list = [matches[a] for a in sorted(all_list)]
print(','.join(can_list))