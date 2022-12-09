import os


def parse():
    lines = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path + "/input.txt", "r") as f:
        for line in f:
            lines.append(line)

    return lines


def create_file_structure(input):
    root = {}

    current_dir = root
    path = [current_dir]

    # Skip first line which is `cd /`
    for line in input[1:]:
        if line == "ls":
            continue
        elif line.split()[0] == "dir":
            current_dir[line.split()[1]] = {}
        elif line.split()[0].isnumeric():
            current_dir[line.split()[1]] = int(line.split()[0])
        elif line.split()[1] == "cd":
            if line.split()[2] == "..":
                current_dir = path[-1]
                path.pop(-1)
            else:
                path.append(current_dir)
                current_dir = current_dir.get(line.split()[2])

    return root


def sum_folder(folder):
    sum = 0

    for key, value in folder.items():
        if type(value) == int:
            sum += value
        else:
            sum += sum_folder(folder[key])

    return sum


def sum_of_folders_under_limit(folders, limit=100000):
    sum = 0

    for key, value in folders.items():
        if type(value) != int:
            folder_sum = sum_folder(folders[key])
            if folder_sum < 100000:
                sum += folder_sum
            sum += sum_of_folders_under_limit(folders[key], limit)

    return sum


def partOne(input):
    root = create_file_structure(input)

    return sum_of_folders_under_limit(root)


def find_lowest_folder_size_over_limit(folders, limit):
    for key, value in folders.items():
        if type(value) != int:
            folder_sum = sum_folder(folders[key])
            if folder_sum > limit:
                lowest_sub_folder = find_lowest_folder_size_over_limit(
                    folders[key], limit
                )
                if lowest_sub_folder > limit:
                    return lowest_sub_folder
                return folder_sum
    return 0


def partTwo(input):
    root = create_file_structure(input)

    total_disk_space_available = 70000000
    unused_disk_space_needed = 30000000
    currently_unused_disk_space = total_disk_space_available - sum_folder(root)
    additional_required_disk_space = (
        unused_disk_space_needed - currently_unused_disk_space
    )

    return find_lowest_folder_size_over_limit(root, additional_required_disk_space)


if __name__ == "__main__":
    input = parse()
    print(f"Part One: {partOne(input)}")
    print(f"Part Two: {partTwo(input)}")
