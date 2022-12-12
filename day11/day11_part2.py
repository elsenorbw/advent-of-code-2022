# --- Day 11: Monkey in the Middle ---
# As you finally start making your way upriver, you realize your pack is much lighter than you remember.
# Just then, one of the items from your pack goes flying overhead. Monkeys are playing Keep Away with your missing things!

# To get your stuff back, you need to be able to predict where the monkeys will throw your items.
# After some careful observation, you realize the monkeys operate based on how worried you are about each item.

# You take some notes (your puzzle input) on the items each monkey currently has, how worried you are about those items,
# and how the monkey makes decisions based on your worry level. For example:

# Monkey 0:
#   Starting items: 79, 98
#   Operation: new = old * 19
#   Test: divisible by 23
#     If true: throw to monkey 2
#     If false: throw to monkey 3

# Monkey 1:
#   Starting items: 54, 65, 75, 74
#   Operation: new = old + 6
#   Test: divisible by 19
#     If true: throw to monkey 2
#     If false: throw to monkey 0

# Monkey 2:
#   Starting items: 79, 60, 97
#   Operation: new = old * old
#   Test: divisible by 13
#     If true: throw to monkey 1
#     If false: throw to monkey 3

# Monkey 3:
#   Starting items: 74
#   Operation: new = old + 3
#   Test: divisible by 17
#     If true: throw to monkey 0
#     If false: throw to monkey 1
# Each monkey has several attributes:

# Starting items lists your worry level for each item the monkey is currently holding in the order they will be inspected.
# Operation shows how your worry level changes as that monkey inspects an item. (An operation like new = old * 5 means that
# your worry level after the monkey inspected the item is five times whatever your worry level was before inspection.)
# Test shows how the monkey uses your worry level to decide where to throw an item next.
# If true shows what happens with an item if the Test was true.
# If false shows what happens with an item if the Test was false.
# After each monkey inspects an item but before it tests your worry level, your relief that the monkey's inspection didn't damage the
# item causes your worry level to be divided by three and rounded down to the nearest integer.

# The monkeys take turns inspecting and throwing items. On a single monkey's turn, it inspects and throws all of the items it is holding
# one at a time and in the order listed. Monkey 0 goes first, then monkey 1, and so on until each monkey has had one turn. The process of
# each monkey taking a single turn is called a round.

# When a monkey throws an item to another monkey, the item goes on the end of the recipient monkey's list. A monkey that starts a round with no
# items could end up inspecting and throwing many items by the time its turn comes around. If a monkey is holding no items at the start of its turn, its turn ends.

# In the above example, the first round proceeds as follows:

