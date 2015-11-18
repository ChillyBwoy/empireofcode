"""
Number Base

Sometimes the robots mix up their coordinates and use other Numeral systems. Let's try to sort this out and see what could be going on.

You are given a positive number as a string along with the radix for it. Your function should convert it into decimal form. The radix is less than 37 and greater than 1. The task uses digits and the letters A-Z for the strings.

Watch out for cases when the number cannot be converted. For example: "1A" cannot be converted with radix 9. For these cases your function should return -1.

Input: Two arguments. A number as string and a radix as an integer.

Output: The converted number as an integer.

Example:

convert("AF", 16) == 175
convert("101", 2) == 5
convert("101", 5) == 26
convert("Z", 36) == 35
convert("AB", 10) == -1
Precondition:

re.match("\A[A-Z0-9]\Z", str_number)
0 < len(str_number) <= 10
2 <= radix <= 36
How it is used:

Here you will learn how to work with the various numeral systems and handle exceptions."""


from string import digits, ascii_uppercase

ALPHABET = list(digits + ascii_uppercase)


def convert(str_number, radix):
    if 0 >= len(str_number) > 10:
        return -1
    elif 2 > radix > 36:
        return -1
    else:
        letters = ALPHABET[0:radix]
        filtered = [s for s in str_number if s in letters]
        if len(filtered) != len(str_number):
            return -1

        

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert convert("AF", 16) == 175, "Hex"
    assert convert("101", 2) == 5, "Bin"
    assert convert("101", 5) == 26, "5 base"
    assert convert("Z", 36) == 35, "Z base"
    assert convert("AB", 10) == -1, "B > A > 10"

    print("Use 'Check' to earn sweet rewards!")
