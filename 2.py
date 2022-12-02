with open("2-input.txt", "r") as f:
    d = f.read().split("\n")


def score1(l):
    elf, me = l

    # rock
    if elf == "A" and me == "X":
        return 4  # rock + draw
    if elf == "B" and me == "X":
        return 1  # rock + lost
    if elf == "C" and me == "X":
        return 7  # rock + win

    # paper
    if elf == "A" and me == "Y":
        return 8  # paper + win
    if elf == "B" and me == "Y":
        return 5  # paper + draw
    if elf == "C" and me == "Y":
        return 2  # paper + loss

    # scissor
    if elf == "A" and me == "Z":
        return 3  # scissor + loss
    if elf == "B" and me == "Z":
        return 9  # scissor + win
    if elf == "C" and me == "Z":
        return 6  # scissor + draw


def score2(l):
    elf, me = l

    # Lose
    if elf == "A" and me == "X":
        return 3
    if elf == "B" and me == "X":
        return 1
    if elf == "C" and me == "X":
        return 2

    # Draw
    if elf == "A" and me == "Y":
        return 4
    if elf == "B" and me == "Y":
        return 5
    if elf == "C" and me == "Y":
        return 6

    # Win
    if elf == "A" and me == "Z":
        return 8
    if elf == "B" and me == "Z":
        return 9
    if elf == "C" and me == "Z":
        return 7


print(sum(list(map(score1, [v.split(" ") for v in d if v != ""]))))
print(sum(list(map(score2, [v.split(" ") for v in d if v != ""]))))
