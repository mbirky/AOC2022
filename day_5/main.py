import os


def parse():
    lines = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path + "/input.txt", "r") as f:
        for line in f:
            lines.append(line)

    return lines


def parse_input(input):
    rows = []
    commands = []
    number_of_stacks = 0

    command_lines = False
    for line in input:
        if not line.strip():
            continue

        if line[1] == "1":
            number_of_stacks = int(line[-3])
            command_lines = True
            continue

        if command_lines:
            commands.append(line)
        else:
            rows.append(line)

    return rows, commands, number_of_stacks


def create_stacks(rows, number_of_stacks):
    stacks = [[] for _ in range(number_of_stacks)]

    # start at bottom and work up
    for row in rows[::-1]:
        for stack in range(number_of_stacks):
            stack_character = row[1 + stack * 4]
            if stack_character != " ":
                stacks[stack].append(stack_character)

    return stacks


def parse_command(command):
    split_command = command.split()
    move_count = int(split_command[1])
    from_stack = int(split_command[3]) - 1
    to_stack = int(split_command[5]) - 1

    return move_count, from_stack, to_stack


def partOne(input):
    rows, commands, number_of_stacks = parse_input(input)

    stacks = create_stacks(rows, number_of_stacks)

    # parse and execute commands
    for command in commands:
        move_count, from_stack, to_stack = parse_command(command)

        for _ in range(move_count):
            stacks[to_stack].append(stacks[from_stack][-1])
            stacks[from_stack].pop(-1)

    return "".join([stack[-1] for stack in stacks])


def partTwo(input):
    rows, commands, number_of_stacks = parse_input(input)

    stacks = create_stacks(rows, number_of_stacks)

    # parse and execute commands
    for command in commands:
        move_count, from_stack, to_stack = parse_command(command)

        for item in stacks[from_stack][move_count * -1 :]:
            stacks[to_stack].append(item)

        stacks[from_stack] = stacks[from_stack][: move_count * -1]

    return "".join([stack[-1] for stack in stacks])


if __name__ == "__main__":
    input = parse()
    print(f"Part One: {partOne(input)}")
    print(f"Part Two: {partTwo(input)}")
