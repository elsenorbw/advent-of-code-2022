# --- Day 17: Pyroclastic Flow ---
# Your handheld device has located an alternative exit from the cave for you and the elephants. 
# The ground is rumbling almost continuously now, but the strange valves bought you some time. 
# It's definitely getting warmer in here, though.

# The tunnels eventually open into a very tall, narrow chamber. Large, oddly-shaped rocks are 
# falling into the chamber from above, presumably due to all the rumbling. If you can't work 
# out where the rocks will fall next, you might be crushed!

# The five types of rocks have the following peculiar shapes, where # is rock and . is empty space:

# ####

# .#.
# ###
# .#.

# ..#
# ..#
# ###

# #
# #
# #
# #

# ##
# ##
# The rocks fall in the order shown above: first the - shape, then the + shape, and so on. 
# Once the end of the list is reached, the same order repeats: the - shape falls first, sixth, 11th, 16th, etc.

# The rocks don't spin, but they do get pushed around by jets of hot gas coming out of the walls 
# themselves. A quick scan reveals the effect the jets of hot gas will have on the rocks as they 
# fall (your puzzle input).

# For example, suppose this was the jet pattern in your cave:

# >>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>
# In jet patterns, < means a push to the left, while > means a push to the right. The pattern above means 
# that the jets will push a falling rock right, then right, then right, then left, then left, then right, 
# and so on. If the end of the list is reached, it repeats.

# The tall, vertical chamber is exactly seven units wide. Each rock appears so that its left edge is two 
# units away from the left wall and its bottom edge is three units above the highest rock in the room 
# (or the floor, if there isn't one).

# After a rock appears, it alternates between being pushed by a jet of hot gas one unit (in the direction 
# indicated by the next symbol in the jet pattern) and then falling one unit down. If any movement would 
# cause any part of the rock to move into the walls, floor, or a stopped rock, the movement instead does 
# not occur. If a downward movement would have caused a falling rock to move into the floor or an 
# already-fallen rock, the falling rock stops where it is (having landed on something) and a new rock 
# immediately begins falling.

# Drawing falling rocks with @ and stopped rocks with #, the jet pattern in the example above manifests as 
# follows:

# The first rock begins falling:
# |..@@@@.|
# |.......|
# |.......|
# |.......|
# +-------+

# Jet of gas pushes rock right:
# |...@@@@|
# |.......|
# |.......|
# |.......|
# +-------+

# Rock falls 1 unit:
# |...@@@@|
# |.......|
# |.......|
# +-------+

# Jet of gas pushes rock right, but nothing happens:
# |...@@@@|
# |.......|
# |.......|
# +-------+

# Rock falls 1 unit:
# |...@@@@|
# |.......|
# +-------+

# Jet of gas pushes rock right, but nothing happens:
# |...@@@@|
# |.......|
# +-------+

# Rock falls 1 unit:
# |...@@@@|
# +-------+

# Jet of gas pushes rock left:
# |..@@@@.|
# +-------+

# Rock falls 1 unit, causing it to come to rest:
# |..####.|
# +-------+

# A new rock begins falling:
# |...@...|
# |..@@@..|
# |...@...|
# |.......|
# |.......|
# |.......|
# |..####.|
# +-------+

# Jet of gas pushes rock left:
# |..@....|
# |.@@@...|
# |..@....|
# |.......|
# |.......|
# |.......|
# |..####.|
# +-------+

# Rock falls 1 unit:
# |..@....|
# |.@@@...|
# |..@....|
# |.......|
# |.......|
# |..####.|
# +-------+

# Jet of gas pushes rock right:
# |...@...|
# |..@@@..|
# |...@...|
# |.......|
# |.......|
# |..####.|
# +-------+

# Rock falls 1 unit:
# |...@...|
# |..@@@..|
# |...@...|
# |.......|
# |..####.|
# +-------+

# Jet of gas pushes rock left:
# |..@....|
# |.@@@...|
# |..@....|
# |.......|
# |..####.|
# +-------+

# Rock falls 1 unit:
# |..@....|
# |.@@@...|
# |..@....|
# |..####.|
# +-------+

# Jet of gas pushes rock right:
# |...@...|
# |..@@@..|
# |...@...|
# |..####.|
# +-------+

# Rock falls 1 unit, causing it to come to rest:
# |...#...|
# |..###..|
# |...#...|
# |..####.|
# +-------+

# A new rock begins falling:
# |....@..|
# |....@..|
# |..@@@..|
# |.......|
# |.......|
# |.......|
# |...#...|
# |..###..|
# |...#...|
# |..####.|
# +-------+
# The moment each of the next few rocks begins falling, you would see this:

# |..@....|
# |..@....|
# |..@....|
# |..@....|
# |.......|
# |.......|
# |.......|
# |..#....|
# |..#....|
# |####...|
# |..###..|
# |...#...|
# |..####.|
# +-------+

# |..@@...|
# |..@@...|
# |.......|
# |.......|
# |.......|
# |....#..|
# |..#.#..|
# |..#.#..|
# |#####..|
# |..###..|
# |...#...|
# |..####.|
# +-------+

