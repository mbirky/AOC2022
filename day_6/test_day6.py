from main import partOne, partTwo, is_each_element_unique

part_one_inputs = [
    [
        "mjqjpqmgbljsphdztnvjfqwrcgsmlb",
    ],
    [
        "bvwbjplbgvbhsrlpgdmjqwftvncz",
    ],
    [
        "nppdvjthqldpwncqszvftbrmjlhg",
    ],
    [
        "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
    ],
    [
        "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",
    ],
]

part_one_answers = [
    7,
    5,
    6,
    10,
    11,
]


def test_partOne():
    for index, input in enumerate(part_one_inputs):
        assert partOne(input) == part_one_answers[index]


part_two_inputs = [
    [
        "mjqjpqmgbljsphdztnvjfqwrcgsmlb",
    ],
    [
        "bvwbjplbgvbhsrlpgdmjqwftvncz",
    ],
    [
        "nppdvjthqldpwncqszvftbrmjlhg",
    ],
    [
        "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
    ],
    [
        "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",
    ],
]

part_two_answers = [
    19,
    23,
    23,
    29,
    26,
]


def test_partTwo():
    for index, input in enumerate(part_two_inputs):
        assert partTwo(input) == part_two_answers[index]


def test_is_each_element_unique_true():
    unique_chars = "abcd"
    assert is_each_element_unique(unique_chars) == True


def test_is_each_element_unique_false():
    not_unique_chars = "aabc"
    assert is_each_element_unique(not_unique_chars) == False
