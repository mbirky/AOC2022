from main import partOne, partTwo, parse_input, create_stacks, parse_command

input = [
    "    [D]    \n",
    "[N] [C]    \n",
    "[Z] [M] [P]\n",
    " 1   2   3 \n",
    "",
    "move 1 from 2 to 1",
    "move 3 from 1 to 3",
    "move 2 from 2 to 1",
    "move 1 from 1 to 2",
]


def test_parse_input():
    assert parse_input(input) == (
        ["    [D]    \n", "[N] [C]    \n", "[Z] [M] [P]\n"],
        [
            "move 1 from 2 to 1",
            "move 3 from 1 to 3",
            "move 2 from 2 to 1",
            "move 1 from 1 to 2",
        ],
        3,
    )


def test_create_stacks():
    rows, _, number_of_stacks = parse_input(input)
    assert create_stacks(rows, number_of_stacks) == [["Z", "N"], ["M", "C", "D"], ["P"]]


def test_parse_command():
    _, commands, _ = parse_input(input)
    assert parse_command(commands[0]) == (1, 1, 0)


def test_partOne():
    assert partOne(input) == "CMZ"


def test_partTwo():
    assert partTwo(input) == "MCD"