# Monkey 0:
#   Monkey inspects an item with a worry level of 79.
#     Worry level is multiplied by 19 to 1501.
#     Monkey gets bored with item. Worry level is divided by 3 to 500.
#     Current worry level is not divisible by 23.
#     Item with worry level 500 is thrown to monkey 3.
#   Monkey inspects an item with a worry level of 98.
#     Worry level is multiplied by 19 to 1862.
#     Monkey gets bored with item. Worry level is divided by 3 to 620.
#     Current worry level is not divisible by 23.
#     Item with worry level 620 is thrown to monkey 3.
# Monkey 1:
#   Monkey inspects an item with a worry level of 54.
#     Worry level increases by 6 to 60.
#     Monkey gets bored with item. Worry level is divided by 3 to 20.
#     Current worry level is not divisible by 19.
#     Item with worry level 20 is thrown to monkey 0.
#   Monkey inspects an item with a worry level of 65.
#     Worry level increases by 6 to 71.
#     Monkey gets bored with item. Worry level is divided by 3 to 23.
#     Current worry level is not divisible by 19.
#     Item with worry level 23 is thrown to monkey 0.
#   Monkey inspects an item with a worry level of 75.
#     Worry level increases by 6 to 81.
#     Monkey gets bored with item. Worry level is divided by 3 to 27.
#     Current worry level is not divisible by 19.
#     Item with worry level 27 is thrown to monkey 0.
#   Monkey inspects an item with a worry level of 74.
#     Worry level increases by 6 to 80.
#     Monkey gets bored with item. Worry level is divided by 3 to 26.
#     Current worry level is not divisible by 19.
#     Item with worry level 26 is thrown to monkey 0.
# Monkey 2:
#   Monkey inspects an item with a worry level of 79.
#     Worry level is multiplied by itself to 6241.
#     Monkey gets bored with item. Worry level is divided by 3 to 2080.
#     Current worry level is divisible by 13.
#     Item with worry level 2080 is thrown to monkey 1.
#   Monkey inspects an item with a worry level of 60.
#     Worry level is multiplied by itself to 3600.
#     Monkey gets bored with item. Worry level is divided by 3 to 1200.
#     Current worry level is not divisible by 13.
#     Item with worry level 1200 is thrown to monkey 3.
#   Monkey inspects an item with a worry level of 97.
#     Worry level is multiplied by itself to 9409.
#     Monkey gets bored with item. Worry level is divided by 3 to 3136.
#     Current worry level is not divisible by 13.
#     Item with worry level 3136 is thrown to monkey 3.
# Monkey 3:
#   Monkey inspects an item with a worry level of 74.
#     Worry level increases by 3 to 77.
#     Monkey gets bored with item. Worry level is divided by 3 to 25.
#     Current worry level is not divisible by 17.
#     Item with worry level 25 is thrown to monkey 1.
#   Monkey inspects an item with a worry level of 500.
#     Worry level increases by 3 to 503.
#     Monkey gets bored with item. Worry level is divided by 3 to 167.
#     Current worry level is not divisible by 17.
#     Item with worry level 167 is thrown to monkey 1.--- Day 11: Monkey in the Middle ---
# As you finally start making your way upriver, you realize your pack is much lighter than you remember.
# Just then, one of the items from your pack goes flying overhead. Monkeys are playing Keep Away with your missing things!

# To get your stuff back, you need to be able to predict where the monkeys will throw your items. After some careful observation,
# you realize the monkeys operate based on how worried you are about each item.

# You take some notes (your puzzle input) on the items each monkey currently has, how worried you are about those items,
# and how the monkey makes decisions based on your worry level. For example:

# Monkey 0:
#   Starting items: 79, 98
#   Operation: new = old * 19
#   Test: divisible by 23
#     If true: throw to monkey 2
#     If false: throw to monkey 3

# Monkey 1:
#   Starting items: 54, 65, 75, 74
#   Operation: new = old + 6
#   Test: divisible by 19
#     If true: throw to monkey 2
#     If false: throw to monkey 0

# Monkey 2:
#   Starting items: 79, 60, 97
#   Operation: new = old * old
#   Test: divisible by 13
#     If true: throw to monkey 1
#     If false: throw to monkey 3

# Monkey 3:
#   Starting items: 74
#   Operation: new = old + 3
#   Test: divisible by 17
#     If true: throw to monkey 0
#     If false: throw to monkey 1
# Each monkey has several attributes:

# Starting items lists your worry level for each item the monkey is currently holding in the order they will be inspected.
# Operation shows how your worry level changes as that monkey inspects an item. (An operation like new = old * 5 means that your worry
# level after the monkey inspected the item is five times whatever your worry level was before inspection.)
# Test shows how the monkey uses your worry level to decide where to throw an item next.
# If true shows what happens with an item if the Test was true.
# If false shows what happens with an item if the Test was false.
# After each monkey inspects an item but before it tests your worry level, your relief that the monkey's inspection didn't damage the item
# causes your worry level to be divided by three and rounded down to the nearest integer.

# The monkeys take turns inspecting and throwing items. On a single monkey's turn, it inspects and throws all of the items it is holding one at a
# time and in the order listed. Monkey 0 goes first, then monkey 1, and so on until each monkey has had one turn. The process of each monkey taking a single turn is called a round.

