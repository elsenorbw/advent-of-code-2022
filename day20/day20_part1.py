# --- Day 20: Grove Positioning System ---
# It's finally time to meet back up with the Elves. When you try to contact them, however, you get no reply. Perhaps you're out of range?

# You know they're headed to the grove where the star fruit grows, so if you can figure out where that is, you should be able to meet back up with them.

# Fortunately, your handheld device has a file (your puzzle input) that contains the grove's coordinates! Unfortunately, the file is encrypted - just in case the device were to fall into the wrong hands.

# Maybe you can decrypt it?

# When you were still back at the camp, you overheard some Elves talking about coordinate file encryption. The main operation involved in decrypting the file is called mixing.

# The encrypted file is a list of numbers. To mix the file, move each number forward or backward in the file a number of positions equal to the value of the number being moved.
# The list is circular, so moving a number off one end of the list wraps back around to the other end as if the ends were connected.

# For example, to move the 1 in a sequence like 4, 5, 6, 1, 7, 8, 9, the 1 moves one position forward: 4, 5, 6, 7, 1, 8, 9. To move the -2 in a sequence like 4, -2, 5, 6, 7, 8, 9, the -2 moves
# two positions backward, wrapping around: 4, 5, 6, 7, 8, -2, 9.

# The numbers should be moved in the order they originally appear in the encrypted file. Numbers moving around during the mixing process do not change the order in which the numbers are moved.

# Consider this encrypted file:

# 1
# 2
# -3
# 3
# -2
# 0
# 4
# Mixing this file proceeds as follows:

# Initial arrangement:
# 1, 2, -3, 3, -2, 0, 4

# 1 moves between 2 and -3:
# 2, 1, -3, 3, -2, 0, 4

# 2 moves between -3 and 3:
# 1, -3, 2, 3, -2, 0, 4

# -3 moves between -2 and 0:
# 1, 2, 3, -2, -3, 0, 4

# 3 moves between 0 and 4:
# 1, 2, -2, -3, 0, 3, 4

# -2 moves between 4 and 1:
# 1, 2, -3, 0, 3, 4, -2

# 0 does not move:
# 1, 2, -3, 0, 3, 4, -2

# 4 moves between -3 and 0:
# 1, 2, -3, 4, 0, 3, -2
# Then, the grove coordinates can be found by looking at the 1000th, 2000th, and 3000th numbers after the value 0, wrapping around the list as necessary.
# In the above example, the 1000th number after 0 is 4, the 2000th is -3, and the 3000th is 2; adding these together produces 3.

# Mix your encrypted file exactly once. What is the sum of the three numbers that form the grove coordinates?


def sign_safe_remainder(a, b):
    if a < 0:
        flip_sign = True
        a = -a
    else:
        flip_sign = False
    result = a % b
    if flip_sign:
        result = -result
    return result


class SpanglyNode:
    def __init__(self, parent, the_value) -> None:
        self.value = the_value
        self.left = None
        self.right = None
        self.parent = parent

    def __repr__(self) -> str:
        left_val = None
        right_val = None
        if self.left is not None:
            left_val = self.left.value
        if self.right is not None:
            right_val = self.right.value
        s = f"< {left_val} <--left v={self.value} right--> {right_val} >"
        return s

    def move_yourself(self):
        # move this item self.value positions..
        # positive means move right, negative means move left
        move_amount = self.value
        list_size = self.parent.item_count
        move_amount = sign_safe_remainder(move_amount, list_size - 1)
        # move_amount += list_size - 1
        if 0 != move_amount:
            print(f"Move of {move_amount} for {self.value}")
            # off to the races then
            # first things first, if this is the head then the new head is the one to the right..
            if self.parent.head == self:
                self.parent.head = self.right
            # now, we can remove ourselves from the list where we are..
            self.left.right = self.right
            self.right.left = self.left
            # and now we need to find our target spot..
            target = self
            if move_amount > 0:
                # moving right and placing on the right..
                for x in range(move_amount):
                    target = target.right
                # we have the target, let's go..
                self.right = target.right
                target.right = self
                self.left = target
                self.right.left = self
            else:
                for x in range(abs(move_amount)):
                    target = target.left
                # we know where we're going, inserting on the left..
                self.left = target.left
                target.left = self
                self.right = target
                self.left.right = self
        else:
            print(f"No move for {self.value}")


class SpanglyListThing:
    def __init__(self) -> None:
        self.head = None
        self.item_count = 0

    def add_item_to_end(self, the_item):
        self.item_count += 1
        new_node = SpanglyNode(self, the_item)
        if self.head is None:
            self.head = new_node
            new_node.left = new_node
            new_node.right = new_node
        else:
            new_node.left = self.head.left
            new_node.right = self.head
            if self.head.right == self.head:
                self.head.right = new_node
            self.head.left = new_node
            new_node.left.right = new_node
        return new_node

    def find_value(self, target_value):
        result = None
        if self.head is not None:
            # special case - are we at the value already ?
            if self.head.value == target_value:
                result = self.head
            else:
                target = self.head.right
                while target != self.head:
                    if target.value == target_value:
                        result = target
                        break
                    else:
                        target = target.right
        return result

    def print(self):
        this_node = self.head
        if this_node is not None:
            s = f"{this_node.value} "
            this_node = this_node.right
            while this_node != self.head:
                s += f"{this_node.value} "
                this_node = this_node.right
        print(f"List({self.item_count}): {s}")

    def get_value_at_location(self, the_index: int, start_from):
        actual_moves = the_index % self.item_count
        target = start_from

        for x in range(actual_moves):
            target = target.right
        return target.value


def load_encrypted_file_to_dll(filename: str):
    main_list = SpanglyListThing()
    move_order_list = list()

    with open(filename, "r") as f:
        for this_line in f:
            this_line = this_line.strip()
            if "" != this_line:
                this_val = int(this_line)
                list_node = main_list.add_item_to_end(this_val)
                move_order_list.append(list_node)
                # main_list.print()

    return main_list, move_order_list


def part1(filename: str):

    list_thing, move_order_list = load_encrypted_file_to_dll(filename)
    print(list_thing)
    print(move_order_list)

    # move everything..
    for this_item in move_order_list:
        this_item.move_yourself()
        # list_thing.print()

    # get the values at 1000, 2000, 3000
    locations = [1000, 2000, 3000]
    zero_offset = list_thing.find_value(0)
    location_values = [
        list_thing.get_value_at_location(x, zero_offset) for x in locations
    ]
    location_total = sum(location_values)

    result = location_total
    print(f"The result for {filename} is {result} based on {location_values}")
    return result


if __name__ == "__main__":
    sample_filename = "sample.txt"
    puzzle_filename = "input.txt"
    sample_expected_result = 3

    sample_actual_result = part1(sample_filename)
    assert sample_expected_result == sample_actual_result

    puzzle_result = part1(puzzle_filename)
    assert 872 == puzzle_result
