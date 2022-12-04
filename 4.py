with open("4-input.txt", "r") as f:
    d = f.read().split("\n")

total1 = 0
total2 = 0

for r in d:
    if r == "":
        continue
    a, b = [(int(v[0]), int(v[1])) for v in [v.split("-") for v in r.split(",")]]
    if a[0] >= b[0] and a[1] <= b[1] or b[0] >= a[0] and b[1] <= a[1]:
        total1 += 1
    if a[0] >= b[0] and a[1] <= b[1] or b[0] <= a[1] and b[1] >= a[0]:
        total2 += 1

print("total 1: ", total1)
print("total 2: ", total2)
