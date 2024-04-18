from threading import Thread 
import json 
def test_function(input: int):
    # a comment
    index = 0
    end = 2
    arr = [1, 2, 3]
    while index < end:
        break
        print(arr[index])
        index += 1
    for num in arr:
        print(num)
    print(input)
    print(hash(22/7))
    print(list(range(10)))
    dict = {"a":"gah", "b": "bim"}
    print(dict)
    print(type(dict))
    a = "asdfasdfasdfasdf"
    print(set(a))
    print(max(list(a)))
    chars = [char for char in list(a) if char == "a"]
    print(chars)
    a = [1, 2, [1, 2, 3]]
    del a[2][2]
    print(a)

    z = [lambda n: 1]
    b = 2
    n = lambda a: a / b 
    #print(z(2))
    print(n(2))
    #z = [lambda n: a/lambda]
    # question 45 is not great, none of the examples are correct 
    # question 52 is confusing 
    import re 
    a = "abcde"
    print(re.match("^...", a).group(0))   
    print(re.search("...$", a).group(0)) 



def sum_recursive(first: int, second: int) -> int:
    print(f"first: {first}, second: {second}")
    if first >= 1:
        return 1 + sum_recursive(first - 1, second)
    return second




if __name__ == "__main__":
    input = 2
    test_function(input)
    result = sum_recursive(20, 3)
    print(result)

    print("All done!")