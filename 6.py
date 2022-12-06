with open("6-input.txt", "r") as f:
    d = f.read().split("\n")


def solve(d, n):
    total = 0
    for row in d:
        for i in range(n, len(row)):
            m = row[i - n : i]
            l = len(set(m))
            if l == n:
                total += i
                break
    return total


print(solve(d, 4))
print(solve(d, 14))
