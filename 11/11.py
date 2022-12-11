with open("./11/11-input.txt", "r") as f:
    d = f.read().split("\n\n")


def monkey_mult_func(x, y):
    if x == "old":
        return y * y
    else:
        return int(x) * y


def monkey_add_func(x, y):
    if x == "old":
        return y + y
    else:
        return int(x) + y


ops = {"*": monkey_mult_func, "+": monkey_add_func}


class Monkey:
    lcd = None

    def __init__(self, id, items, operation, divisble_by, if_true, if_false) -> None:
        self.id = id
        self.items = [*items]
        self.operation = operation
        self.divisble_by = divisble_by
        self.if_true = if_true
        self.if_false = if_false
        self.inspected = 0

    def inspect_items(self):
        itp = []
        while self.items:
            item = self.items.pop(0)
            # print(f"Monkey instects item: {item}")
            self.inspected += 1
            o, m = self.operation.split(" ")
            niv = ops[o](m, item)

            # print(f"New worry level: {niv}")
            # niv = niv // 3
            # nv = niv % int(self.divisble_by)
            # if niv % int(self.divisble_by) == 0:

            itp.append(
                (
                    niv % Monkey.lcd,
                    self.if_true.strip() if niv % int(self.divisble_by) == 0 else self.if_false.strip(),
                )
            )
        return itp

    def __repr__(self) -> str:
        return f"<Monkey Id={self.id} Items=[{','.join([str(s) for s in self.items])}]>"


monkeys = {}

# Process input
for mi, m in enumerate(d):
    m = m.split("\n")
    monkey = {}
    for i in range(len(m)):
        v = m[i]
        match i:
            case 1:
                monkey["items"] = [int(x.strip()) for x in v[v.index(":") + 1 :].split(",")]
            case 2:
                monkey["operation"] = v[v.index(": new = old ") + 12 :]
            case 3:
                monkey["divisble_by"] = v[v.index("Test: divisible by ") + 19 :]
            case 4:
                monkey["if_true"] = v[v.index("If true: throw to monkey ") + 25 :]
            case 5:
                monkey["if_false"] = v[v.index("If false: throw to monkey ") + 25 :]

    monkeys[mi] = Monkey(id=mi, **monkey)

from time import time

start = time()

import math

monkey_dividers = [int(m.divisble_by) for m in monkeys.values()]
lcd = math.lcm(*monkey_dividers)
Monkey.lcd = lcd

# Compute rounds
for n in range(0, 10_000):
    if n % 100 == 0:
        print(time() - start)
        print("Round ", n)
        print([m.inspected for m in monkeys.values()])

    for i, monkey in monkeys.items():
        items_to_pass = monkey.inspect_items()
        for item in items_to_pass:
            iv, mi = item
            monkeys[int(mi)].items.append(iv)

# Active monkeys
am = sorted([m.inspected for m in monkeys.values()])[-2:]
m1, m2 = am
print("Part 2: ", m1 * m2)