# When a monkey throws an item to another monkey, the item goes on the end of the recipient monkey's list. A monkey that starts a round with
# no items could end up inspecting and throwing many items by the time its turn comes around. If a monkey is holding no items at the start of its turn, its turn ends.

# In the above example, the first round proceeds as follows:

# Monkey 0:
#   Monkey inspects an item with a worry level of 79.
#     Worry level is multiplied by 19 to 1501.
#     Monkey gets bored with item. Worry level is divided by 3 to 500.
#     Current worry level is not divisible by 23.
#     Item with worry level 500 is thrown to monkey 3.
#   Monkey inspects an item with a worry level of 98.
#     Worry level is multiplied by 19 to 1862.
#     Monkey gets bored with item. Worry level is divided by 3 to 620.
#     Current worry level is not divisible by 23.
#     Item with worry level 620 is thrown to monkey 3.
# Monkey 1:
#   Monkey inspects an item with a worry level of 54.
#     Worry level increases by 6 to 60.
#     Monkey gets bored with item. Worry level is divided by 3 to 20.
#     Current worry level is not divisible by 19.
#     Item with worry level 20 is thrown to monkey 0.
#   Monkey inspects an item with a worry level of 65.
#     Worry level increases by 6 to 71.
#     Monkey gets bored with item. Worry level is divided by 3 to 23.
#     Current worry level is not divisible by 19.
#     Item with worry level 23 is thrown to monkey 0.
#   Monkey inspects an item with a worry level of 75.
#     Worry level increases by 6 to 81.
#     Monkey gets bored with item. Worry level is divided by 3 to 27.
#     Current worry level is not divisible by 19.
#     Item with worry level 27 is thrown to monkey 0.
#   Monkey inspects an item with a worry level of 74.
#     Worry level increases by 6 to 80.
#     Monkey gets bored with item. Worry level is divided by 3 to 26.
#     Current worry level is not divisible by 19.
#     Item with worry level 26 is thrown to monkey 0.
# Monkey 2:
#   Monkey inspects an item with a worry level of 79.
#     Worry level is multiplied by itself to 6241.
#     Monkey gets bored with item. Worry level is divided by 3 to 2080.
#     Current worry level is divisible by 13.
#     Item with worry level 2080 is thrown to monkey 1.
#   Monkey inspects an item with a worry level of 60.
#     Worry level is multiplied by itself to 3600.
#     Monkey gets bored with item. Worry level is divided by 3 to 1200.
#     Current worry level is not divisible by 13.
#     Item with worry level 1200 is thrown to monkey 3.
#   Monkey inspects an item with a worry level of 97.
#     Worry level is multiplied by itself to 9409.
#     Monkey gets bored with item. Worry level is divided by 3 to 3136.
#     Current worry level is not divisible by 13.
#     Item with worry level 3136 is thrown to monkey 3.
# Monkey 3:
#   Monkey inspects an item with a worry level of 74.
#     Worry level increases by 3 to 77.
#     Monkey gets bored with item. Worry level is divided by 3 to 25.
#     Current worry level is not divisible by 17.
#     Item with worry level 25 is thrown to monkey 1.
#   Monkey inspects an item with a worry level of 500.
#     Worry level increases by 3 to 503.
#     Monkey gets bored with item. Worry level is divided by 3 to 167.
#     Current worry level is not divisible by 17.
#     Item with worry level 167 is thrown to monkey 1.
#   Monkey inspects an item with a worry level of 620.
#     Worry level increases by 3 to 623.
#     Monkey gets bored with item. Worry level is divided by 3 to 207.
#     Current worry level is not divisible by 17.
#     Item with worry level 207 is thrown to monkey 1.
#   Monkey inspects an item with a worry level of 1200.
#     Worry level increases by 3 to 1203.
#     Monkey gets bored with item. Worry level is divided by 3 to 401.
#     Current worry level is not divisible by 17.
#     Item with worry level 401 is thrown to monkey 1.
#   Monkey inspects an item with a worry level of 3136.
#     Worry level increases by 3 to 3139.
#     Monkey gets bored with item. Worry level is divided by 3 to 1046.
#     Current worry level is not divisible by 17.
#     Item with worry level 1046 is thrown to monkey 1.
# After round 1, the monkeys are holding items with these worry levels:

