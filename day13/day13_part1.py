# --- Day 13: Distress Signal ---
# You climb the hill and again try contacting the Elves. However, you instead receive a signal you weren't expecting: a distress signal.

# Your handheld device must still not be working properly; the packets from the distress signal got decoded out of order.
# You'll need to re-order the list of received packets (your puzzle input) to decode the message.

# Your list consists of pairs of packets; pairs are separated by a blank line. You need to identify how many pairs of packets are in the right order.

# For example:

# [1,1,3,1,1]
# [1,1,5,1,1]

# [[1],[2,3,4]]
# [[1],4]

# [9]
# [[8,7,6]]

# [[4,4],4,4]
# [[4,4],4,4,4]

# [7,7,7,7]
# [7,7,7]

# []
# [3]

# [[[]]]
# [[]]

# [1,[2,[3,[4,[5,6,7]]]],8,9]
# [1,[2,[3,[4,[5,6,0]]]],8,9]
# Packet data consists of lists and integers. Each list starts with [, ends with ], and contains zero or more comma-separated values (either integers or other lists).
# Each packet is always a list and appears on its own line.

# When comparing two values, the first value is called left and the second value is called right. Then:

# If both values are integers, the lower integer should come first. If the left integer is lower than the right integer, the inputs are in the right order.
# If the left integer is higher than the right integer, the inputs are not in the right order.
# Otherwise, the inputs are the same integer; continue checking the next part of the input.

# If both values are lists, compare the first value of each list, then the second value, and so on.
# If the left list runs out of items first, the inputs are in the right order.
# If the right list runs out of items first, the inputs are not in the right order.
# If the lists are the same length and no comparison makes a decision about the order, continue checking the next part of the input.

# If exactly one value is an integer, convert the integer to a list which contains that integer as its only value, then retry the comparison.
# For example, if comparing [0,0,0] and 2, convert the right value to [2] (a list containing 2); the result is then found by instead comparing [0,0,0] and [2].
# Using these rules, you can determine which of the pairs in the example are in the right order:

# == Pair 1 ==
# - Compare [1,1,3,1,1] vs [1,1,5,1,1]
#   - Compare 1 vs 1
#   - Compare 1 vs 1
#   - Compare 3 vs 5
#     - Left side is smaller, so inputs are in the right order

# == Pair 2 ==
# - Compare [[1],[2,3,4]] vs [[1],4]
#   - Compare [1] vs [1]
#     - Compare 1 vs 1
#   - Compare [2,3,4] vs 4
#     - Mixed types; convert right to [4] and retry comparison
#     - Compare [2,3,4] vs [4]
#       - Compare 2 vs 4
#         - Left side is smaller, so inputs are in the right order

# == Pair 3 ==
# - Compare [9] vs [[8,7,6]]
#   - Compare 9 vs [8,7,6]
#     - Mixed types; convert left to [9] and retry comparison
#     - Compare [9] vs [8,7,6]
#       - Compare 9 vs 8
#         - Right side is smaller, so inputs are not in the right order

# == Pair 4 ==
# - Compare [[4,4],4,4] vs [[4,4],4,4,4]
#   - Compare [4,4] vs [4,4]
#     - Compare 4 vs 4
#     - Compare 4 vs 4
#   - Compare 4 vs 4
#   - Compare 4 vs 4
#   - Left side ran out of items, so inputs are in the right order

# == Pair 5 ==
# - Compare [7,7,7,7] vs [7,7,7]
#   - Compare 7 vs 7
#   - Compare 7 vs 7
#   - Compare 7 vs 7
#   - Right side ran out of items, so inputs are not in the right order

# == Pair 6 ==
# - Compare [] vs [3]
#   - Left side ran out of items, so inputs are in the right order

# == Pair 7 ==
# - Compare [[[]]] vs [[]]
#   - Compare [[]] vs []
#     - Right side ran out of items, so inputs are not in the right order

# == Pair 8 ==
# - Compare [1,[2,[3,[4,[5,6,7]]]],8,9] vs [1,[2,[3,[4,[5,6,0]]]],8,9]
#   - Compare 1 vs 1
#   - Compare [2,[3,[4,[5,6,7]]]] vs [2,[3,[4,[5,6,0]]]]
#     - Compare 2 vs 2
#     - Compare [3,[4,[5,6,7]]] vs [3,[4,[5,6,0]]]
#       - Compare 3 vs 3
#       - Compare [4,[5,6,7]] vs [4,[5,6,0]]
#         - Compare 4 vs 4
#         - Compare [5,6,7] vs [5,6,0]
#           - Compare 5 vs 5
#           - Compare 6 vs 6
#           - Compare 7 vs 0
#             - Right side is smaller, so inputs are not in the right order
# What are the indices of the pairs that are already in the right order? (The first pair has index 1, the second pair has index 2, and so on.)
# In the above example, the pairs in the right order are 1, 2, 4, and 6; the sum of these indices is 13.

# Determine which pairs of packets are already in the right order. What is the sum of the indices of those pairs?

# To begin, get your puzzle input.


from enum import Enum

# class syntax
class PacketType(Enum):
    LIST = 1002
    INT = 1003


class OrderingResult(Enum):
    YES = 100
    NO = 200
    MAYBE = 300


