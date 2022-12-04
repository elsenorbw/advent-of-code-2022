# --- Day 4: Camp Cleanup ---
# Space needs to be cleared before the last supplies can be unloaded from the ships, and so several Elves have been assigned the job of cleaning up sections of the camp.
# Every section has a unique ID number, and each Elf is assigned a range of section IDs.

# However, as some of the Elves compare their section assignments with each other, they've noticed that many of the assignments overlap. To try to quickly find overlaps and
# reduce duplicated effort, the Elves pair up and make a big list of the section assignments for each pair (your puzzle input).

# For example, consider the following list of section assignment pairs:

# 2-4,6-8
# 2-3,4-5
# 5-7,7-9
# 2-8,3-7
# 6-6,4-6
# 2-6,4-8
# For the first few pairs, this list means:

# Within the first pair of Elves, the first Elf was assigned sections 2-4 (sections 2, 3, and 4), while the second Elf was assigned sections 6-8 (sections 6, 7, 8).
# The Elves in the second pair were each assigned two sections.
# The Elves in the third pair were each assigned three sections: one got sections 5, 6, and 7, while the other also got 7, plus 8 and 9.
# This example list uses single-digit section IDs to make it easier to draw; your actual list might contain larger numbers. Visually, these pairs of section assignments look like this:

# .234.....  2-4
# .....678.  6-8

# .23......  2-3
# ...45....  4-5

# ....567..  5-7
# ......789  7-9

# .2345678.  2-8
# ..34567..  3-7

# .....6...  6-6
# ...456...  4-6

# .23456...  2-6
# ...45678.  4-8
# Some of the pairs have noticed that one of their assignments fully contains the other. For example, 2-8 fully contains 3-7, and 6-6 is fully contained by 4-6.
# In pairs where one assignment fully contains the other, one Elf in the pair would be exclusively cleaning sections their partner will already be cleaning, so these seem like the most in need of reconsideration.
# In this example, there are 2 such pairs.

# In how many assignment pairs does one range fully contain the other?
import re


def parse_pair_from_string(pair_string):
    # given a string of "2-3,4-5" return tuple(tuple(2, 3), tuple(4, 5))
    parts = re.split(",|-", pair_string)

    assert len(parts) == 4
    int_parts = [int(x) for x in parts]

    # make sure that lower and upper values are the right way round
    a1, a2, b1, b2 = tuple(int_parts)

    result = tuple(
        [tuple([min(a1, a2), max(a1, a2)]), tuple([min(b1, b2), max(b1, b2)])]
    )

    return result


def load_cleaning_pairs(filename: str):
    # return a list of tuples, each tuple contains a pair of tuples for the starting and ending positions of the elf in question
    all_pairs = []
    with open(filename, "r") as f:
        for this_line in f:
            this_line = this_line.strip()
            this_pair = parse_pair_from_string(this_line)
            all_pairs.append(this_pair)
    return all_pairs


def is_total_overlap(the_pair):
    # True is one of the ranges completely covers the other
    total_overlap = False
    a, b = the_pair
    if b[0] < a[0]:
        a, b = b, a

    # if they start at the same place then they must overlap
    if a[0] == b[0]:
        total_overlap = True

    # therefore we have an overlap if the top value of b is smaller than or equal to the top value of a
    # a starts before b, if b ends before a then we're overlapping..
    if b[1] <= a[1]:
        total_overlap = True

    return total_overlap


def part1(filename: str):
    the_pairs = load_cleaning_pairs(filename)
    # find all the pairs where there is total overlap
    overlaps = [is_total_overlap(this_pair) for this_pair in the_pairs]

    # add em up..
    total_overlaps = sum(overlaps)

    # and that's the answer..
    print(f"part1 result for {filename} is {total_overlaps}")
    return total_overlaps


if __name__ == "__main__":
    sample_filename = "sample.txt"
    puzzle_filename = "input.txt"
    expected_sample_result = 2

    actual_sample_result = part1(sample_filename)
    assert actual_sample_result == expected_sample_result

    part1_result = part1(puzzle_filename)
