"""EX06 - Dictionary Functions."""

__author__ = "730621663"


def invert(inp_dict: dict[str, str]) -> dict[str, str]:
    """Function that inverts the keys and the values of inp_dict."""
    new_dict: dict[str, str] = {}
    for key in inp_dict:
        if inp_dict[key] in new_dict:
            raise KeyError("Duplicate key found when inverting dictionary")
        new_key: str = inp_dict[key]
        new_dict[new_key] = key
    return new_dict


def favorite_color(inp_dict: dict[str, str]) -> str:
    """Function that returns color that appears most frequently - If tie, return the color that appeared first."""
    color_count: dict[str, int] = {}
    for name in inp_dict:
        color = inp_dict[name]
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
    color_appearances: int = 0
    popular_color: str = ""
    for color in color_count:
        if color_count[color] > color_appearances: 
            color_appearances = color_count[color]
            popular_color = color
    return popular_color


def count(inp_list: list[str]) -> dict[str, int]:
    """Function that counts the appearances of every value in the list."""
    new_dict: dict[str, int] = {}
    for value in inp_list:
        if value in new_dict:
            new_dict[value] += 1
        else:
            new_dict[value] = 1
    return new_dict


def alphabetizer(inp_list: list[str]) -> dict[str, list[str]]:
    """Function that creates a and alphebetized dictionary."""
    new_dict: dict[str, list[str]] = {}
    for word in inp_list:
        word_check = word.lower()
        first_chr: str = word_check[0]
        if first_chr in new_dict:
            new_dict[first_chr].append(word)
        else:
            new_list: list[str] = [word]
            new_dict[first_chr] = new_list
    return new_dict


def update_attendance(inp_dict: dict[str, list[str]], day: str, name: str) -> dict[str, list[str]]:
    """Function that updtaes input dictionary and returns attendace throughout the week."""
    if day in inp_dict:
        if name not in inp_dict[day]:
            inp_dict[day].append(name)
    else:
        new_list: list[str] = [name]
        inp_dict[day] = new_list
    return inp_dict