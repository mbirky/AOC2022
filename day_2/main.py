import os


rps_options = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors",
}

options_scores = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3,
}

game_scores = {
    "Loss": 0,
    "Draw": 3,
    "Win": 6,
}


def parse():
    lines = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path + "/input.txt", "r") as f:
        for line in f:
            lines.append(line)

    return lines


def rps_outcome(opponent_shape, my_shape):
    if opponent_shape == my_shape:
        return "Draw"
    if (
        (opponent_shape == "Rock" and my_shape == "Scissors")
        or (opponent_shape == "Paper" and my_shape == "Rock")
        or (opponent_shape == "Scissors" and my_shape == "Paper")
    ):
        return "Loss"
    return "Win"


def partOne(input):
    score = 0
    for round in input:
        opponent_shape = rps_options[round[0]]
        my_shape = rps_options[round[2]]

        outcome = rps_outcome(opponent_shape, my_shape)

        score += options_scores[my_shape] + game_scores[outcome]

    return score


required_outcomes = {
    "X": "Loss",
    "Y": "Draw",
    "Z": "Win",
}

wins_against = {
    "Rock": "Scissors",
    "Paper": "Rock",
    "Scissors": "Paper",
}

losses_against = {
    "Rock": "Paper",
    "Paper": "Scissors",
    "Scissors": "Rock",
}


def partTwo(input):
    score = 0
    for round in input:
        opponent_shape = rps_options[round[0]]
        required_outcome = required_outcomes[round[2]]

        score += game_scores[required_outcome]

        if required_outcome == "Loss":
            score += options_scores[wins_against[opponent_shape]]
        elif required_outcome == "Draw":
            score += options_scores[opponent_shape]
        else:
            score += options_scores[losses_against[opponent_shape]]

    return score


if __name__ == "__main__":
    input = parse()
    print(f"Part One: {partOne(input)}")
    print(f"Part Two: {partTwo(input)}")
