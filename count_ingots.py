"""
Count Ingots

To create an accurate accounting of our stock, incoming ingots in cargo
shipments are numbered.

Ingots in each consignment are numbered in the row from A1 to Z9 as
A1, A2,..., A9, B1, B2,..., Z9. Each consignment is marked with the number of
the last ingot in it. So you can define the quantity of ingots by the number
of marks.

You are given a report of daily consignments as number marks written in a
string separated by commas. Count the total quantity of ingots. Take the report
"A2,B1" for example. Here we can see two consignments with 2 (A2) and 10 (B1)
ingots, giving us a result of 12.

Input: A daily report as a string.

Output: The total quantity of ingots as an integer.


count_ingots("A2,B1") == 12
count_ingots("A1,A1,A1") == 3
count_ingots("Z9,X8,Y7") == 672
count_ingots("C1,D1,B1,E1,F1") == 140

(2, 10) = 12
(1, 1, 1) = 3
(26 * 9, 24 * 8, 25 * 7)


1  2  3  4  5  6  7  8  9
10 11 12 13 14 15 16 17 18
19 20 21 22 23 24
"""


from string import ascii_uppercase

LETTERS = list(ascii_uppercase)
NUMBERS = list(range(1, 10))


def ingot(src):
    let, num = tuple(src)
    num = int(num)

    val = LETTERS.index(let) * len(NUMBERS)

    print(src, val, num, val + num)

    return val + num


def count_ingots(report):
    return sum(ingot(r) for r in report.split(','))


if __name__ == '__main__':
    # These "asserts" using only for self-checking
    # and not necessary for auto-testing
    assert count_ingots("A2,B1") == 12, "Two and ten"
    assert count_ingots("A1,A1,A1") == 3, "One, two, three"
    assert count_ingots("Z9,X8,Y7") == 672, "XYZ"
    assert count_ingots("C1,D1,B1,E1,F1") == 140, "Daily normal"
