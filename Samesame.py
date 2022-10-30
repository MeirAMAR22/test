"""
This program prints the product of all numbers in a list
"""


def samesame(my_list):
    """ This function sums the members of a list"""
    # Let's say that all the variables on the list have the same type
    results = my_list[0]
    for i in my_list[1:]:
        results = results + i
    return results


def test(my_result, expected):
    """ simple test() function used in main() to print
        what each function returns vs. what it's supposed to return. """
    if my_result == expected:
        prefix = " OK "
    else:
        prefix = "  X "
    print(f"{prefix} : You obtain {my_result} and {expected} was attempt")


def main():
    """ main() calls the above functions with interesting inputs,
        using test() to check if each result is correct or not. """
    test(samesame([2, 4, 5]), 11)
    test(samesame(['a', 'b', 'c']), 'abc')
    test(samesame([[3, 2], [4, 5]]), [3, 2, 4, 5])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
