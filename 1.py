with open("1-input.txt", "r") as f:
    d = f.read()

c = [sum([int(c) for c in v.split("\n") if c != ""]) for v in d.split("\n\n")]

print("1-1:")
print(max(c))

print("1-2:")
c.sort(reverse=True)
print(sum(c[:3]))
