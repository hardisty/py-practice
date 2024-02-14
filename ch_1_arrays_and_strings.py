def is_unique(input: str) -> bool:
    """
    Determine if all characters in a string are unique.
    Clarification: Is string UTF-8 encoded?
    Strategy: Use Python Set

    Args:
        input: String to test

    Returns:
        True if there are no repeat characters, False otherwise

    """
    chars = set()
    for char in input:
        if char in chars:
            return False
        chars.add(char)
    return True


def test_is_unique():
    input_1 = "bir"
    input_2 = "birb"
    assert is_unique(input_1) == True
    assert is_unique(input_2) == False


def is_permutation(str_1: str, str_2: str) -> bool:
    """
    Determine if two strings are permutations of each other.

    Clarification:
        Are uppercase and lowercase distict?
        Is it OK to use Python's built-in List?

    Strategy:
        Turn strings into lists, sort, and compare.

    Args:
        str_1: First string to compare
        str:2: Second string to compare

    Returns:
        True if strings contain the same characters, False otherwise
    """

    if sorted(list(str_1)) == sorted(list(str_2)):
        return True
    return False


def test_is_permutation():
    input_1 = "birb"
    input_2 = "bbir"
    input_3 = "bird"

    assert is_permutation(input_1, input_2)
    assert is_permutation(input_1, input_3) == False


if __name__ == "__main__":
    test_is_unique()
    test_is_permutation()
    print("all done!")
