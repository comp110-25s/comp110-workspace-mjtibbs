"""Dictionary functions exercise."""

__author__: str = " 730676720"


def invert(input_0: dict[str, str]) -> dict[str, str]:
    """Will invert the given values and set of the dictionary."""
    output: dict[str, str] = {}

    for key in input_0:
        value = input_0[key]
        if value in output:
            raise KeyError("Will duplicate the value of dictionary.")
        output[value] = key

    return output


def count(input_1: list[str]) -> dict[str, int]:
    """Will count the number of times a value will appear."""
    output: dict[str, int] = {}

    for item in input_1:
        if item in output:
            output[item] += 1
        else:
            output[item] = 1

    return output


def favorite_color(colors: dict[str, str]) -> str:
    """Will give the names of each person's favorite color."""
    favorites = []

    for key in colors:
        favorites.append(colors[key])
    number_colors = count(favorites)
    highest_number = 0
    most_common = ""

    for key in colors:
        color = colors[key]
        if number_colors[color] > highest_number:
            highest_number = number_colors[color]
            most_common = color

    return most_common


def bin_len(words: list[str]) -> dict[int, set[str]]:
    """Gives length of dictionary."""
    output: dict[int, set[str]] = {}

    for word in words:
        length_of_word = len(word)

        if length_of_word not in output:
            output[length_of_word] = set()

        output[length_of_word].add(word)

    return output
