with open("./10/10-input.txt", "r") as f:
    d = f.read().split("\n")


def calc_operations(d, m, c=0):
    """Calc operations for the program d=data, m=moves c=counter"""
    for r in d:
        if r == "noop":
            c += 1
            continue
        i, v = r.split(" ")
        if "add" in i:
            m[c + 2] = (i, v)
            c += 2


def slv(m, x, ss, o):
    """Solves the puzzle m=moves, x=list of all values ss=list of solutions at intervals"""
    for c in range(1, max(m) + 1):
        if c in m:
            i, v = m[c]
        if c in [20, 60, 100, 140, 180, 220]:
            s = sum(x)
            ss.append(c * s)
        o[c] = sum(x)
        if c in m:
            x.append(int(v))


def draw(o, crt_w):
    """Draws the CRT monitor for part two"""
    c = 1

    while c < max(o):
        r = ""
        for w in range(crt_w):
            try:
                x = o[c]
                d = abs(x - w)
                if d <= 1:
                    r += "#"
                else:
                    r += "."
                c += 1
            except KeyError:
                pass
        print(r)


x = [1]
m = {}
ss = []
o = {}

calc_operations(d, m)
slv(m, x, ss, o)

print("Part 1: ", sum(ss))

crt_w = 40

print("Part 2:")
draw(o, crt_w)
