def is_unique(input):
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


if __name__ == "__main__":
    test_is_unique()
    print("all done!")
