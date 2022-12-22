# --- Day 21: Monkey Math ---
# The monkeys are back! You're worried they're going to try to steal your stuff again, but it seems like they're just holding their ground and making various monkey noises at you.

# Eventually, one of the elephants realizes you don't speak monkey and comes over to interpret. As it turns out, they overheard you talking about trying to find the grove;
# they can show you a shortcut if you answer their riddle.

# Each monkey is given a job: either to yell a specific number or to yell the result of a math operation. All of the number-yelling monkeys know their number from the start;
# however, the math operation monkeys need to wait for two other monkeys to yell a number, and those two other monkeys might also be waiting on other monkeys.

# Your job is to work out the number the monkey named root will yell before the monkeys figure it out themselves.

# For example:

# root: pppw + sjmn
# dbpl: 5
# cczh: sllz + lgvd
# zczc: 2
# ptdq: humn - dvpt
# dvpt: 3
# lfqf: 4
# humn: 5
# ljgn: 2
# sjmn: drzm * dbpl
# sllz: 4
# pppw: cczh / lfqf
# lgvd: ljgn * ptdq
# drzm: hmdt - zczc
# hmdt: 32
# Each line contains the name of a monkey, a colon, and then the job of that monkey:

# A lone number means the monkey's job is simply to yell that number.
# A job like aaaa + bbbb means the monkey waits for monkeys aaaa and bbbb to yell each of their numbers; the monkey then yells the sum of those two numbers.
# aaaa - bbbb means the monkey yells aaaa's number minus bbbb's number.
# Job aaaa * bbbb will yell aaaa's number multiplied by bbbb's number.
# Job aaaa / bbbb will yell aaaa's number divided by bbbb's number.
# So, in the above example, monkey drzm has to wait for monkeys hmdt and zczc to yell their numbers.
# Fortunately, both hmdt and zczc have jobs that involve simply yelling a single number, so they do this immediately: 32 and 2.
# Monkey drzm can then yell its number by finding 32 minus 2: 30.

# Then, monkey sjmn has one of its numbers (30, from monkey drzm), and already has its other number, 5, from dbpl. This allows it to yell its own number by finding 30 multiplied by 5: 150.

# This process continues until root yells a number: 152.

# However, your actual situation involves considerably more monkeys. What number will the monkey named root yell?

# Your puzzle answer was 66174565793494.

# The first half of this puzzle is complete! It provides one gold star: *

# --- Part Two ---
# Due to some kind of monkey-elephant-human mistranslation, you seem to have misunderstood a few key details about the riddle.

# First, you got the wrong job for the monkey named root; specifically, you got the wrong math operation.
# The correct operation for monkey root should be =, which means that it still listens for two numbers (from the same two monkeys as before), but now checks that the two numbers match.

# Second, you got the wrong monkey for the job starting with humn:.
# It isn't a monkey - it's you. Actually, you got the job wrong, too: you need to figure out what number you need to yell so that root's equality check passes.
# (The number that appears after humn: in your input is now irrelevant.)

# In the above example, the number you need to yell to pass root's equality test is 301. (This causes root to get the same number, 150, from both of its monkeys.)

# What number do you yell to pass root's equality test?


from typing import Optional, Dict