# |..@@@@.|
# |.......|
# |.......|
# |.......|
# |....##.|
# |....##.|
# |....#..|
# |..#.#..|
# |..#.#..|
# |#####..|
# |..###..|
# |...#...|
# |..####.|
# +-------+

# |...@...|
# |..@@@..|
# |...@...|
# |.......|
# |.......|
# |.......|
# |.####..|
# |....##.|
# |....##.|
# |....#..|
# |..#.#..|
# |..#.#..|
# |#####..|
# |..###..|
# |...#...|
# |..####.|
# +-------+

# |....@..|
# |....@..|
# |..@@@..|
# |.......|
# |.......|
# |.......|
# |..#....|
# |.###...|
# |..#....|
# |.####..|
# |....##.|
# |....##.|
# |....#..|
# |..#.#..|
# |..#.#..|
# |#####..|
# |..###..|
# |...#...|
# |..####.|
# +-------+

# |..@....|
# |..@....|
# |..@....|
# |..@....|
# |.......|
# |.......|
# |.......|
# |.....#.|
# |.....#.|
# |..####.|
# |.###...|
# |..#....|
# |.####..|
# |....##.|
# |....##.|
# |....#..|
# |..#.#..|
# |..#.#..|
# |#####..|
# |..###..|
# |...#...|
# |..####.|
# +-------+

# |..@@...|
# |..@@...|
# |.......|
# |.......|
# |.......|
# |....#..|
# |....#..|
# |....##.|
# |....##.|
# |..####.|
# |.###...|
# |..#....|
# |.####..|
# |....##.|
# |....##.|
# |....#..|
# |..#.#..|
# |..#.#..|
# |#####..|
# |..###..|
# |...#...|
# |..####.|
# +-------+

# |..@@@@.|
# |.......|
# |.......|
# |.......|
# |....#..|
# |....#..|
# |....##.|
# |##..##.|
# |######.|
# |.###...|
# |..#....|
# |.####..|
# |....##.|
# |....##.|
# |....#..|
# |..#.#..|
# |..#.#..|
# |#####..|
# |..###..|
# |...#...|
# |..####.|
# +-------+
# To prove to the elephants your simulation is accurate, they want to know how tall the tower will 
# get after 2022 rocks have stopped (but before the 2023rd rock begins falling). In this example, 
# the tower of rocks will be 3068 units tall.

# How many units tall will the tower of rocks be after 2022 rocks have stopped falling?

# Your puzzle answer was 3224.

# The first half of this puzzle is complete! It provides one gold star: *

# --- Part Two ---
# The elephants are not impressed by your simulation. They demand to know how tall the tower will 
# be after 1,000,000,000,000 rocks have stopped! Only then will they feel confident enough to proceed 
# through the cave.

# In the example above, the tower would be 1,514,285,714,288 units tall!

# How tall will the tower be after 1000000000000 rocks have stopped?


class ShapeProvider:
    def __init__(self):
        self.shape_idx = 0
        self.shapes = [
            [(0,0), (1,0), (2,0), (3,0)],
            [(1,0), (0,1), (1,1), (2,1), (1,2)],
            [(2,0), (2,1), (2,2), (0,0), (1,0)],
            [(0,0), (0,1), (0,2), (0,3)],
            [(0,0), (1,0), (0,1), (1,1)]
        ]
        self.shape_heights = [1, 3, 3, 4, 2]

    def next(self):
        result = (self.shapes[self.shape_idx], self.shape_heights[self.shape_idx])
        self.shape_idx += 1
        if self.shape_idx >= len(self.shapes):
            self.shape_idx = 0
        return result



class Tetris:
    def __init__(self, jets_object):
        self.jets = jets_object
        self.shapes = ShapeProvider()
        self.board = set()
        self.current_top = 0

    def store_one_location(self, x, y):
        self.board.add((x, y))
        self.current_top = max(self.current_top, y)

    def store_shape(self, shape, x, y):
        for this_location in shape:
            self.store_one_location(this_location[0] + x, this_location[1] + y)

    def shape_fits(self, shape, x, y):
        # see whether it would make logical sense to allow this shape to exist here
        result = True

        for this_point in shape:
            this_x, this_y = this_point[0]+x, this_point[1]+y
            if (this_x, this_y) in self.board:
                result = False
            elif this_x < 0 or this_x > 6:
                result = False
            elif this_y <= 0:
                result = False

        return result

    def drop_one(self, inhibit_drop=False):
        # get the next shape and height
        shape, shape_height = self.shapes.next()
        x = 2  # Each rock appears so that its left edge is two units away from the left wall 
        
        # this doesn't matter as the shapes logically extend upwards..
        # y = self.current_top + 3 + shape_height  # and its bottom edge is three units above the highest rock in the room
        # so uing the much simpler..
        y = self.current_top + 4

        # keep on moving until we can't..
        done_dropping = inhibit_drop

        while not done_dropping:
            # part 1 - move left/right
            x_increment = self.jets.next_move()
            target_x = x + x_increment
            if self.shape_fits(shape, target_x, y):
                x = target_x
            
            # part 2 - move down..
            target_y = y - 1
            if self.shape_fits(shape, x, target_y):
                y = target_y
            else:
                done_dropping = True

        # and store that shape..
        self.store_shape(shape, x, y)



    def print(self):
        # let's print this tetris gutter..
        print_top = self.current_top + 3
        for y in range(print_top, 0, -1):
            s = f"{y:03d} "
            if y == self.current_top:
                s += '>'
            else:
                s += '|'
            for x in range(7):
                if (x, y) not in self.board:
                    s += '.'
                else:
                    s += '#'
            if y == self.current_top:
                s += '<'
            else:
                s += '|'
            print(s)

        # and print the bottom
        print("000 +-------+")
        print("")



