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
# Content with the amount of tree cover available, the Elves just need to know the best spot to build their tree house: they would like to be able to see a lot of trees.

# To measure the viewing distance from a given tree, look up, down, left, and right from that tree; stop if you reach an edge or at the first tree that is the same height or taller than the tree under consideration. (If a tree is right on the edge, at least one of its viewing distances will be zero.)

# The Elves don't care about distant trees taller than those found by the rules above; the proposed tree house has large eaves to keep it dry, so they wouldn't be able to see higher than the tree house anyway.

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


def calculate_visibility_for_one_orth(
    trees, start_x, start_y, x_increment, y_increment, end_x, end_y
):
    result = []
    x = start_x
    y = start_y
    current_tallest_tree = trees[y - y_increment][x - x_increment]

    while x != end_x and y != end_y:
        # handle this spot..
        this_tree = trees[y][x]
        if this_tree > current_tallest_tree:
            print(f"Tree at {x},{y} ({this_tree}) is visible")
            result.append((x, y))
            current_tallest_tree = this_tree

        # move to next spot
        x += x_increment
        y += y_increment

    return result


def calculate_visible_trees(trees):
    # generate a list of all the visible tree pairs as (x, y) tuples
    result = []

    # first, all the outside trees are visible, so add those
    x_min = 0
    y_min = 0
    x_max = len(trees[0]) - 1
    y_max = len(trees) - 1

    print(f"Grid is : {x_min},{y_min} to {x_max},{y_max}")

    # add the freebies..
    for x in range(x_min, x_max + 1, 1):
        result.append((x, y_min))
        result.append((x, y_max))
    for y in range(y_min, y_max + 1, 1):
        result.append((x_min, y))
        result.append((x_max, y))

    # now do the visible calculations for each row and column
    for x in range(x_min + 1, x_max, 1):
        print("From top")
        visible_from_top = calculate_visibility_for_one_orth(
            trees, x, 1, 0, 1, x_max, y_max
        )
        result.extend(visible_from_top)

        print("From bottom")
        visible_from_bottom = calculate_visibility_for_one_orth(
            trees, x, y_max - 1, 0, -1, 0, 0
        )
        result.extend(visible_from_bottom)

    for y in range(y_min + 1, y_max, 1):
        print("From left")
        visible_from_left = calculate_visibility_for_one_orth(
            trees, 1, y, 1, 0, x_max, y_max
        )
        result.extend(visible_from_left)
        print("From right")
        visible_from_right = calculate_visibility_for_one_orth(
            trees, x_max - 1, y, -1, 0, 0, 0
        )
        result.extend(visible_from_right)

    # now trees can obviously be seen from different sides so we need the unique list
    result = list(set(result))
    return result


def part1(filename: str):
    trees = load_trees(filename)
    print_trees(trees)

    vis_trees = calculate_visible_trees(trees)

    answer = len(vis_trees)
    print(f"The number of visible trees for {filename} is {answer}")
    return answer


if __name__ == "__main__":
    sample_filename = "sample.txt"
    puzzle_filename = "input.txt"
    sample_expected_result = 21

    sample_actual_result = part1(sample_filename)
    assert sample_actual_result == sample_expected_result

    puzzle_result = part1(puzzle_filename)