class Monkey:
    def __init__(
        self,
        name: str,
        int_val: int,
        operation: str,
        monkey_a_name: Optional[str],
        monkey_b_name: Optional[str],
    ) -> None:
        self.name = name
        self.int_val = int_val
        self.operation = operation
        self.a = monkey_a_name
        self.b = monkey_b_name

    def set_value(self, the_new_value: int):
        self.int_val = the_new_value

    def set_operation(self, new_operation: str):
        self.operation = new_operation

    def __repr__(self) -> str:
        s = f"<Monkey {self.name} {self.operation} {self.int_val}, {self.a}, {self.b}>"
        return s

    def evaluate(self, all_monkeys):
        # execute this monkey, may need to get recursive..
        if "!" == self.operation:
            return self.int_val
        else:
            a_val = all_monkeys[self.a].evaluate(all_monkeys)
            b_val = all_monkeys[self.b].evaluate(all_monkeys)
            if "+" == self.operation:
                return int(a_val + b_val)
            elif "-" == self.operation:
                return int(a_val - b_val)
            elif "*" == self.operation:
                return int(a_val * b_val)
            elif "/" == self.operation:
                return int(a_val // b_val)
            elif "=" == self.operation:
                # we need to see how far apart the two sides are... so..
                return a_val - b_val
            else:
                raise Exception(
                    f"What the hell kind of operation is {self.operation} ? ({self.name})"
                )


def load_monkeys(filename: str):
    monkeys: Dict[str, Monkey] = dict()

    with open(filename, "r") as f:
        for this_line in f:
            this_line = this_line.strip()
            if "" != this_line:
                # got a monkey..
                main_parts = this_line.split(":")
                assert 2 == len(main_parts)
                monkey_name = main_parts[0]
                job_parts = main_parts[1].strip().split(" ")
                if 1 == len(job_parts):
                    monkey_intval = int(job_parts[0])
                    monkey_operation = "!"
                    monkey_a = None
                    monkey_b = None
                elif 3 == len(job_parts):
                    monkey_operation = job_parts[1]
                    monkey_a = job_parts[0]
                    monkey_b = job_parts[2]
                    monkey_intval = -1
                else:
                    raise Exception(f"er what now ? {this_line} - {job_parts}")

                # create that monkey..
                this_monkey = Monkey(
                    monkey_name, monkey_intval, monkey_operation, monkey_a, monkey_b
                )
                monkeys[monkey_name] = this_monkey

    return monkeys


def run_monkeys_for_one_human_value(monkeys, human_value):
    monkeys["humn"].set_value(human_value)
    result = monkeys["root"].evaluate(monkeys)
    return result


def sign(i: int):
    if i < 0:
        return "-"
    return "+"


def binary_find_human_value(monkeys):
    # going to find some starting values..
    low_val = 100
    low_val_result = run_monkeys_for_one_human_value(monkeys, low_val)
    print(f"{low_val} --> {low_val_result}")

    # keep going until we flip the sign of the result..
    next_val_result = low_val_result
    next_val = low_val
    while sign(next_val_result) == sign(low_val_result):
        # so far we have a low value..
        low_val = next_val
        low_val_result = next_val_result
        print(f"{low_val} --> {low_val_result}")

        # double up and try again..
        next_val = int(low_val * 2)
        next_val_result = run_monkeys_for_one_human_value(monkeys, next_val)

    # and we've exited the loop, so we have a high value..
    high_val = next_val
    high_val_result = next_val_result
    print(
        f" starting the search proper with a low of {low_val}->{low_val_result} and a high of {high_val}->{high_val_result}"
    )

    # we will do this until we get a 0
    while 0 != next_val_result:
        # have a go..
        next_val = low_val + int((high_val - low_val) // 2)
        next_val_result = run_monkeys_for_one_human_value(monkeys, next_val)
        # if it's non-zero we need to decide which side to move..
        print(f"- search continues with {next_val}->{next_val_result}")
        if sign(next_val_result) == sign(low_val_result):
            low_val_result = next_val_result
            low_val = next_val
        else:
            high_val_result = next_val_result
            high_val = next_val
        print(
            f"   - state is now  low of {low_val}->{low_val_result} and a high of {high_val}->{high_val_result}"
        )

    # and we have a result..
    print(f" - finishing off with {next_val} -> {next_val_result}")
    return next_val


def part2(filename: str):
    monkeys = load_monkeys(filename)
    monkeys["root"].set_operation("=")

    # so we need to set the human value and evaluate..

    result = binary_find_human_value(monkeys)

    print(
        f"the human needs to shout {result} to make the monkey in file {filename} happy"
    )
    return result


if __name__ == "__main__":
    puzzle_filename = "input.txt"
    sample_filename = "sample.txt"
    sample_expected_result = 301

    sample_actual_result = part2(sample_filename)
    assert sample_actual_result == sample_expected_result

    puzzle_result = part2(puzzle_filename)
