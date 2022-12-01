import os


def parse():
    lines = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path + "/input.txt", "r") as f:
        for line in f:
            lines.append(line)

    return lines


def partOne(input):
    elf_calories = []

    current_elf_calories = 0
    for item in input:
        if item == "\n":
            elf_calories.append(current_elf_calories)
            current_elf_calories = 0
        else:
            current_elf_calories += int(item)
    elf_calories.append(current_elf_calories)

    return max(elf_calories)


def partTwo(input):
    elf_calories = []

    current_elf_calories = 0
    for item in input:
        if item == "\n":
            elf_calories.append(current_elf_calories)
            current_elf_calories = 0
        else:
            current_elf_calories += int(item)
    elf_calories.append(current_elf_calories)

    return sum(sorted(elf_calories, reverse=True)[0:3])


if __name__ == "__main__":
    input = parse()
    print(f"Part One: {partOne(input)}")
    print(f"Part Two: {partTwo(input)}")