# Monkey 0: 20, 23, 27, 26
# Monkey 1: 2080, 25, 167, 207, 401, 1046
# Monkey 2:
# Monkey 3:
# Monkeys 2 and 3 aren't holding any items at the end of the round; they both inspected items during the round and threw them all before the round ended.

# This process continues for a few more rounds:

# After round 2, the monkeys are holding items with these worry levels:
# Monkey 0: 695, 10, 71, 135, 350
# Monkey 1: 43, 49, 58, 55, 362
# Monkey 2:
# Monkey 3:

# After round 3, the monkeys are holding items with these worry levels:
# Monkey 0: 16, 18, 21, 20, 122
# Monkey 1: 1468, 22, 150, 286, 739
# Monkey 2:
# Monkey 3:

# After round 4, the monkeys are holding items with these worry levels:
# Monkey 0: 491, 9, 52, 97, 248, 34
# Monkey 1: 39, 45, 43, 258
# Monkey 2:
# Monkey 3:

# After round 5, the monkeys are holding items with these worry levels:
# Monkey 0: 15, 17, 16, 88, 1037
# Monkey 1: 20, 110, 205, 524, 72
# Monkey 2:
# Monkey 3:

# After round 6, the monkeys are holding items with these worry levels:
# Monkey 0: 8, 70, 176, 26, 34
# Monkey 1: 481, 32, 36, 186, 2190
# Monkey 2:
# Monkey 3:

# After round 7, the monkeys are holding items with these worry levels:
# Monkey 0: 162, 12, 14, 64, 732, 17
# Monkey 1: 148, 372, 55, 72
# Monkey 2:
# Monkey 3:

# After round 8, the monkeys are holding items with these worry levels:
# Monkey 0: 51, 126, 20, 26, 136
# Monkey 1: 343, 26, 30, 1546, 36
# Monkey 2:
# Monkey 3:

# After round 9, the monkeys are holding items with these worry levels:
# Monkey 0: 116, 10, 12, 517, 14
# Monkey 1: 108, 267, 43, 55, 288
# Monkey 2:
# Monkey 3:

# After round 10, the monkeys are holding items with these worry levels:
# Monkey 0: 91, 16, 20, 98
# Monkey 1: 481, 245, 22, 26, 1092, 30
# Monkey 2:
# Monkey 3:

# ...

# After round 15, the monkeys are holding items with these worry levels:
# Monkey 0: 83, 44, 8, 184, 9, 20, 26, 102
# Monkey 1: 110, 36
# Monkey 2:
# Monkey 3:

# ...

# After round 20, the monkeys are holding items with these worry levels:
# Monkey 0: 10, 12, 14, 26, 34
# Monkey 1: 245, 93, 53, 199, 115
# Monkey 2:
# Monkey 3:
# Chasing all of the monkeys at once is impossible; you're going to have to focus on the two most active monkeys if you want any hope of getting your stuff back.
# Count the total number of times each monkey inspects items over 20 rounds:

# Monkey 0 inspected items 101 times.
# Monkey 1 inspected items 95 times.
# Monkey 2 inspected items 7 times.
# Monkey 3 inspected items 105 times.
# In this example, the two most active monkeys inspected items 101 and 105 times. The level of monkey business in this situation can be found by multiplying these together: 10605.

# Figure out which monkeys to chase by counting how many items they inspect over 20 rounds. What is the level of monkey business after 20 rounds of stuff-slinging simian shenanigans?

