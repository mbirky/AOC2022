from main import partOne, partTwo, create_file_structure, sum_folder, sum_folder_sizes

input = [
    "$ cd /",
    "$ ls",
    "dir a",
    "14848514 b.txt",
    "8504156 c.dat",
    "dir d",
    "$ cd a",
    "$ ls",
    "dir e",
    "29116 f",
    "2557 g",
    "62596 h.lst",
    "$ cd e",
    "$ ls",
    "584 i",
    "$ cd ..",
    "$ cd ..",
    "$ cd d",
    "$ ls",
    "4060174 j",
    "8033020 d.log",
    "5626152 d.ext",
    "7214296 k",
]


def test_create_file_structure():
    assert create_file_structure(input) == {
        "a": {
            "e": {
                "i": 584,
            },
            "f": 29116,
            "g": 2557,
            "h.lst": 62596,
        },
        "b.txt": 14848514,
        "c.dat": 8504156,
        "d": {
            "j": 4060174,
            "d.log": 8033020,
            "d.ext": 5626152,
            "k": 7214296,
        },
    }


def test_sum_folder():
    root = create_file_structure(input)
    assert sum_folder(root["a"]) == 94853


def test_sum_folder_sizes():
    root = create_file_structure(input)
    assert sum_folder_sizes(root) == {"a": 94853, "d": 24933642, "e": 584}


def test_partOne():
    assert partOne(input) == 95437


def test_partTwo():
    assert partTwo(input) == 24933642
