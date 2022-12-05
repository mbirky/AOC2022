from main import partOne, partTwo, rps_outcome

input = [
    "A Y",
    "B X",
    "C Z",
]


def test_rps_outcomes():
    assert rps_outcome("Rock", "Rock") == "Draw"
    assert rps_outcome("Rock", "Scissors") == "Loss"
    assert rps_outcome("Paper", "Rock") == "Loss"
    assert rps_outcome("Paper", "Scissors") == "Win"


def test_partOne():
    assert partOne(input) == 15


def test_partTwo():
    assert partTwo(input) == 12
