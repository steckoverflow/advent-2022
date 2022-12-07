with open("7-input.txt", "r") as f:
    d = f.read().split("\n")

dirs = {}
current_path = ""

for cmd in d:
    # Path management
    if "$ cd" in cmd:
        if ".." in cmd:
            new_path = ("/".join([v for v in current_path.split("/")[:-1]])).replace("//", "/")
            current_path = new_path
            continue
        dir = cmd.split(" ")[-1]
        current_path = (current_path + "/" + dir).replace("//", "/")
        if current_path not in dirs:
            dirs[current_path] = []
        continue

    # If we do ls just continue
    if "$ ls" in cmd:
        continue

    # Add file sum or dir to path index
    if cmd.split(" ")[0].isdigit():
        dirs[current_path].append(int(cmd.split(" ")[0]))
    else:
        dir = cmd.split(" ")[-1]
        np = (current_path + "/" + dir).replace("//", "/")
        dirs[current_path].append(np)

res = {}


def flatten(l, d):
    t = 0
    for v in l:
        if type(v) is int:
            t += v
        else:
            t += flatten(dirs[v], d)
    return t


for key, value in dirs.items():
    s = flatten(value, dirs)
    res[key] = s


print("Part 1: ", sum([v for v in res.values() if v <= 100_000]))

s = [(v, k) for k, v in res.items()]
s.sort()

root_dir_size = s[-1][0]

size_left = 70_000_000 - root_dir_size
threshhold = 30_000_000 - size_left

for item in s:
    v, k = item
    if v >= threshhold:
        print("Part 2: ", v)
        break
