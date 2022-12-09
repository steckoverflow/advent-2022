from dataclasses import dataclass, astuple

with open("./09/9-input.txt", "r") as f:
    data = f.read().split("\n")

data = data[:-1]


@dataclass
class Pos:
    x: int
    y: int

    def to_tuple(self):
        return astuple(self)


h = Pos(0, 0)
t = Pos(0, 0)
vp = [(0, 0)]  # starting pos included


def execute_move(h, t, d, v):
    pass


def render_grid(h, t):
    max_x = max([h.x, t.x])
    max_y = max([h.y, t.y])

    for i in range(max_y + 1):
        r = ""
        for j in range(max_x + 1):
            if h.x == j and h.y == i:
                r += "H"
                continue
            if t.x == j and t.y == i:
                r += "T"
                continue
            r += "."
        print(r)


for row in data:
    d, n = row.split(" ")

    for _ in range(int(n)):

        # First thing first let's move head
        if d == "R":
            h.x += 1
        if d == "L":
            h.x -= 1
        if d == "U":
            h.y += 1
        if d == "D":
            h.y -= 1

        # Calculate tail movement
        # Otherwise, if the head and tail aren't touching and aren't in the same row or column, the tail always moves one step diagonally to keep up:
        # If the head is ever two steps directly up, down, left, or right from the tail, the tail must also move one step in that direction so it remains close enough
        if h.y == t.y and h.x > t.x and abs(h.x - t.x) > 1:
            # print("Tail more than 1 pos behind to the RIGHT -> moving")
            t.x += 1

        elif h.y == t.y and h.x < t.x and abs(h.x - t.x) > 1:
            # print("Tail more than 1 pos behind to the LEFT -> moving")
            t.x -= 1

        elif h.x == t.x and h.y > t.y and abs(h.y - t.y) > 1:
            # print("Tail more than 1 pos behind UPWARDS -> moving")
            t.y += 1

        elif h.x == t.x and h.y < t.y and abs(h.y - t.y) > 1:
            # print("Tail more than 1 pos behind DOWNWARDS -> moving")
            t.y -= 1

        max_dist = max([abs(h.x - t.x), abs(h.y - t.y)])

        # if h.y > t.y and h.x > t.x and abs(h.y - t.y) > 1 and abs(h.x - t.x) > 1:
        if h.y > t.y and h.x > t.x and max_dist > 1:
            # print("Tail more than 1 vert-pos behind UPWARDS and needs to move diagonally right -> moving")
            t.x += 1
            t.y += 1

        elif h.y < t.y and h.x > t.x and max_dist > 1:
            # print("Tail more than 1 vert-pos behind DOWNWARDS and needs to move diagonally right -> moving")
            t.x += 1
            t.y -= 1

        elif h.y > t.y and h.x < t.x and max_dist > 1:
            # print("Tail more than 1 vert-pos behind UPWARDS and needs to move diagonally left -> moving")
            t.x -= 1
            t.y += 1

        elif h.y < t.y and h.x < t.x and max_dist > 1:
            # print("Tail more than 1 vert-pos behind DOWNWARDS and needs to move diagonally left -> moving")
            t.x -= 1
            t.y -= 1

        if t.to_tuple() not in vp:
            vp.append(t.to_tuple())

        print("Iteration: ", _)
        render_grid(h, t)

print(len(vp))