#   Monkey inspects an item with a worry level of 620.
#     Worry level increases by 3 to 623.
#     Monkey gets bored with item. Worry level is divided by 3 to 207.
#     Current worry level is not divisible by 17.
#     Item with worry level 207 is thrown to monkey 1.
#   Monkey inspects an item with a worry level of 1200.
#     Worry level increases by 3 to 1203.
#     Monkey gets bored with item. Worry level is divided by 3 to 401.
#     Current worry level is not divisible by 17.
#     Item with worry level 401 is thrown to monkey 1.
#   Monkey inspects an item with a worry level of 3136.
#     Worry level increases by 3 to 3139.
#     Monkey gets bored with item. Worry level is divided by 3 to 1046.
#     Current worry level is not divisible by 17.
#     Item with worry level 1046 is thrown to monkey 1.
# After round 1, the monkeys are holding items with these worry levels:

# Monkey 0: 20, 23, 27, 26
# Monkey 1: 2080, 25, 167, 207, 401, 1046
# Monkey 2:
# Monkey 3:
# Monkeys 2 and 3 aren't holding any items at the end of the round; they both inspected items during the round and threw them all before the round ended.

# This process continues for a few more rounds:

# After round 2, the monkeys are holding items with these worry levels:
# Monkey 0: 695, 10, 71, 135, 350
# Monkey 1: 43, 49, 58, 55, 362
# Monkey 2:
# Monkey 3:

# After round 3, the monkeys are holding items with these worry levels:
# Monkey 0: 16, 18, 21, 20, 122
# Monkey 1: 1468, 22, 150, 286, 739
# Monkey 2:
# Monkey 3:

# After round 4, the monkeys are holding items with these worry levels:
# Monkey 0: 491, 9, 52, 97, 248, 34
# Monkey 1: 39, 45, 43, 258
# Monkey 2:
# Monkey 3:

# After round 5, the monkeys are holding items with these worry levels:
# Monkey 0: 15, 17, 16, 88, 1037
# Monkey 1: 20, 110, 205, 524, 72
# Monkey 2:
# Monkey 3:

# After round 6, the monkeys are holding items with these worry levels:
# Monkey 0: 8, 70, 176, 26, 34
# Monkey 1: 481, 32, 36, 186, 2190
# Monkey 2:
# Monkey 3:

# After round 7, the monkeys are holding items with these worry levels:
# Monkey 0: 162, 12, 14, 64, 732, 17
# Monkey 1: 148, 372, 55, 72
# Monkey 2:
# Monkey 3:

# After round 8, the monkeys are holding items with these worry levels:
# Monkey 0: 51, 126, 20, 26, 136
# Monkey 1: 343, 26, 30, 1546, 36
# Monkey 2:
# Monkey 3:

# After round 9, the monkeys are holding items with these worry levels:
# Monkey 0: 116, 10, 12, 517, 14
# Monkey 1: 108, 267, 43, 55, 288
# Monkey 2:
# Monkey 3:

# After round 10, the monkeys are holding items with these worry levels:
# Monkey 0: 91, 16, 20, 98
# Monkey 1: 481, 245, 22, 26, 1092, 30
# Monkey 2:
# Monkey 3:

# ...

# After round 15, the monkeys are holding items with these worry levels:
# Monkey 0: 83, 44, 8, 184, 9, 20, 26, 102
# Monkey 1: 110, 36
# Monkey 2:
# Monkey 3:

# ...

# After round 20, the monkeys are holding items with these worry levels:
# Monkey 0: 10, 12, 14, 26, 34
# Monkey 1: 245, 93, 53, 199, 115
# Monkey 2:
# Monkey 3:
# Chasing all of the monkeys at once is impossible; you're going to have to focus on the two most active monkeys if you want any hope of getting your stuff back. Count the total number of times each monkey inspects items over 20 rounds:

