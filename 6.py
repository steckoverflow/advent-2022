with open("6-input.txt", "r") as f:
    d = f.read().split("\n")


def solve(d, n):
    t = 0
    for r in d:
        for i in range(n, len(r)):
            m = r[i - n : i]
            l = len(set(m))
            if l == n:
                t += i
                break
    return t


print(solve(d, 4))
print(solve(d, 14))
