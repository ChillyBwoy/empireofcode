"""
Triangle Angles

Most of the facets on a crystal are triangle. Since these crystals are vital to
our base, we should attempt to learn more about this shape.

You are given the lengths for each side of a triangle. You need to find all
three of the angles for this triangle. If the given side lengths cannot form a
triangle (or form a degenerated triangle), then you must return all angles as
0 (zero). The angles should be represented as a list of integers in ascending
order. Each angle is measured in degrees and rounded to the nearest integer
number using standard mathematical rounding.

Input: The lengths of the sides of a triangle as integers.

Output: Angles of a triangle in degrees as sorted list of integers.

Example:

angles(4, 4, 4) == [60, 60, 60]
angles(3, 4, 5) == [37, 53, 90]
angles(2, 2, 5) == [0, 0, 0]
Precondition:

0 < a ≤ 1000

0 < b ≤ 1000

0 < c ≤ 1000

How it is used:

This is a classical geometry problem. With this concept you can measure an
angle without the need for a protractor for use in fields such as topography or
architecture.

Repository
https://github.com/Checkio-Game-Missions/checkio-empire-triangle-angles.git
"""


from math import acos, pi


def angles(a, b, c):
    p1 = a + b > c
    p2 = b + c > a
    p3 = a + c > b

    if not p1 or not p2 or not p3:
        return [0, 0, 0]

    alpha = round(acos((b**2 + c**2 - a**2) / (2.0 * b * c)) * 180.0 / pi)
    beta = round(acos((a**2 + c**2 - b**2) / (2.0 * a * c)) * 180.0 / pi)

    return sorted([alpha, beta, 180 - (alpha + beta)])


if __name__ == '__main__':
    # These "asserts" using only for self-checkingand not necessary for
    # auto-testing
    assert angles(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert angles(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert angles(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"

    print("Code's finished? Earn rewards by clicking 'Check' to review your tests!")