# Monkey 0 inspected items 101 times.
# Monkey 1 inspected items 95 times.
# Monkey 2 inspected items 7 times.
# Monkey 3 inspected items 105 times.
# In this example, the two most active monkeys inspected items 101 and 105 times. The level of monkey business in this situation can be found by multiplying these together: 10605.

# Figure out which monkeys to chase by counting how many items they inspect over 20 rounds. What is the level of monkey business after 20 rounds of stuff-slinging simian shenanigans?

# Your puzzle answer was 182293.

# The first half of this puzzle is complete! It provides one gold star: *

# --- Part Two ---
# You're worried you might not ever get your items back. So worried, in fact, that your relief that a monkey's inspection didn't damage an item no longer causes your worry level to be divided by three.

# Unfortunately, that relief was all that was keeping your worry levels from reaching ridiculous levels. You'll need to find another way to keep your worry levels manageable.

# At this rate, you might be putting up with these monkeys for a very long time - possibly 10000 rounds!

# With these new rules, you can still figure out the monkey business after 10000 rounds. Using the same example above:

# == After round 1 ==
# Monkey 0 inspected items 2 times.
# Monkey 1 inspected items 4 times.
# Monkey 2 inspected items 3 times.
# Monkey 3 inspected items 6 times.

# == After round 20 ==
# Monkey 0 inspected items 99 times.
# Monkey 1 inspected items 97 times.
# Monkey 2 inspected items 8 times.
# Monkey 3 inspected items 103 times.

# == After round 1000 ==
# Monkey 0 inspected items 5204 times.
# Monkey 1 inspected items 4792 times.
# Monkey 2 inspected items 199 times.
# Monkey 3 inspected items 5192 times.

# == After round 2000 ==
# Monkey 0 inspected items 10419 times.
# Monkey 1 inspected items 9577 times.
# Monkey 2 inspected items 392 times.
# Monkey 3 inspected items 10391 times.

# == After round 3000 ==
# Monkey 0 inspected items 15638 times.
# Monkey 1 inspected items 14358 times.
# Monkey 2 inspected items 587 times.
# Monkey 3 inspected items 15593 times.

# == After round 4000 ==
# Monkey 0 inspected items 20858 times.
# Monkey 1 inspected items 19138 times.
# Monkey 2 inspected items 780 times.
# Monkey 3 inspected items 20797 times.

# == After round 5000 ==
# Monkey 0 inspected items 26075 times.
# Monkey 1 inspected items 23921 times.
# Monkey 2 inspected items 974 times.
# Monkey 3 inspected items 26000 times.

# == After round 6000 ==
# Monkey 0 inspected items 31294 times.
# Monkey 1 inspected items 28702 times.
# Monkey 2 inspected items 1165 times.
# Monkey 3 inspected items 31204 times.

# == After round 7000 ==
# Monkey 0 inspected items 36508 times.
# Monkey 1 inspected items 33488 times.
# Monkey 2 inspected items 1360 times.
# Monkey 3 inspected items 36400 times.

# == After round 8000 ==
# Monkey 0 inspected items 41728 times.
# Monkey 1 inspected items 38268 times.
# Monkey 2 inspected items 1553 times.
# Monkey 3 inspected items 41606 times.

# == After round 9000 ==
# Monkey 0 inspected items 46945 times.
# Monkey 1 inspected items 43051 times.
# Monkey 2 inspected items 1746 times.
# Monkey 3 inspected items 46807 times.

# == After round 10000 ==
# Monkey 0 inspected items 52166 times.
# Monkey 1 inspected items 47830 times.
# Monkey 2 inspected items 1938 times.
# Monkey 3 inspected items 52013 times.
# After 10000 rounds, the two most active monkeys inspected items 52166 and 52013 times.
# Multiplying these together, the level of monkey business in this situation is now 2713310158.

# Worry levels are no longer divided by three after each item is inspected; you'll need to find another way to keep your worry levels manageable.
# Starting again from the initial state in your puzzle input, what is the level of monkey business after 10000 rounds?

