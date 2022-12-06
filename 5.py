with open("5-input.txt", "r") as f:
    d = f.read().split("\n")

stack_data, moves = d[: d.index("")], d[d.index("") :]
no_stacks = stack_data.pop()

# Find number of stacks
for c in reversed(no_stacks):
    if c.replace(" ", "") != "":
        l = int(c)
        break

# Generate stack
stacks = {i: [] for i in range(1, l + 1, 1)}
for row in reversed(stack_data):
    for i in range(0, len(row) // 4 + 1):
        v = row[:4]
        v = v.replace(" ", "")
        if len(v) != 0:
            stacks[i + 1].append(v)
        row = row[4:]

# re-arrange
for instruction in moves:
    if len(instruction) == 0:
        continue
    instruction = instruction.split(" ")
    n, f, t = instruction[1], instruction[3], instruction[5]

    # THIS IS FOR PART 1
    # for _ in range(0, int(n)):
    #     c = stacks[int(f)].pop()
    #     stacks[int(t)].append(c)

    # THIS IS FOR PART 2
    c = stacks[int(f)][-int(n) :]
    stacks[int(t)] = stacks[int(t)] + c
    stacks[int(f)] = stacks[int(f)][: -int(n)]

# Joining together
print("final: ", "".join([v.pop() for v in stacks.values() if len(v) != 0]).replace("[", "").replace("]", ""))
