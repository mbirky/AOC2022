from main import partOne, partTwo

input = [
    "1000",
    "2000",
    "3000",
    "\n",
    "4000",
    "\n",
    "5000",
    "6000",
    "\n",
    "7000",
    "8000",
    "9000",
    "\n",
    "10000",
]


def test_partOne():
    assert partOne(input) == 24000


def test_partTwo():
    assert partTwo(input) == 45000
