def number_swapper(first: int, second: int) ->tuple[int, int]:
    return (second, first)

def number_swapper_2(first: int, second: int) ->tuple[int, int]:
    print(first ^ second) # try XOR
    print(second ^ first)
    print(abs(first-second))
    print(first ^ abs(first-second))
    print(second ^ abs(first-second)) 
    print(first ^ first-second)
    print(second ^ first-second)    
    return (second, first)

def test_number_swapper():
    first = 6
    second = 42
    assert (42, 6) == number_swapper(first, second)
    second = 11
    number_swapper_2(first, second)

if __name__ == "__main__":
    test_number_swapper()
    print("All done!")