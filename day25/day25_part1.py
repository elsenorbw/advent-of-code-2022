# --- Day 25: Full of Hot Air ---
# As the expedition finally reaches the extraction point, several large hot air balloons drift down to meet you. Crews quickly start unloading the equipment the balloons brought: many hot air balloon kits, some fuel tanks, and a fuel heating machine.

# The fuel heating machine is a new addition to the process. When this mountain was a volcano, the ambient temperature was more reasonable; now, it's so cold that the fuel won't work at all without being warmed up first.

# The Elves, seemingly in an attempt to make the new machine feel welcome, have already attached a pair of googly eyes and started calling it "Bob".

# To heat the fuel, Bob needs to know the total amount of fuel that will be processed ahead of time so it can correctly calibrate heat output and flow rate. This amount is simply the sum of the fuel requirements of all of the hot air balloons, and those fuel requirements are even listed clearly on the side of each hot air balloon's burner.

# You assume the Elves will have no trouble adding up some numbers and are about to go back to figuring out which balloon is yours when you get a tap on the shoulder. Apparently, the fuel requirements use numbers written in a format the Elves don't recognize; predictably, they'd like your help deciphering them.

# You make a list of all of the fuel requirements (your puzzle input), but you don't recognize the number format either. For example:

# 1=-0-2
# 12111
# 2=0=
# 21
# 2=01
# 111
# 20012
# 112
# 1=-1=
# 1-12
# 12
# 1=
# 122
# Fortunately, Bob is labeled with a support phone number. Not to be deterred, you call and ask for help.

# "That's right, just supply the fuel amount to the-- oh, for more than one burner? No problem, you just need to add together our Special Numeral-Analogue Fuel Units. Patent pending!
# They're way better than normal numbers for--"

# You mention that it's quite cold up here and ask if they can skip ahead.

# "Okay, our Special Numeral-Analogue Fuel Units - SNAFU for short - are sort of like normal numbers. You know how starting on the right, normal numbers have a ones place, a tens place,
# a hundreds place, and so on, where the digit in each place tells you how many of that value you have?"

# "SNAFU works the same way, except it uses powers of five instead of ten. Starting from the right, you have a ones place, a fives place, a twenty-fives place, a one-hundred-and-twenty-fives place,
# and so on. It's that easy!"

# You ask why some of the digits look like - or = instead of "digits".

# "You know, I never did ask the engineers why they did that.
# Instead of using digits four through zero, the digits are 2, 1, 0, minus (written -), and double-minus (written =). Minus is worth -1, and double-minus is worth -2."

# "So, because ten (in normal numbers) is two fives and no ones, in SNAFU it is written 20. Since eight (in normal numbers) is two fives minus two ones, it is written 2=."

# "You can do it the other direction, too. Say you have the SNAFU number 2=-01. That's 2 in the 625s place, = (double-minus) in the 125s place, - (minus) in the 25s place, 0 in the 5s place, and 1 in
# the 1s place. (2 times 625) plus (-2 times 125) plus (-1 times 25) plus (0 times 5) plus (1 times 1). That's 1250 plus -250 plus -25 plus 0 plus 1. 976!"

# "I see here that you're connected via our premium uplink service, so I'll transmit our handy SNAFU brochure to you now. Did you need anything else?"

# You ask if the fuel will even work in these temperatures.

# "Wait, it's how cold? There's no way the fuel - or any fuel - would work in those conditions! There are only a few places in the-- where did you say you are again?"

# Just then, you notice one of the Elves pour a few drops from a snowflake-shaped container into one of the fuel tanks, thank the support representative for their time, and disconnect the call.

# The SNAFU brochure contains a few more examples of decimal ("normal") numbers and their SNAFU counterparts:

#   Decimal          SNAFU
#         1              1
#         2              2
#         3             1=
#         4             1-
#         5             10
#         6             11
#         7             12
#         8             2=
#         9             2-
#        10             20
#        15            1=0
#        20            1-0
#      2022         1=11-2
#     12345        1-0---0
# 314159265  1121-1110-1=0
# Based on this process, the SNAFU numbers in the example above can be converted to decimal numbers as follows:

#  SNAFU  Decimal
# 1=-0-2     1747
#  12111      906
#   2=0=      198
#     21       11
#   2=01      201
#    111       31
#  20012     1257
#    112       32
#  1=-1=      353
#   1-12      107
#     12        7
#     1=        3
#    122       37
# In decimal, the sum of these numbers is 4890.

