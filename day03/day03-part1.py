# --- Day 3: Rucksack Reorganization ---
# One Elf has the important job of loading all of the rucksacks with supplies for the jungle journey.
# Unfortunately, that Elf didn't quite follow the packing instructions, and so a few items now need to be rearranged.

# Each rucksack has two large compartments. All items of a given type are meant to go into exactly one of the two compartments.
# The Elf that did the packing failed to follow this rule for exactly one item type per rucksack.

# The Elves have made a list of all of the items currently in each rucksack (your puzzle input), but they need your help finding the errors.
# Every item type is identified by a single lowercase or uppercase letter (that is, a and A refer to different types of items).

# The list of items for each rucksack is given as characters all on a single line. A given rucksack always has the same number of items in each of its two compartments,
# so the first half of the characters represent items in the first compartment, while the second half of the characters represent items in the second compartment.

# For example, suppose you have the following list of contents from six rucksacks:

# vJrwpWtwJgWrhcsFMMfFFhFp
# jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# PmmdzqPrVvPwwTWBwg
# wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# ttgJtRGJQctTZtZT
# CrZsJsPPZsGzwwsLwLmpwMDw

# The first rucksack contains the items vJrwpWtwJgWrhcsFMMfFFhFp, which means its first compartment contains the items vJrwpWtwJgWr,
# while the second compartment contains the items hcsFMMfFFhFp. The only item type that appears in both compartments is lowercase p.
# The second rucksack's compartments contain jqHRNqRjqzjGDLGL and rsFMfFZSrLrFZsSL. The only item type that appears in both compartments is uppercase L.
# The third rucksack's compartments contain PmmdzqPrV and vPwwTWBwg; the only common item type is uppercase P.
# The fourth rucksack's compartments only share item type v.
# The fifth rucksack's compartments only share item type t.
# The sixth rucksack's compartments only share item type s.
# To help prioritize item rearrangement, every item type can be converted to a priority:

# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.
# In the above example, the priority of the item type that appears in both compartments of each rucksack is 16 (p), 38 (L), 42 (P), 22 (v), 20 (t), and 19 (s); the sum of these is 157.

# Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?


def bag_from_line(the_bag: str):
    """
    cut the thing in half, turn it into a tuple of 2 sets
    also sanity check that we have an even number of characters
    """
    assert len(the_bag) % 2 == 0
    items_in_bag = len(the_bag)
    items_per_compartment = items_in_bag // 2
    first_compartment = the_bag[:items_per_compartment]
    second_compartment = the_bag[items_per_compartment:]
    # make sure we don't have an off by one error..
    assert first_compartment + second_compartment == the_bag
    # build the result
    result = (set(first_compartment), set(second_compartment))

    # for my sanity
    print(
        f"started with [{the_bag}], items_in_bag={items_in_bag}, items_per_compartment={items_per_compartment}, first_compartment=[{first_compartment}] second_compartment=[{second_compartment}], result={result}"
    )

    return result


def load_bags(filename: str):
    """
    return a list of the bags in the given file
    each bag will be a tuple of sets of characters
    """
    bags = []
    with open(filename, "r") as f:
        for this_line in f:
            this_line = this_line.strip()
            if "" != this_line:
                this_bag = bag_from_line(this_line)
                bags.append(this_bag)
    return bags


def find_errors(bag_list):
    # find which character is in both the first and second compartments
    matching_sets = [this_bag[0].intersection(this_bag[1]) for this_bag in bag_list]

    # logic check, there should be exactly one item in each result set..
    sanity = [len(this_match) == 1 for this_match in matching_sets]
    assert all(sanity)

    # now de-set the result list
    error_items = [x.pop() for x in matching_sets]

    return error_items


def priority_value_one_supply(the_supply):
    # the values of a supply are :
    # Lowercase item types a through z have priorities 1 through 26.
    # Uppercase item types A through Z have priorities 27 through 52.
    priority_list = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if the_supply not in priority_list:
        raise Exception("You cannot get a priority value for {the_supply}")
    idx = priority_list.index(the_supply)
    return idx


def priority_value_supplies(supply_list):
    # value each item in the supply list
    priority_values = [
        priority_value_one_supply(this_supply) for this_supply in supply_list
    ]
    return priority_values


def part1(filename: str):
    # load all the bags
    all_bags = load_bags(filename)

    # obtain a list of the erroneous items in each bag
    error_supplies = find_errors(all_bags)

    # swap the items for their values
    error_values = priority_value_supplies(error_supplies)

    # add them up
    total_error_value = sum(error_values)

    # disco baby yeah!
    print(f"part1 result for {filename} is {total_error_value}")
    return total_error_value


if __name__ == "__main__":
    sample_filename = "sample.txt"
    puzzle_filename = "input.txt"

    expected_sample_result = 157
    actual_sample_result = part1(sample_filename)
    assert expected_sample_result == actual_sample_result

    real_result = part1(puzzle_filename)
