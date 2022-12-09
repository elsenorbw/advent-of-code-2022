# --- Day 8: Treetop Tree House ---
# The expedition comes across a peculiar patch of tall trees all planted carefully in a grid. The Elves explain that a previous expedition planted these trees as a
# reforestation effort. Now, they're curious if this would be a good location for a tree house.

# First, determine whether there is enough tree cover here to keep a tree house hidden. To do this, you need to count the number of trees that are visible
# from outside the grid when looking directly along a row or column.

# The Elves have already launched a quadcopter to generate a map with the height of each tree (your puzzle input). For example:

# 30373
# 25512
# 65332
# 33549
# 35390
# Each tree is represented as a single digit whose value is its height, where 0 is the shortest and 9 is the tallest.

# A tree is visible if all of the other trees between it and an edge of the grid are shorter than it. Only consider trees in the same row or column;
# that is, only look up, down, left, or right from any given tree.

# All of the trees around the edge of the grid are visible - since they are already on the edge, there are no trees to block the view.
# In this example, that only leaves the interior nine trees to consider:

# The top-left 5 is visible from the left and top. (It isn't visible from the right or bottom since other trees of height 5 are in the way.)
# The top-middle 5 is visible from the top and right.
# The top-right 1 is not visible from any direction; for it to be visible, there would need to only be trees of height 0 between it and an edge.
# The left-middle 5 is visible, but only from the right.
# The center 3 is not visible from any direction; for it to be visible, there would need to be only trees of at most height 2 between it and an edge.
# The right-middle 3 is visible from the right.
# In the bottom row, the middle 5 is visible, but the 3 and 4 are not.
# With 16 trees visible on the edge and another 5 visible in the interior, a total of 21 trees are visible in this arrangement.

# Consider your map; how many trees are visible from outside the grid?

# Your puzzle answer was 1792.

# The first half of this puzzle is complete! It provides one gold star: *

# --- Part Two ---
# Content with the amount of tree cover available, the Elves just need to know the best spot to build their tree house: 
# they would like to be able to see a lot of trees.

# To measure the viewing distance from a given tree, look up, down, left, and right from that tree; 
# stop if you reach an edge or at the first tree that is the same height or taller than the tree under consideration. 
# (If a tree is right on the edge, at least one of its viewing distances will be zero.)

# The Elves don't care about distant trees taller than those found by the rules above; the proposed tree house has large eaves to keep it dry, so 
# they wouldn't be able to see higher than the tree house anyway.

# In the example above, consider the middle 5 in the second row:

# 30373
# 25512
# 65332
# 33549
# 35390
# Looking up, its view is not blocked; it can see 1 tree (of height 3).
# Looking left, its view is blocked immediately; it can see only 1 tree (of height 5, right next to it).
# Looking right, its view is not blocked; it can see 2 trees.
# Looking down, its view is blocked eventually; it can see 2 trees (one of height 3, then the tree of height 5 that blocks its view).
# A tree's scenic score is found by multiplying together its viewing distance in each of the four directions. For this tree, this is 4 (found by multiplying 1 * 1 * 2 * 2).

# However, you can do even better: consider the tree of height 5 in the middle of the fourth row:

# 30373
# 25512
# 65332
# 33549
# 35390
# Looking up, its view is blocked at 2 trees (by another tree with a height of 5).
# Looking left, its view is not blocked; it can see 2 trees.
# Looking down, its view is also not blocked; it can see 1 tree.
# Looking right, its view is blocked at 2 trees (by a massive tree of height 9).
# This tree's scenic score is 8 (2 * 2 * 1 * 2); this is the ideal spot for the tree house.

# Consider each tree on your map. What is the highest scenic score possible for any tree?


def load_trees(filename: str):
    # return a list of lists for each tree
    result = []
    with open(filename, "r") as f:
        for this_line in f:
            this_line = this_line.strip()
            # if this is a line then let's split it up..
            this_row = list(this_line)
            int_row = [int(x) for x in this_row]
            result.append(int_row)
    return result


def print_trees(trees):
    for this_row in trees:
        s = ""
        for x in this_row:
            s += str(x)
        print(s)
    print("")



def calculate_scenic_in_one_direction(trees, x, y, x_increment, y_increment):

    treehouse_view_height = trees[y][x]
    result = 0

    # take an initial step
    x += x_increment
    y += y_increment

    # get the outside limit
    x_min = 0
    y_min = 0
    x_max = len(trees[0]) - 1
    y_max = len(trees) - 1

    # until we run out of trees to count..
    while x >= x_min and x <= x_max and y >= y_min and y <= y_max:
        # this tree is definitely visible..
        result += 1
        # is this the last one we can see ?
        if trees[y][x] >= treehouse_view_height:
            break

        # next tree
        x += x_increment
        y += y_increment
    
    return result




def calculate_scenic_for_one_spot(trees, x, y):

    left_view = calculate_scenic_in_one_direction(trees, x, y, -1, 0)
    right_view = calculate_scenic_in_one_direction(trees, x, y, 1, 0)
    top_view = calculate_scenic_in_one_direction(trees, x, y, 0, -1)
    bottom_view = calculate_scenic_in_one_direction(trees, x, y, 0, 1)

    result = left_view * right_view * top_view * bottom_view
    print(f"location {x},{y} scores {result} - left={left_view},right={right_view},top={top_view},bottom={bottom_view}")
    return result


def calculate_scenic_locations(trees):
    # generate a list of all the visible tree pairs as (x, y) tuples
    result = {}

    # first, all the outside trees are visible, so add those
    x_min = 0
    y_min = 0
    x_max = len(trees[0]) - 1
    y_max = len(trees) - 1

    print(f"Grid is : {x_min},{y_min} to {x_max},{y_max}")

    # add the freebies..
    for x in range(x_min, x_max + 1, 1):
        result[(x, y_min)] = 0
        result[(x, y_max)] = 0
    for y in range(y_min, y_max + 1, 1):
        result[(x_min, y)] = 0
        result[(x_max, y)] = 0

    # now do the visible calculations for each row and column
    for x in range(x_min + 1, x_max, 1):
        for y in range(y_min + 1, y_max, 1):
            result[(x, y)] = calculate_scenic_for_one_spot(trees, x, y)

    # now trees can obviously be seen from different sides so we need the unique list
    return result


def part2(filename: str):
    trees = load_trees(filename)
    print_trees(trees)

    scenic_trees = calculate_scenic_locations(trees)

    answer = max(scenic_trees.values())
    print(f"The number of visible trees for {filename} is {answer}")
    return answer


if __name__ == "__main__":
    sample_filename = "sample.txt"
    puzzle_filename = "input.txt"
    sample_expected_result = 8

    sample_actual_result = part2(sample_filename)
    assert sample_actual_result == sample_expected_result

    puzzle_result = part2(puzzle_filename)
