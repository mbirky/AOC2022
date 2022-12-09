import os


def parse():
    lines = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path + "/input.txt", "r") as f:
        for line in f:
            lines.append(line)

    return lines


def is_each_element_unique(list):
    return len(list) == len(set(list))


def partOne(input):
    signal = input[0]
    for index in range(4, len(signal)):
        possible_marker = signal[index - 4 : index]
        if is_each_element_unique(possible_marker):
            return index
    return 0


def partTwo(input):
    signal = input[0]
    for index in range(14, len(signal)):
        possible_message = signal[index - 14 : index]
        if is_each_element_unique(possible_message):
            return index
    return 0


if __name__ == "__main__":
    input = parse()
    print(f"Part One: {partOne(input)}")
    print(f"Part Two: {partTwo(input)}")