import sys


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


class Monkey:
    def __init__(self, monkey_index: int) -> None:
        self.index = monkey_index
        self.inspected_count = 0
        self.op_function = None
        self.op_value = None
        self.test_value = None
        self.true_target = None
        self.false_target = None
        self.items = []

    def __repr__(self) -> str:
        return f"<Monkey {self.index} :- holding {len(self.items)}, throwing to {self.true_target},{self.false_target}, inspected={self.inspected_count}>"

    def set_operation(self, operation_function, operation_value):
        self.op_function = operation_function
        self.op_value = operation_value

    def set_test_value(self, test_value):
        self.test_value = test_value

    def set_target_monkey(self, condition, target):
        # make sure we're not throwing to ourselves, would make the logic different later if we are
        assert target != self.index

        if condition:
            self.true_target = target
        else:
            self.false_target = target

    def add_item(self, the_item: int):
        self.items.append(the_item)

    def run_one_round(self, round_no: int, monkeys, big_rounding_value):
        # execute one set of the round logic for this monkey..

        # do something with each Item..
        for this_item in self.items:
            # 1) Inspect the item (execute the operation function)
            new_worry_level = self.op_function(this_item, self.op_value)
            self.inspected_count += 1

            # 2) Get bored (no longer divide by three)
            # new_worry_level //= 3

            # new part, round off to keep it fast
            new_worry_level %= big_rounding_value

            # 3) Decide whether the result is now divisble by whatever this monkey has as the test_value
            # 4) and throw it one way or the other..
            if 0 == new_worry_level % self.test_value:
                monkeys[self.true_target].add_item(new_worry_level)
            else:
                monkeys[self.false_target].add_item(new_worry_level)

        # we have no items left, we threw them all..
        self.items = []

        # and we're done..


def addition_op(current: int, operator_value: int):
    return current + operator_value


def multiplication_op(current: int, operator_value: int):
    return current * operator_value


def square_op(current: int, operator_value):
    return current * current


# Monkey 3:
#   Starting items: 76, 92
#   Operation: new = old + 6
#   Test: divisible by 5
#     If true: throw to monkey 1
#     If false: throw to monkey 6


def load_monkeys(filename: str):
    monkeys = []

    # winch through the file
    this_monkey = None
    with open(filename, "r") as f:
        for this_line in f:
            this_line = this_line.strip()
            # blank lines can be ignored
            if "" != this_line:
                parts = this_line.split(" ")

                # starting a new monkey
                if parts[0] == "Monkey":
                    # ok - if this is Monkey line then we should store the one we're working on and get a clean one..
                    if this_monkey is not None:
                        monkeys.append(this_monkey)
                    # Monkey index..
                    monkey_idx_str = parts[1][:-1]
                    monkey_idx = int(monkey_idx_str)
                    this_monkey = Monkey(monkey_idx)

                # or we have the starting items
                elif parts[0] == "Starting":
                    assert parts[1] == "items:"
                    for this_part in parts[2:]:
                        # this is an item, optionally with a comma at the end..
                        if this_part.endswith(","):
                            this_part = this_part[:-1]
                        this_item = int(this_part)
                        this_monkey.add_item(this_item)

                # or we have the operation..
                elif parts[0] == "Operation:":
                    # check our assumptions
                    assert parts[1] == "new"
                    assert parts[2] == "="
                    assert parts[3] == "old"
                    # and now it's either addition or multiplication
                    assert parts[4] in ["+", "*"]
                    if parts[4] == "+":
                        # plus only has a numerical constant at the end
                        operation_value = int(parts[5])
                        this_monkey.set_operation(addition_op, operation_value)
                    else:
                        if "old" == parts[5]:
                            this_monkey.set_operation(square_op, None)
                        else:
                            operation_value = int(parts[5])
                            this_monkey.set_operation(
                                multiplication_op, operation_value
                            )

                # or we have the Test logic
                elif parts[0] == "Test:":
                    assert parts[1] == "divisible"
                    assert parts[2] == "by"
                    test_value = int(parts[3])
                    this_monkey.set_test_value(test_value)

                # we have the monkey destinations
                elif parts[0] == "If":
                    assert parts[1] in ["true:", "false:"]
                    assert parts[2] == "throw"
                    assert parts[3] == "to"
                    assert parts[4] == "monkey"
                    target_monkey = int(parts[5])
                    target_monkey_condition = "true:" == parts[1]
                    this_monkey.set_target_monkey(
                        target_monkey_condition, target_monkey
                    )
                else:
                    print(f"Absolutely no idea what to do with this line :{this_line}")
                    print(f"")
                    raise Exception("Bad Line")

    # and add the final monkey
    if this_monkey is not None:
        monkeys.append(this_monkey)

    return monkeys


