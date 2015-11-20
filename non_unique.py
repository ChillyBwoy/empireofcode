"""
Non Unique

If you have 50 different plug types, appliances wouldn't be available and would
be very expensive. But once an electric outlet becomes standardized, many
companies can design appliances, and competition ensues, creating variety and
better prices for consumers.

-- Bill Gates

You are given a non-empty list of integers (X). For this task, you should
return a list consisting of only the non-unique elements in this list.
To do so you will need to remove all unique elements (elements which are
contained in a given list only once). When solving this task, do not change
the order of the list. Example: [1, 2, 3, 1, 3] 1 and 3 non-unique elements
so the result will be [1, 3, 1, 3].

Input: A list of integers.

Output: The list of integers.

Example:

non_unique([1, 2, 3, 1, 3]) == [1, 3, 1, 3]
non_unique([1, 2, 3, 4, 5]) == []
non_unique([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]
non_unique([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9]
Precondition:

0 < |data| < 1000

Optional Goals

Rank 2:

An array can contain Latin letters. Letters are counted as case insensitive,
so "a" == "A", so in ["d", "D", "A"] only one unique element - "A".

Precondition Rank 2

data contains only numbers or letters (one symbol string).

How it is used:

This mission will help you to understand how to use manipulate arrays, giving
you a foundation for solving more complex tasks. The concept can be easily
generalized for real world tasks. For example; it allows you to clarify data
by removing low frequency elements (noise)."""


def non_unique(data):
    return data


if __name__ == "__main__":
    # These "asserts" using only for self-checking
    # and not necessary for auto-testing
    # Rank 1
    assert isinstance(non_unique([1]), list), "The result must be a list"
    assert non_unique([1, 2, 3, 1, 3]) == [1, 3, 1, 3], "1st example"
    assert non_unique([1, 2, 3, 4, 5]) == [], "2nd example"
    assert non_unique([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "3rd example"
    assert non_unique([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9], "4th example"

    # Rank 2
    assert non_unique(['P', 7, 'j', 'A', 'P', 'N', 'Z', 'i',
                       'A', 'X', 'j', 'L', 'y', 's', 'K', 'g',
                       'p', 'r', 7, 'b']) == ['P', 7, 'j', 'A',
                                              'P', 'A', 'j', 'p', 7], "Letters"

    print("All done? Earn rewards by using the 'Check' button!")
