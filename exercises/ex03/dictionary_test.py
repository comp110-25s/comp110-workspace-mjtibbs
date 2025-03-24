"""Dictionary functions test."""

__author__: str = "730676720"

from exercises.ex03.dictionary import invert, favorite_color, count, bin_len


def test_invert():
    """Testing the use case of the function."""
    assert invert({"a": "z", "b": "y", "c": "x"}) == ({"z": "a", "y": "b", "x": "c"})


def test_invert_2():
    """Testing the use case of the function."""
    assert invert({"cat": "apple"}) == ({"apple": "cat"})


def test_dublicate():
    """Testing the edge case of the function."""
    assert invert({}) == {}


def test_favorite_color():
    """Testing the use case of the function."""
    assert favorite_color({"Sally": "Purple"}) == "Purple"


def test_favorite_color2():
    """Testing the use case of the function."""
    assert (
        favorite_color({"Sally": "Purple", "Brad": "Purple", "Rachel": "Green"})
        == "Purple"
    )


def test_favorite_color3():
    """Testing the edge case of the function."""
    assert favorite_color({"Sally": "Purple", "Rachel": "Green"}) == "Purple"


def test_count():
    """Testing the use case of the function."""
    assert count(["bambi", "dumbo", "bambi"]) == {
        "bambi": 2,
        "dumbo": 1,
    }


def test_count2():
    """Testing the use case of the function."""
    assert count(["snow white", "cinderella", "sleeping beauty"]) == {
        "snow white": 1,
        "cinderella": 1,
        "sleeping beauty": 1,
    }


def test_count3():
    """Testing the edge case of the function."""
    assert count([]) == {}


def bin_lin():
    """Testing the use case of the function."""
    assert bin_len(["the", "quick", "fox"]) == {3: {"the", "fox"}, 5: {"quick"}}


def bin_lin2():
    """Testing the use case of the function."""
    assert bin_len(["the", "the", "fox"]) == {3: {"the", "fox"}}


def bin_lin3():
    """Testing the edge case of the function."""
    assert bin_len([]) == {}
