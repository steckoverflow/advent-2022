with open("6-input.txt", "r") as f:
    d = f.read().split("\n")


def solve(d, n):
    t = 0
    for r in d:
        for i in range(n, len(r)):
            if len(set(r[i - n : i])) == n:
                t += i
                break
    return t


print("Part 1: ", solve(d, 4))
print("Part 2: ", solve(d, 14))
