with open("3-input.txt", "r") as f:
    d = f.read().split("\n")

# Sets correct pts ascii - elf math
def calc_prio(i):
    if i.islower():
        return ord(i) - 96
    else:
        return ord(i) - 38


# Check if first half has second half stuff
total = 0
for row in d:
    l = len(row) // 2
    r1, r2 = set(calc_prio(i) for i in row[:l]), set(calc_prio(i) for i in row[l:])
    for v in r1:
        if v in r2:
            total += v

print("1: ", total)

# Need to re-group in parts of 3
def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i : i + n]


# Re-calc row for pts
d = [set(calc_prio(i) for i in row) for row in d]
groups = list(chunks(d, 3))
found = False
total2 = 0

for group in groups:
    found = False

    for row in group:
        if found:
            break

        for v in row:
            if found:
                break

            if v in group[0] and v in group[1] and v in group[2]:
                found = True
                total2 += v
                break

print("2: ", total2)
