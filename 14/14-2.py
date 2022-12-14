with open("./14/14-input.txt", "r") as f:
    d = f.read().split("\n")

# find minx, maxx, miny, maxy
all_x = []
all_y = []

for r in d:
    r = r.split("->")
    all_x = all_x + [int(v[0].strip()) for v in [v.split(",") for v in r]]
    all_y = all_y + [int(v[1].strip()) for v in [v.split(",") for v in r]]

sand_x = 500
sand_y = 0


def draw_grid(grid):
    for row in grid:
        print("".join(row))


minx = min(all_x)
maxx = max(all_x)
miny = min(all_y)
maxy = max(all_y)

# Generate grid

shift_x = (maxx - minx + 1) * 4

rel_sand_x = sand_x - minx
grid = [[] for _ in range(maxy + 3)]
for y in range(maxy + 3):
    for x in range(maxx - minx + 1 + shift_x * 2):
        if y == 0 and x == rel_sand_x + shift_x:
            grid[y].append("+")
        elif y == maxy + 2:
            grid[y].append("#")
        else:
            grid[y].append(".")

print("Generate grid")

# Add rock to grid
for r in d:
    instruction = r.split("->")
    lst_x = lst_y = None
    for step in instruction:
        x, y = [int(v.strip()) for v in step.split(",")]

        x = x + shift_x

        if lst_x is None and lst_y is None:
            lst_x = x
            lst_y = y
            continue

        # Draw from
        dr_x = x - lst_x
        dr_y = y - lst_y

        # Draw vertically
        if dr_y != 0 and dr_x == 0:
            if dr_y > 0:  # Draw downwards
                print(f"[Y] From: {lst_y} Dist: {dr_y} Target: {lst_y + dr_y}")
                for j in range(lst_y, lst_y + dr_y + 1):
                    grid[j][lst_x - minx] = "#"
            if dr_y < 0:  # Draw upwards
                print(f"[Y] From: {lst_y} Dist: {dr_y} Target: {lst_y + dr_y}")
                for j in range(lst_y, lst_y + dr_y - 1, -1):
                    grid[j][lst_x - minx] = "#"

        # Draw horizontally
        if dr_x != 0 and dr_y == 0:
            if dr_x > 0:  # Draw right
                print(f"[X] From: {lst_x - minx} Dist: {dr_x} Target: {lst_x - minx + dr_x}")
                for i in range(lst_x - minx, lst_x - minx + dr_x + 1):
                    grid[lst_y][i] = "#"
            if dr_x < 0:  # Draw left
                print(f"[X] From: {lst_x - minx} Dist: {dr_x} Target: {lst_x - minx + dr_x - 1}")
                for i in range(lst_x - minx, lst_x - minx + dr_x - 1, -1):
                    grid[lst_y][i] = "#"

        # Reassign for next draw
        lst_x = x
        lst_y = y

print("Rocks added")
# draw_grid(grid)


resting_counter = 0
previous_resting_counter = resting_counter


def calculate_sand(grid, sx, sy):
    global resting_counter
    is_resting = False

    while not is_resting:
        try:
            if grid[sy][sx] == "o":
                break

            if grid[sy + 1][sx] not in ("#", "o"):  # Falling down
                sy += 1
            elif grid[sy + 1][sx - 1] == ".":  # attempt one step down and left
                sy += 1
                sx -= 1
            elif grid[sy + 1][sx + 1] == ".":  # attempt one step down and rigt
                sy += 1
                sx += 1
            else:  # Blocked
                grid[sy][sx] = "o"
                resting_counter += 1
                is_resting = True

        except IndexError:  # Out of bounds... Free fall... Break
            break


print("Sanding the shit out of it")
while True:
    previous_resting_counter = resting_counter
    calculate_sand(grid, rel_sand_x + shift_x, 0)
    if resting_counter <= previous_resting_counter:  # not growing
        break

draw_grid(grid)
print("Part 2: ", resting_counter)