# As you go to input this number on Bob's console, you discover that some buttons you expected are missing. Instead, you are met with buttons labeled =, -, 0, 1, and 2.
# Bob needs the input value expressed as a SNAFU number, not in decimal.

# Reversing the process, you can determine that for the decimal number 4890, the SNAFU number you need to supply to Bob's console is 2=-1=0.

# The Elves are starting to get cold. What SNAFU number do you supply to Bob's console?

# To begin, get your puzzle input.


def load_snafu_file(filename: str):
    result = []
    with open(filename, "r") as f:
        for this_line in f:
            this_line = this_line.strip()
            if "" != this_line:
                result.append(this_line)

    return result


def snafu_to_decimal(s: str):

    digits = {"0": 0, "1": 1, "2": 2, "-": -1, "=": -2}

    multiplier = 1
    result = 0
    for this_digit in reversed(s):
        this_digit_value = digits[this_digit]
        result += this_digit_value * multiplier
        # next multiplier
        multiplier *= 5

    return result


def decimal_to_snafu(i: int, verbose=False):
    # ok, so this gets a little trickier I suppose..
    multiplier = 1
    while multiplier < i:
        multiplier *= 5
    if verbose:
        print(f"decimal_to_snafu: initial multiplier value is {multiplier}")

    # so we have a starting location..
    s = []
    remaining_value = i
    while multiplier > 0:
        if verbose:
            print(
                f"decimal_to_snafu: looping for multiplier value {multiplier}, remainging={remaining_value}, s={s}"
            )
        # ok, do we have any number of these that fit into the remaining value
        number_that_fit = remaining_value // multiplier
        if verbose:
            print(
                f"decimal_to_snafu: we have decided that it fits {number_that_fit} times into the remaining {remaining_value}"
            )
        if number_that_fit < 3:
            # easy, we can just fill them in..
            s.append(str(number_that_fit))
        else:
            # more complicated, we need to express 3 or 4
            # easy in this location, they're either minus 2 or minus 1 respectively..
            if number_that_fit == 3:
                s.append("=")
            elif number_that_fit == 4:
                s.append("-")
            else:
                raise Exception(f"No idea what is happening here - {number_that_fit}")
            # and now we need to increment the previous location..
            # this is basically a loop all the way back until we find one that can be incremented..
            need_to_increment = True
            increment_pos = len(s) - 2
            while need_to_increment:
                this_digit = s[increment_pos]
                # so either we have anything less than a 2, which makes life easy..
                if "2" != this_digit:
                    mapping = {"=": "-", "-": "0", "0": "1", "1": "2"}
                    new_digit = mapping[this_digit]
                    s[increment_pos] = new_digit
                    need_to_increment = False
                else:
                    # rolling over from 2 to 3 means rolling to -2 and incrementing the next digit along
                    new_digit = "="
                    s[increment_pos] = new_digit
                    increment_pos -= 1

        # regardless of how we dealt with it, we did deal with it..
        remaining_value -= number_that_fit * multiplier

        # next multiplier
        if multiplier > 1:
            multiplier //= 5
        else:
            multiplier = 0

    # ok, we are done..
    if s[0] == "0":
        result = "".join(s[1:])
    else:
        result = "".join(s)
    return result


def snafu_logic_check():
    for this_val in range(2000):
        snafu_value = decimal_to_snafu(this_val)
        decimal_value = snafu_to_decimal(snafu_value)
        if decimal_value != this_val:
            print(
                f"failed the snafu test on {this_val} -> {snafu_value} -> {decimal_value}"
            )
            decimal_to_snafu(this_val, verbose=True)
            raise Exception(f"loser - {this_val}")


def part1(filename: str):

    snafu_logic_check()

    snafu_strings = load_snafu_file(filename)
    print(snafu_strings)

    decimal_values = [
        snafu_to_decimal(this_snafu_string) for this_snafu_string in snafu_strings
    ]
    print(decimal_values)

    result = sum(decimal_values)

    # and convert it to a snafu number
    result_snafu = decimal_to_snafu(result)

    print(f"The result for {filename} is decimal={result}, snafu={result_snafu}")
    return result_snafu, result


if __name__ == "__main__":
    puzzle_filename = "input.txt"
    sample_filename = "sample.txt"
    sample_expected_result = "2=-1=0"
    sample_expected_result_decimal = 4890

    sample_snafu, sample_decimal = part1(sample_filename)
    assert sample_decimal == sample_expected_result_decimal
    assert sample_snafu == sample_expected_result

    puzzle_snafu, puzzle_decimal = part1(puzzle_filename)
