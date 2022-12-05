import os


def parse():
    lines = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path + "/input.txt", "r") as f:
        for line in f:
            lines.append(line)

    return lines


def parse_pair(pair):
    assignments = pair.split(",")
    left = [int(i) for i in assignments[0].split("-")]
    right = [int(i) for i in assignments[1].split("-")]

    return left, right


def partOne(input):
    fully_contained_assignments = 0

    for pair in input:
        left, right = parse_pair(pair)

        if (right[0] >= left[0] and right[1] <= left[1]) or (
            left[0] >= right[0] and left[1] <= right[1]
        ):
            fully_contained_assignments += 1

    return fully_contained_assignments


def partTwo(input):
    overlapping_assignments = 0

    for pair in input:
        left, right = parse_pair(pair)

        if (left[0] >= right[0] and left[0] <= right[1]) or (
            right[0] >= left[0] and right[0] <= left[1]
        ):
            overlapping_assignments += 1

    return overlapping_assignments


if __name__ == "__main__":
    input = parse()
    print(f"Part One: {partOne(input)}")
    print(f"Part Two: {partTwo(input)}")
