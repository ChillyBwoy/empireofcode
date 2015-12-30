"""
Morse Clock

"I'm sending our time logs for the last expedition to HQ, but with this
equipment it's no easy task..." the pilot grumbled. "Can you imagine that with
all the computer power at our disposal, I STILL have to convert this message to
Morse-code using only an on/off button... Hrmph... what a colossal pain."

You will create a module for converting a normal time string to a morse time
string. As you can see in the illustration, a gray circle means on, while a
white circle means off. Every digit in the time string contains a different
number of slots. The first digit for the hours has a length of 2 while the
second digit for the hour has a length of 4. The first digits for the minutes
and seconds have a length of 3 while the second digits for the minutes and
seconds have a length of 4. Every digit in the time is converted to binary
representation. You will convert every "on" (or 1) signal to dash ("-") and
every "off" (or 0) signal to dot (".").

A time string can be in any of the following formats: "hh:mm:ss", "h:m:s" or
"hh:m:ss". The "missing" digits are zeroes. For example, "1:2:3" is the same as
"01:02:03".

The result will be a morse time string with specific format:

h h : m m : s s

where each digits is represented as sequence of "." and "-" (dots and dashes).
Morse clock

Input: A normal time string as a string.

Output: The morse time string as a string.

Example:

morse_time("10:37:49") == ".- .... : .-- .--- : -.. -..-"
morse_time("21:34:56") == "-. ...- : .-- .-.. : -.- .--."
morse_time("00:1:02") == ".. .... : ... ...- : ... ..-."
morse_time("23:59:59") == "-. ..-- : -.- -..- : -.- -..-"
Precondition:

time string contains correct time.

How it is used:

Did you play the binary clocks mission earlier? This can be the basis for a fun
gift for any geek. Now we've remixed the binary clock idea with Morse Code.
Now you can create an even more complex binary clock, one which doesn't just
tell time -- but makes morse style bips and beeps. ;-)

Repository
https://github.com/Checkio-Game-Missions/checkio-empire-morse-clock.git
"""


def fill_zeros(src, size):
    return ('0' * (size - len(src))) + src if len(src) < size else src


def to_bin_str(src):
    digit_int = int(src)
    digit_str = '0' + str(digit_int) if digit_int < 10 else str(digit_int)

    return bin(int(digit_str[0]))[2:], bin(int(digit_str[1]))[2:]


def bin_to_morze(src):
    return ' '.join(
        [''.join(['.' if y == '0' else '-' for y in x]) for x in src])


def morse_time(time_string):
    (h, m, s) = map(to_bin_str, time_string.split(':'))

    hours = fill_zeros(h[0], 2), fill_zeros(h[1], 4)
    minutes = fill_zeros(m[0], 3), fill_zeros(m[1], 4)
    seconds = fill_zeros(s[0], 3), fill_zeros(s[1], 4)

    return ' : '.join([
        bin_to_morze(hours),
        bin_to_morze(minutes),
        bin_to_morze(seconds)
    ])


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert morse_time("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert morse_time("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert morse_time("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert morse_time("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
