with open("./08/8-input.txt", "r") as f:
    d = f.read().split("\n")

d = d[:-1]

cls = len(d[0])
rws = len(d)

t = cls * 2 + rws * 2 - 4

for y in range(1, rws - 1):
    for x in range(1, cls - 1):
        c = int(d[y][x])

        if c > max([int(v) for v in list(d[y])[:x]]):  # left
            t += 1
            continue

        if c > max([int(v) for v in list(d[y])[x + 1 :]]):  # right
            t += 1
            continue

        if c > max([int(r[x]) for r in d[:y]]):  # top
            t += 1
            continue

        if c > max([int(r[x]) for r in d[y + 1 :]]):  # bottom
            t += 1

print("Part 1: ", t)

cls = len(d[0])
rws = len(d)

msc = 0

for y in range(rws):
    for x in range(cls):
        c = int(d[y][x])

        l = [int(v) for v in list(d[y])[:x]]
        ls = 0
        for v in l[::-1]:
            ls += 1
            if v >= c:
                break

        r = [int(v) for v in list(d[y])[x + 1 :]]
        rs = 0
        for v in r:
            rs += 1
            if v >= c:
                break

        t = [int(r[x]) for r in d[:y]]
        ts = 0
        for v in t[::-1]:
            ts += 1
            if v >= c:
                break

        b = [int(r[x]) for r in d[y + 1 :]]
        bs = 0
        for v in b:
            bs += 1
            if v >= c:
                break

        sc = ls * rs * ts * bs
        if sc > msc:
            msc = sc

print("Part 2: ", msc)
