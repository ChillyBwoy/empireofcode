"""
Fizz Buzz

To get them ready for storage, we need the worker-bots to sort crystals by 3 or 5 or divide them by the number of edges. To make things easier, we will base our program on the ancient human word game "Fizz buzz".

Our goal is to write a function that will receive a positive integer and return:

The phrase "Fizz Buzz" if the number is divisible by 3 and by 5,

The word "Fizz" if the number is divisible by 3,

The word "Buzz" if the number is divisible by 5,

The number as a string for all other cases.

Input: A number as an integer.

Output: The answer as a string.

Example:

fizz_buzz(15) == "Fizz Buzz"
fizz_buzz(6) == "Fizz"
fizz_buzz(5) == "Buzz"
fizz_buzz(7) == "7"
Precondition:

0 < number ≤ 1000

How it is used:

Here you can learn how to write simple functions and work with if-else statements.
"""


def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "Fizz Buzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert fizz_buzz(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert fizz_buzz(6) == "Fizz", "6 is divisible by 3"
    assert fizz_buzz(5) == "Buzz", "5 is divisible by 5"
    assert fizz_buzz(7) == "7", "7 is not divisible by 3 or 5"

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