class Jets:
    def __init__(self, jet_string: str):
        self.jets = jet_string
        self.jet_index = 0

    def next_move(self):
        this_move = self.jets[self.jet_index]
        if this_move == '<':
            result = -1
        elif this_move == '>':
            result = 1
        else:
            raise Exception(f"No idea what we're doing with {this_move}")

        # line up the next one..
        self.jet_index += 1
        if self.jet_index >= len(self.jets):
            self.jet_index = 0

        return result

    def jets_were_reset(self):
        return 0 == self.jet_index

    def __repr__(self):
        return f"<Jets current={self.jet_index} jet_count={len(self.jets)}>"



def load_jets_from_file(filename: str):

    jet_string = ''
    with open(filename, 'r') as f:
        for this_line in f:
            this_line = this_line.strip()
            if '' != this_line:
                jet_string += this_line
    # and we're done
    jets = Jets(jet_string)
    return jets


def find_interval(heights):

    biggest_idx = max(heights.keys())
    print(f"find_interval - biggest_idx={biggest_idx}")
    historical_versions = 15
    for window_size in range(1, 100000, 1):
        # we have a window size let's get the last x versions..
        indexes = [biggest_idx - (window_size * x) for x in range(historical_versions)]
        versions = [heights[biggest_idx - (window_size * x)] for x in range(historical_versions)]
        print(f"window_size={window_size} indexes={indexes}, versions={versions}")

        # calculate the differences between the heights..
        diffs = [versions[x-1] - versions[x] for x in range(1, historical_versions, 1)]
        print(f"diffs=[{diffs}]")
        # and see if they are all the same..
        diff_change = [diffs[x-1] - diffs[x] for x in range(1, len(diffs), 1)]
        print(f"diff_change={diff_change}")
        # are they all 0s ?
        zero_diff = [diff_change[x] == 0 for x in range(len(diff_change))]
        print(f"zero_diff={zero_diff}")
        if all(zero_diff):
            print(f"we have a repeating loop here..")
            window_height_increment = diffs[0]
            print(f"window_size={window_size} window_increment={window_height_increment}")
            return window_size, window_height_increment

    raise Exception(f"Unable to find a repeating group in {window_size}")

def part2(filename: str):
    # load the specific jets
    jets = load_jets_from_file(filename)
    print(jets)

    # create a Tetris board
    board = Tetris(jets)
    board.print()

    heights = dict()
    heights[0] = board.current_top

    this_value = 0
    previous_value = 0

    sample_drop_size = 1000000

    # run through a few initial drops..
    for x in range(1, sample_drop_size + 1, 1):
        board.drop_one()
        heights[x] = board.current_top


    # now try and find some repeating groups
    window_size, window_height_increment = find_interval(heights)
    # ok, so we know everything we need to..
    total_rocks_to_drop = 1000000000000
    # so we have the current height, plus we know how many we have dropped so far..
    remaining_rocks_to_drop = total_rocks_to_drop - sample_drop_size
    print(f"remaining rocks to drop={remaining_rocks_to_drop}")
    height_so_far = board.current_top
    print(f"height_so_far={height_so_far}")
    # ok, we can calculate how many remaining 
    remaining_full_windows = remaining_rocks_to_drop // window_size
    print(f"remaining_full_windows={remaining_full_windows}")
    height_so_far += remaining_full_windows * window_height_increment
    print(f"height_so_far={height_so_far}")
    remaining_rocks_to_drop -= remaining_full_windows * window_size
    print(f"remaining_rocks_to_drop={remaining_rocks_to_drop}")

    # so now we need to calculate the difference for the remaining rock drops..
    x = sample_drop_size - window_size
    base_height = heights[x]
    x += remaining_rocks_to_drop
    height_difference = heights[x] - base_height
    height_so_far += height_difference
    print(f"final height {height_so_far}")
    result = height_so_far


    # board.print()
    print(f"height for jets from {filename} is {result}")
    return result

if __name__ == "__main__":
    sample_filename = 'sample.txt'
    puzzle_filename = 'input.txt'
    sample_expected_result = 1514285714288

    sample_result = part2(sample_filename)
    assert sample_result == sample_expected_result

    puzzle_result = part2(puzzle_filename)