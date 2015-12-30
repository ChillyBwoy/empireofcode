"""
Vault Password

We've installed a new vault to contain our valuable resources and treasures,
but before we can put anything into it, we need a suitable password for our new
vault. One that should be as safe as possible.

The password will be considered strong enough if its length is greater than or
equal to 10 characters, it contains at least one digit, as well as at least one
uppercase letter and one lowercase letter. The password may only contain ASCII
latin letters or digits, no punctuation symbols.

You are given a password. We need your code to verify if it meets the
conditions for a secure password.

In this mission the main goal to make your code as short as possible. The
shorter your code, the more points you earn. Your score for this mission is
dynamic and directly related to the length of your code.

Input: A password as a string.

Output: A determination if the password safe or not as a boolean, or any data
type that can be converted and processed as a boolean. When the results
process, you will see the converted results.

Example:

golf('A1213pokl') == False
golf('bAse730onE') == True
golf('asasasasasasasaas') == False
golf('QWERTYqwerty') == False
golf('123456123456') == False
golf('QwErTy911poqqqq') == True
Precondition:

0 < "password| ≤ 64

password matches by regexp expression "[a-zA-Z0-9]+"

Scoring:

Scoring in this mission is based on the number of characters used in your code
(comment lines are not counted).

Rank1:

Any code length.

Rank2:

Your code should be shorter than 200 characters.

Rank3:

Your code should be shorter than 100 characters.

How it is used:

If you are worried about the security of your app or service, you can use this
handy code to personally check your users' passwords for complexity. You can
further use these skills to require that your users passwords meet or include
even more conditions, punctuation or unicode.
"""

import string as s


def golf(p):
    alnum = set(s.ascii_letters + s.digits)
    return len(p) > 9 and len(set(p) & alnum) > 3


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert golf('A1213pokl') == False, 'A1213pokl'
    assert golf('bAse730onE') == True, 'bAse730onE'
    assert golf('asasasasasasasaas') == False, 'asasasasasasasaas'
    assert golf('QWERTYqwerty') == False, 'QWERTYqwerty'
    assert golf('123456123456') == False, '123456123456'
    assert golf('QwErTy911poqqqq') == True, 'QwErTy911poqqqq'

    print("Use 'Check' to earn sweet rewards!")
