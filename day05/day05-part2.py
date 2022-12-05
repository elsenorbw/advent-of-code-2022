# --- Day 5: Supply Stacks ---
# The expedition can depart as soon as the final supplies have been unloaded from the ships. Supplies are stored in stacks of marked crates, but because the needed supplies are buried under many other crates, the crates need to be rearranged.

# The ship has a giant cargo crane capable of moving crates between stacks. To ensure none of the crates get crushed or fall over, the crane operator will rearrange them in a series of carefully-planned steps. After the crates are rearranged, the desired crates will be at the top of each stack.

# The Elves don't want to interrupt the crane operator during this delicate procedure, but they forgot to ask her which crate will end up where, and they want to be ready to unload them as soon as possible so they can embark.

# They do, however, have a drawing of the starting stacks of crates and the rearrangement procedure (your puzzle input). For example:

#     [D]
# [N] [C]
# [Z] [M] [P]
#  1   2   3

# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2
# In this example, there are three stacks of crates. Stack 1 contains two crates: crate Z is on the bottom, and crate N is on top.
# Stack 2 contains three crates; from bottom to top, they are crates M, C, and D. Finally, stack 3 contains a single crate, P.

# Then, the rearrangement procedure is given. In each step of the procedure, a quantity of crates is moved from one stack to a different stack.
# In the first step of the above rearrangement procedure, one crate is moved from stack 2 to stack 1, resulting in this configuration:

# [D]
# [N] [C]
# [Z] [M] [P]
#  1   2   3
# In the second step, three crates are moved from stack 1 to stack 3. Crates are moved one at a time, so the first crate to be moved (D) ends up below the second and third crates:

#         [Z]
#         [N]
#     [C] [D]
#     [M] [P]
#  1   2   3
# Then, both crates are moved from stack 2 to stack 1. Again, because crates are moved one at a time, crate C ends up below crate M:

#         [Z]
#         [N]
# [M]     [D]
# [C]     [P]
#  1   2   3
# Finally, one crate is moved from stack 1 to stack 2:

#         [Z]
#         [N]
#         [D]
# [C] [M] [P]
#  1   2   3
# The Elves just need to know which crate will end up on top of each stack; in this example, the top crates are C in stack 1, M in stack 2, and Z in stack 3, so you should combine these
# together and give the Elves the message CMZ.

# After the rearrangement procedure completes, what crate ends up on top of each stack?

# Your puzzle answer was ZBDRNPMVH.

# The first half of this puzzle is complete! It provides one gold star: *

# --- Part Two ---
# As you watch the crane operator expertly rearrange the crates, you notice the process isn't following your prediction.

# Some mud was covering the writing on the side of the crane, and you quickly wipe it away. The crane isn't a CrateMover 9000 - it's a CrateMover 9001.

# The CrateMover 9001 is notable for many new and exciting features: air conditioning, leather seats, an extra cup holder, and the ability to pick up and move multiple crates at once.

# Again considering the example above, the crates begin in the same configuration:

#     [D]
# [N] [C]
# [Z] [M] [P]
#  1   2   3
# Moving a single crate from stack 2 to stack 1 behaves the same as before:

# [D]
# [N] [C]
# [Z] [M] [P]
#  1   2   3
# However, the action of moving three crates from stack 1 to stack 3 means that those three moved crates stay in the same order, resulting in this new configuration:

#         [D]
#         [N]
#     [C] [Z]
#     [M] [P]
#  1   2   3
# Next, as both crates are moved from stack 2 to stack 1, they retain their order as well:

#         [D]
#         [N]
# [C]     [Z]
# [M]     [P]
#  1   2   3
# Finally, a single crate is still moved from stack 1 to stack 2, but now it's crate C that gets moved:

#         [D]
#         [N]
#         [Z]
# [M] [C] [P]
#  1   2   3
# In this example, the CrateMover 9001 has put the crates in a totally different order: MCD.