class Packet:
    def __init__(self, node_type, parent=None) -> None:
        self.type = node_type
        self.int_val = None
        self.list_val = []
        self.parent = parent

    def print(self):
        print(f"{self.type}")

    def is_int(self):
        return self.type == PacketType.INT

    def is_list(self):
        return self.type == PacketType.LIST

    def __repr__(self) -> str:
        if self.type == PacketType.LIST:
            s = f"{self.list_val}"
        elif self.type == PacketType.INT:
            s = f"{self.int_val}"
        else:
            s = f"<Packet type={self.type}, int_val={self.int_val}, list_val={self.list_val}>"
        return s

    def add_list_item(self, the_item):
        assert self.type == PacketType.LIST
        self.list_val.append(the_item)

    def get_item(self, idx):
        assert self.type == PacketType.LIST
        return self.list_val[idx]

    def promote_to_list(self):
        assert self.type == PacketType.INT
        result = ListPacket(self.parent)
        result.add_list_item(self)
        return result


class ListPacket(Packet):
    def __init__(self, parent=None) -> None:
        super().__init__(node_type=PacketType.LIST, parent=parent)


class IntPacket(Packet):
    def __init__(self, int_val, parent=None) -> None:
        super().__init__(node_type=PacketType.INT, parent=parent)
        self.int_val = int_val


def packet_from_string(s: str):
    # walk through the string creating nodes as we go..

    # we start with the base list
    the_packet = ListPacket(None)

    # confirm we have the standard thing and chop off the ends..
    assert s[0] == "["
    assert s[-1] == "]"
    print(s)
    s = s[1:-1]
    print(s)

    # let's walk through the string and create / uncreate lists as we're going..
    idx = 0
    while idx < len(s):

        # so far.. what do we have ?
        print(f"Processed {s[:idx]} -> {the_packet}")

        # ok, what is in this location..
        if s[idx].isdigit():
            digits = ""
            while idx < len(s) and s[idx].isdigit():
                digits += s[idx]
                idx += 1
            # add it to the list..
            new_int_node = IntPacket(int(digits), the_packet)
            the_packet.add_list_item(new_int_node)

        # otherwise, we have some other options..
        elif s[idx] == ",":
            idx += 1
        elif s[idx] == "[":
            # new list..
            new_list_node = ListPacket(the_packet)
            the_packet.add_list_item(new_list_node)
            the_packet = new_list_node
            idx += 1
        elif s[idx] == "]":
            # end of a list..
            the_packet = the_packet.parent
            idx += 1
        else:
            print(f"no idea what to do with... {s}")

        # and moving on..

    return the_packet


def load_packet_pairs(filename: str):

    pairs = []

    current_packets = []
    with open(filename, "r") as f:
        for this_line in f:
            this_line = this_line.strip()
            if "" != this_line:
                # load this line into a packet
                this_packet = packet_from_string(this_line)
                # add it to the list
                current_packets.append(this_packet)
                # if we have 2 then we can add the pair to the result..
                if 2 == len(current_packets):
                    pairs.append(tuple(current_packets))
                    current_packets = []

    return pairs


def correct_ordering(left, right):
    # run the ordering logic to determine if the left < right
    # we need to be able to return yes, no and unsure
    for idx in range(max(len(left.list_val), len(right.list_val))):
        # so.. have we run out of one side or another ?
        if idx >= len(left.list_val):
            # the left hand side ran out
            print(f" - ran out of left side - lists are in the correct order")
            return True
        elif idx >= len(right.list_val):
            print(f" - ran out of right side, lists are not in the correct order")
            return False

        # nope, so we have some things to compare..
        # get both items.
        left_item = left.get_item(idx)
        right_item = right.get_item(idx)
        # if they are both integers then it's simple..
        if left_item.is_int() and right_item.is_int():
            print(f" - Compare ints {left_item} and {right_item}")
            # simple logic here -  If the left integer is lower than the right integer, the inputs are in the right order. If the left integer is higher than the right integer, the inputs are not in the right order. Otherwise, the inputs are the same integer; continue checking the next part of the input.
            if left_item.int_val < right_item.int_val:
                print(f" - Left side is smaller, order is correct")
                return True
            elif left_item.int_val > right_item.int_val:
                print(f" - Right side is smaller, order is incorrect")
                return False
        else:
            # we need to compare the two items as lists..
            # one of them may need converting to a list first..
            if left_item.is_int():
                print(f" - promoting {left_item} to a list..")
                left_item = left_item.promote_to_list()
                print(f" - after promotion: {left_item}")
            if right_item.is_int():
                print(f" - promoting {right_item} to a list..")
                right_item = right_item.promote_to_list()
                print(f" - after promotion: {right_item}")

            # and now use that ol recursion spirit..
            sub_result = correct_ordering(left_item, right_item)
            if sub_result is True:
                return True
            elif sub_result is False:
                return False

    # and we couldn't make a decision..
    print(f" - ultimately no decision on this list.")
    return None


def part1(filename: str):
    # load the input to a set of pairs..
    pairs = load_packet_pairs(filename)
    for left, right in pairs:
        print(f" left:{left}")
        print(f"right:{right}")
        print("")

    # run the calculations on each pair..
    correctly_ordered = [correct_ordering(left, right) for left, right in pairs]

    # and now add up the indices of the correctly ordered statements.. 1 based (boo)
    total = 0
    for idx, result in enumerate(correctly_ordered, start=1):
        if result:
            total += idx

    result = total
    print(f"The puzzle result for {filename} is {result}")
    return result


if __name__ == "__main__":
    sample_filename = "sample.txt"
    puzzle_filename = "input.txt"
    sample_expected_result = 13

    sample_result = part1(sample_filename)
    assert sample_result == sample_expected_result

    puzzle_result = part1(puzzle_filename)
