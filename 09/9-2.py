from dataclasses import dataclass, astuple

with open("./09/9-input.txt", "r") as f:
    data = f.read().split("\n")
    data = [d for d in data if d != ""]


@dataclass
class Pos:
    x: int
    y: int

    def to_tuple(self):
        return astuple(self)


h = Pos(0, 0)
tails = [Pos(0, 0) for x in range(9)]
vp = [(0, 0)]


def move_head(h, d):
    if d == "R":
        h.x += 1
    if d == "L":
        h.x -= 1
    if d == "U":
        h.y += 1
    if d == "D":
        h.y -= 1


def move_tail(h, t):
    if h.y == t.y and h.x > t.x and abs(h.x - t.x) > 1:
        t.x += 1
    elif h.y == t.y and h.x < t.x and abs(h.x - t.x) > 1:
        t.x -= 1
    elif h.x == t.x and h.y > t.y and abs(h.y - t.y) > 1:
        t.y += 1
    elif h.x == t.x and h.y < t.y and abs(h.y - t.y) > 1:
        t.y -= 1

    max_dist = max([abs(h.x - t.x), abs(h.y - t.y)])

    if h.y > t.y and h.x > t.x and max_dist > 1:
        t.x += 1
        t.y += 1

    elif h.y < t.y and h.x > t.x and max_dist > 1:
        t.x += 1
        t.y -= 1

    elif h.y > t.y and h.x < t.x and max_dist > 1:
        t.x -= 1
        t.y += 1

    elif h.y < t.y and h.x < t.x and max_dist > 1:
        t.x -= 1
        t.y -= 1


def render_grid(h, tails):
    """This shit is broken with negative grid values. RIP"""
    max_x = max([h.x, *[t.x for t in tails]])
    max_y = max([h.y, *[t.y for t in tails]])

    rows = []

    for i in range(max_y + 50):
        row = ""
        for j in range(max_x + 50):
            h.x += 25
            h.y += 25
            if h.x == j and h.y == i:
                row += "H"
                continue

            found_tail = False
            for idx, t in enumerate(tails):
                t.x += 25
                t.y += 25
                if t.x == j and t.y == i:
                    row += str(idx + 1)
                    found_tail = True
                    break

            if not found_tail and i == 0 and j == 0:
                row += "s"
                continue

            if not found_tail:
                row += "."
        rows.append(row)

    for row in rows:
        print(row)


for row in data:
    d, n = row.split(" ")

    for iter in range(int(n)):
        move_head(h, d)
        for i in range(len(tails)):
            if i == 0:
                move_tail(h=h, t=tails[i])
            else:
                move_tail(h=tails[i - 1], t=tails[i])
            if i == 8:
                if tails[i].to_tuple() not in vp:
                    vp.append(tails[i].to_tuple())

    # render_grid(h, tails)

print(len(vp))
