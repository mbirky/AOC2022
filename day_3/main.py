import os


def parse():
    lines = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path + "/input.txt", "r") as f:
        for line in f:
            lines.append(line)

    return lines


def item_priority(item):
    priority = ord(item.lower()) - 96
    if item.isupper():
        priority += 26

    return priority


def partOne(input):
    priority_sum = 0

    for rucksack in input:
        first_compartment = rucksack[: int(len(rucksack) / 2)]
        second_compartment = rucksack[int(len(rucksack) / 2) :]

        duplicates = [item for item in first_compartment if item in second_compartment]

        for item in set(duplicates):
            priority_sum += item_priority(item)

    return priority_sum


def partTwo(input):
    badge_sum = 0

    for index in range(0, len(input), 3):
        for item in input[index]:
            if item in input[index + 1] and item in input[index + 2]:
                badge_sum += item_priority(item)
                break

    return badge_sum


if __name__ == "__main__":
    input = parse()
    print(f"Part One: {partOne(input)}")
    print(f"Part Two: {partTwo(input)}")
