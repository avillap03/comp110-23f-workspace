"""EX07 - Testinf Dictionary Functions."""

__author__ = "730621663"

from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


# Tests for invert
def test_invert_empty_dict() -> None:
    """Edge case - empty inp dict - return empty new dict."""
    assert invert([]) == {} 


def test_single_input() -> None: 
    """Use case - testing fucntion with single input pair."""
    test_dict: dict[str, str] = {"Ale": "Peru"}
    assert invert(test_dict) == {"Peru": "Ale"}


def test_multiple_input() -> None:
    """Use case - tetsing function with multiple input pairs."""
    test_dict: dict[str, str] = {"Ale": "Peru", "Nico": "Chile", "Derek": "Mexico"}
    assert invert(test_dict) == {"Peru": "Ale", "Chile": "Nico", "Mexico": "Derek"}


# Tests for favorite_color
def test_favorite_color_empty_dict() -> None:
    """Edge case - empty inp dict - return empty str."""
    assert favorite_color([]) == ""


def test_tie() -> None:
    """Use case - tie in favorite color - return color that appeared first."""
    test_dict: dict[str, str] = {"Ale": "Blue", "Nico": "Red"}
    assert favorite_color(test_dict) == "Blue"


def test_multiple_people_single_color() -> None:
    """Use case - multiple names matched with same color - return color one time."""
    test_dict: dict[str, str] = {"Ale": "Blue", "Nico": "Blue", "Derek": "Blue"}
    assert favorite_color(test_dict) == "Blue"


# Tests for count
def test_empty_list() -> None:
    """Edge case - empty inp list - return empty dict."""
    assert count([]) == {}


def test_unique_inputs() -> None:
    """Use case - testing fucntion with unique inputs."""
    test_list: list[str] = ["Blue", "Red", "Green", "Black"]
    assert count(test_list) == {"Blue": 1, "Red": 1, "Green": 1, "Black": 1}


def test_same_inputs() -> None:
    """Use case - testing fucntion with identical inputs."""
    test_list: list[str] = ["Blue", "Blue", "Blue", "Red", "Red"]
    assert count(test_list) == {"Blue": 3, "Red": 2}


# Tests for alphabetizer
def test_alphabetizer_empty_list() -> None:
    """Edge case - empty inp list - return empty dict."""
    test_list: list[str] = []
    assert alphabetizer(test_list) == {}


def test_duplicate_inputs() -> None:
    """Use case - testing function with duplicated inputs."""
    test_list: list[str] = ["computer", "computer", "science"]
    assert alphabetizer(test_list) == {"c": ["computer", "computer"], "s": ["science"]}


def test_case_sensitive_input() -> None:
    """Use case - testing if function is case sensitive."""
    test_list: list[str] = ["computer", "Computer", "science", "Science"]
    assert alphabetizer(test_list) == {"c": ["computer", "Computer"], "s": ["science", "Science"]}


# Test for update_attendance
def test_update_attendance_empty_dict() -> None:
    """Edge case - empty dict - return empty dict."""
    test_dict: dict[str, list[str]] = {}
    day: str = "Monday"
    name: str = "Ale"
    assert update_attendance(test_dict, day, name) == {"Monday": ["Ale"]}


def test_add_name_existing_day() -> None:
    """Edge case - testing function for adding a new name to an existing day."""
    test_dict: dict[str, list[str]] = {"Monday": ["Ale"]}
    day: str = "Monday"
    name: str = "Nico"
    assert update_attendance(test_dict, day, name) == {"Monday": ["Ale", "Nico"]}


def test_add_existing_name_new_day() -> None:
    """Edge case - testing function for adding an existing aname to an new day."""
    test_dict: dict[str, list[str]] = {"Monday": ["Ale", "Nico"]}
    day: str = "Friday"
    name: str = "Nico"
    assert update_attendance(test_dict, day, name) == {"Monday": ["Ale", "Nico"], "Friday": ["Nico"]}