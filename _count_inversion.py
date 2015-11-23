"""
Count Inversion

All units should be numbered and the order is very important. But how do we
deal with and measure irregularities?

In computer science and discrete mathematics, an inversion is a pair of places
in a sequence where the elements in these places are out of their natural
order. So, if we use ascending order for a group of numbers, then an inversion
is when the order is reversed and larger numbers appear before lower number in
a sequence.

Check out this example sequence: (1, 2, 5, 3, 4, 7, 6) and we can see here
three inversions:

5 and 3;
5 and 4;
7 and 6.
You are given a sequence of unique numbers and you should count the number of
inversions in this sequence.

Input: A sequence as a tuple of integers.

Output: The inversion number as an integer.

Example:

count_inversion((1, 2, 5, 3, 4, 7, 6)) == 3
count_inversion((0, 1, 2, 3)) == 0
Precondition:

2 < |sequence| < 200

All elements of a sequence are unique.

How it is used:

In this mission you will experience the wonder of nested loops, that is of
course supposing you don't use advanced algorithms or black magic.

Repository
https://github.com/Checkio-Game-Missions/checkio-empire-count-inversion.git
"""


def count_inversion(sequence):
    if not len(sequence):
        return 0
    new_seq = [x for x in sequence if x < sequence[0]]
    return len(new_seq) + count_inversion(sequence[1:])


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert count_inversion((1, 2, 5, 3, 4, 7, 6)) == 3, "Example"
    assert count_inversion((0, 1, 2, 3)) == 0, "Sorted"
    assert count_inversion((99, -99)) == 1, "Two numbers"
    assert count_inversion((5, 3, 2, 1, 0)) == 10, "Reversed"
    print("Code's finished? Earn rewards by clicking 'Check' to review your tests!")