def calculate_monkey_business(monkeys):
    # we need to multiply the two monkeys that have handled the most items..
    most_handled = [x.inspected_count for x in monkeys]
    ordered_most_handled = list(sorted(most_handled, reverse=True))
    print(ordered_most_handled)

    result = ordered_most_handled[0] * ordered_most_handled[1]

    return result


def calculate_monkey_magic_value(monkeys):
    all_divisors = [x.test_value for x in monkeys]
    product = 1
    for this_divisor in all_divisors:
        product *= this_divisor
    return product


def part2(filename: str, rounds: int = 10000):
    # load the monkeys
    monkeys = load_monkeys(filename)
    print(monkeys)

    # calculate the big, scary divisor value
    big_magic_number = calculate_monkey_magic_value(monkeys)

    # execute the rounds of throwing items
    for this_round in range(rounds):
        for this_monkey in monkeys:
            this_monkey.run_one_round(this_round, monkeys, big_magic_number)

        print(f"After round {this_round}")
        if 0 == this_round % 25:
            eprint(f"Round {this_round}")

        for x in monkeys:
            print(f" - {x}")
        print("")

    # calculate the monkey business
    result = calculate_monkey_business(monkeys)

    # and we're done
    print(f"The monkey business score for {filename} is {result}")
    return result


def fastness_logic():
    # checking the fastness logic..
    divisors = [13, 17, 19, 23]
    mega_divisor = 13 * 17 * 19 * 23
    print(f"{divisors} and {mega_divisor}")

    the_value = 0
    while True:
        # check this one..
        chopped_value = the_value % mega_divisor

        # do the relevant maths
        a = [the_value % x for x in divisors]
        b = [chopped_value % x for x in divisors]
        c = [x != y for x, y in zip(a, b)]
        if any(c):
            print(f"It broke here.. {the_value} ({chopped_value}) {a}, {b}, {c}")
            exit(2)

        # checking the multiplication
        ans1 = the_value * 19
        ans2 = chopped_value * 19
        ans1_b = ans1 % mega_divisor
        ans2_b = ans2 % mega_divisor
        if ans1_b != ans2_b:
            print(f"multiply: {ans1} {ans2} {ans1_b} {ans2_b}")
            exit(3)

        ans1 = the_value * the_value
        ans2 = chopped_value * chopped_value
        ans1_b = ans1 % mega_divisor
        ans2_b = ans2 % mega_divisor
        if ans1_b != ans2_b:
            print(f"squared: {ans1} {ans2} {ans1_b} {ans2_b}")
            exit(3)

        # report the values
        if the_value % 1000 == 0:
            print(f"{the_value} ({chopped_value})")

        # next value
        the_value += 1


if __name__ == "__main__":
    sample_filename = "sample.txt"
    filename = "input.txt"
    sample_expected_result = 2713310158

    # fastness_logic()

    sample_actual_result = part2(sample_filename)
    assert sample_actual_result == sample_expected_result

    puzzle_result = part2(filename)
