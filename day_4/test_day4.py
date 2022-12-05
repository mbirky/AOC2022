from main import partOne, partTwo

input = [
    "2-4,6-8",
    "2-3,4-5",
    "5-7,7-9",
    "2-8,3-7",
    "6-6,4-6",
    "2-6,4-8",
]


def test_partOne():
    assert partOne(input) == 2


def test_partTwo():
    assert partTwo(input) == 4