# Before the rearrangement process finishes, update your simulation so that the Elves know where they should stand to be ready to unload the final supplies.
# After the rearrangement procedure completes, what crate ends up on top of each stack?


def load_crates_and_instructions(filename: str):
    # returning two values, the dictionary of initial state values and tuples of instructions (repetition, source_stack, target_stack)
    the_stacks = dict()
    the_instructions = list()

    with open(filename, "r") as f:
        for this_line in f:
            this_line = this_line.rstrip()
            if "" != this_line:
                # ok, we have 2 types of line we care about
                # lines where the first non-space character is a square bracket - a crate line..
                # and lines that start with move
                if -1 != this_line.find("["):
                    print(f"CRATES! -> {this_line}")
                    # so the first useful thing is at position 1, then every 4 characters after that is the next crate pile
                    for idx, this_character in enumerate(
                        range(1, len(this_line), 4), start=1
                    ):
                        the_character = this_line[this_character]
                        print(
                            f"Found [{the_character}] at location {this_character} which is for stack {idx}"
                        )
                        if " " != the_character:
                            # we need to store this crate
                            if idx not in the_stacks:
                                the_stacks[idx] = list()
                            the_stacks[idx].append(the_character)

                elif this_line.startswith("move"):
                    # line format is "move 1 from 2 to 1"
                    from_idx = this_line.find(" from ")
                    to_idx = this_line.find(" to ")

                    # extract the numerical parts
                    repetitions_str = this_line[5:from_idx]
                    source_str = this_line[from_idx + 6 : to_idx]
                    to_str = this_line[to_idx + 4 :]

                    # and build the instructions
                    this_instruction = tuple(
                        [int(repetitions_str), int(source_str), int(to_str)]
                    )

                    # and add them to the list
                    the_instructions.append(this_instruction)

                    print(
                        f"MOVE! -> {this_line} -> [{repetitions_str}],[{source_str}],[{to_str}]"
                    )

    # It would be more convenient if the stacks had their top-most element at the end of the lists..
    for this_stack in the_stacks.keys():
        the_stacks[this_stack] = list(reversed(the_stacks[this_stack]))

    print(f"Load is complete and we have : {the_stacks} and {the_instructions}")

    return the_stacks, the_instructions


def move_one_crate(crates, source_idx, target_idx):
    the_crate = crates[source_idx].pop()
    crates[target_idx].append(the_crate)


def move_many_crates(crates, source_idx, target_idx, count):
    # move a stack of crates from a to b
    # copy the top X crates..
    crates_to_move = crates[source_idx][-count:]
    # remove them from the source
    crates[source_idx] = crates[source_idx][:-count]
    # and add them to the target
    crates[target_idx].extend(crates_to_move)


def apply_one_instruction(crates, crates_to_move, source_stack, target_stack):
    move_many_crates(crates, source_stack, target_stack, crates_to_move)
    return crates


def apply_instructions(crates, instructions):
    moved_crates = crates.copy()

    for repetitions, source_stack, target_stack in instructions:
        apply_one_instruction(moved_crates, repetitions, source_stack, target_stack)

    return moved_crates


def get_top_crates(crates):
    result = ""
    for stack in sorted(crates.keys()):
        result += crates[stack][-1]
    return result


def part2(filename: str):
    the_crates, the_instructions = load_crates_and_instructions(filename)

    # apply the instructions to the crates
    moved_crates = apply_instructions(the_crates, the_instructions)

    # get the top crates..
    top_crates = get_top_crates(moved_crates)

    print(f"The part2 result for {filename} is {top_crates}")
    return top_crates


if __name__ == "__main__":
    sample_filename = "sample.txt"
    puzzle_filename = "input.txt"
    expected_sample_result = "MCD"

    actual_sample_result = part2(sample_filename)
    assert actual_sample_result == expected_sample_result

    part2_result = part2(puzzle_filename)
