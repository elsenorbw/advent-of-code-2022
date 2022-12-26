# --- Day 23: Unstable Diffusion ---
# You enter a large crater of gray dirt where the grove is supposed to be. All around you, plants you imagine were expected to be full of fruit are instead withered and broken. A large group of Elves has formed in the middle of the grove.

# "...but this volcano has been dormant for months. Without ash, the fruit can't grow!"

# You look up to see a massive, snow-capped mountain towering above you.

# "It's not like there are other active volcanoes here; we've looked everywhere."

# "But our scanners show active magma flows; clearly it's going somewhere."

# They finally notice you at the edge of the grove, your pack almost overflowing from the random star fruit you've been collecting. Behind you, elephants and monkeys explore the grove, looking concerned. Then, the Elves recognize the ash cloud slowly spreading above your recent detour.

# "Why do you--" "How is--" "Did you just--"

# Before any of them can form a complete question, another Elf speaks up: "Okay, new plan. We have almost enough fruit already, and ash from the plume should spread here eventually. If we quickly plant new seedlings now, we can still make it to the extraction point. Spread out!"

# The Elves each reach into their pack and pull out a tiny plant. The plants rely on important nutrients from the ash, so they can't be planted too close together.

# There isn't enough time to let the Elves figure out where to plant the seedlings themselves; you quickly scan the grove (your puzzle input) and note their positions.

# For example:

# ....#..
# ..###.#
# #...#.#
# .#...##
# #.###..
# ##.#.##
# .#..#..
# The scan shows Elves # and empty ground .; outside your scan, more empty ground extends a long way in every direction. The scan is oriented so that north is up; orthogonal directions are written N (north), S (south), W (west), and E (east), while diagonal directions are written NE, NW, SE, SW.

# The Elves follow a time-consuming process to figure out where they should each go; you can speed up this process considerably. The process consists of some number of rounds during which Elves alternate between considering where to move and actually moving.

# During the first half of each round, each Elf considers the eight positions adjacent to themself. If no other Elves are in one of those eight positions, the Elf does not do anything during this round. Otherwise, the Elf looks in each of four directions in the following order and proposes moving one step in the first valid direction:

# If there is no Elf in the N, NE, or NW adjacent positions, the Elf proposes moving north one step.
# If there is no Elf in the S, SE, or SW adjacent positions, the Elf proposes moving south one step.
# If there is no Elf in the W, NW, or SW adjacent positions, the Elf proposes moving west one step.
# If there is no Elf in the E, NE, or SE adjacent positions, the Elf proposes moving east one step.
# After each Elf has had a chance to propose a move, the second half of the round can begin. Simultaneously, each Elf moves to their proposed destination tile if they were the only Elf to propose moving to that position. If two or more Elves propose moving to the same position, none of those Elves move.

# Finally, at the end of the round, the first direction the Elves considered is moved to the end of the list of directions. For example, during the second round, the Elves would try proposing a move to the south first, then west, then east, then north. On the third round, the Elves would first consider west, then east, then north, then south.

# As a smaller example, consider just these five Elves:

# .....
# ..##.
# ..#..
# .....
# ..##.
# .....
# The northernmost two Elves and southernmost two Elves all propose moving north, while the middle Elf cannot move north and proposes moving south. The middle Elf proposes the same destination as the southwest Elf, so neither of them move, but the other three do:

# ..##.
# .....
# ..#..
# ...#.
# ..#..
# .....
# Next, the northernmost two Elves and the southernmost Elf all propose moving south. Of the remaining middle two Elves, the west one cannot move south and proposes moving west, while the east one cannot move south or west and proposes moving east. All five Elves succeed in moving to their proposed positions:

# .....
# ..##.
# .#...
# ....#
# .....
# ..#..
# Finally, the southernmost two Elves choose not to move at all. Of the remaining three Elves, the west one proposes moving west, the east one proposes moving east, and the middle one proposes moving north; all three succeed in moving:

# ..#..
# ....#
# #....
# ....#
# .....
# ..#..
# At this point, no Elves need to move, and so the process ends.

# The larger example above proceeds as follows:

# == Initial State ==
# ..............
# ..............
# .......#......
# .....###.#....
# ...#...#.#....
# ....#...##....
# ...#.###......
# ...##.#.##....
# ....#..#......
# ..............
# ..............
# ..............

# == End of Round 1 ==
# ..............
# .......#......
# .....#...#....
# ...#..#.#.....
# .......#..#...
# ....#.#.##....
# ..#..#.#......
# ..#.#.#.##....
# ..............
# ....#..#......
# ..............
# ..............

# == End of Round 2 ==
# ..............
# .......#......
# ....#.....#...
# ...#..#.#.....
# .......#...#..
# ...#..#.#.....
# .#...#.#.#....
# ..............
# ..#.#.#.##....
# ....#..#......
# ..............
# ..............

# == End of Round 3 ==
# ..............
# .......#......
# .....#....#...
# ..#..#...#....
# .......#...#..
# ...#..#.#.....
# .#..#.....#...
# .......##.....
# ..##.#....#...
# ...#..........
# .......#......
# ..............

# == End of Round 4 ==
# ..............
# .......#......
# ......#....#..
# ..#...##......
# ...#.....#.#..
# .........#....
# .#...###..#...
# ..#......#....
# ....##....#...
# ....#.........
# .......#......
# ..............

# == End of Round 5 ==
# .......#......
# ..............
# ..#..#.....#..
# .........#....
# ......##...#..
# .#.#.####.....
# ...........#..
# ....##..#.....
# ..#...........
# ..........#...
# ....#..#......
# ..............
# After a few more rounds...

# == End of Round 10 ==
# .......#......
# ...........#..
# ..#.#..#......
# ......#.......
# ...#.....#..#.
# .#......##....
# .....##.......
# ..#........#..
# ....#.#..#....
# ..............
# ....#..#..#...
# ..............
# To make sure they're on the right track, the Elves like to check after round 10 that they're making good progress toward covering enough ground. To do this, count the number of empty ground tiles contained by the smallest rectangle that contains every Elf. (The edges of the rectangle should be aligned to the N/S/E/W directions; the Elves do not have the patience to calculate arbitrary rectangles.) In the above example, that rectangle is:

# ......#.....
# ..........#.
# .#.#..#.....
# .....#......
# ..#.....#..#
# #......##...
# ....##......
# .#........#.
# ...#.#..#...
# ............
# ...#..#..#..
# In this region, the number of empty ground tiles is 110.

# Simulate the Elves' process and find the smallest rectangle that contains the Elves after 10 rounds. How many empty ground tiles does that rectangle contain?

# To begin, get your puzzle input.


def load_elves(filename: str):
    result = []

    with open(filename, "r") as f:
        y = -1
        for this_line in f:
            this_line = this_line.strip()
            if "" != this_line:
                y += 1
                for x, the_value in enumerate(this_line):
                    if "#" == the_value:
                        result.append((x, y))

    return result


def field_info(elves):
    # return xmin, xmax, ymin, ymax, free_spaces
    x_min = elves[0][0]
    x_max = x_min
    y_min = elves[0][1]
    y_max = y_min
    for this_elf in elves[1:]:
        x_min = min(x_min, this_elf[0])
        x_max = max(x_max, this_elf[0])
        y_min = min(y_min, this_elf[1])
        y_max = max(y_max, this_elf[1])

    # ok, we have the min, max values...
    x_size = x_max - x_min + 1
    y_size = y_max - y_min + 1
    field_size = x_size * y_size
    elf_count = len(elves)
    free_spaces = field_size - elf_count
    return x_min, x_max, y_min, y_max, free_spaces


def print_elf_field(elves):
    x_min, x_max, y_min, y_max, _ = field_info(elves)
    for y in range(y_min, y_max + 1, 1):
        s = ""
        for x in range(x_min, x_max + 1, 1):
            if (x, y) in elves:
                s += "#"
            else:
                s += "."
        print(s)


def count_dict_for_iterable(iterable):
    counts = {}
    for x in iterable:
        if x not in counts:
            counts[x] = 1
        else:
            counts[x] += 1
    return counts


def walk_the_elves(elves, iteration: int):
    # execute one step of the walk logic and return a new list of elf positions..
    surrounding = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    # moving them into patches for ease of re-use after the initial check..
    directional_check_locations = [
        [0, 1, 2],  # north
        [5, 6, 7],  # south
        [0, 3, 5],  # west
        [2, 4, 7],  # east
    ]
    directional_increments = [
        (0, -1),
        (0, 1),
        (-1, 0),
        (1, 0),
    ]

    planned_moves = {}

    for this_elf in elves:
        elf_x, elf_y = this_elf
        # do I need to move ?
        view_locations = [(x + elf_x, y + elf_y) for x, y in surrounding]
        populated_locations = [(x, y) in elves for x, y in view_locations]
        if not any(populated_locations):
            # nothing near me, staying still
            planned_moves[this_elf] = this_elf
        else:
            # something near me, time to propose a move..
            mover_base = iteration % len(directional_check_locations)
            for i in range(4):
                mover_idx = (mover_base + i) % len(directional_check_locations)
                this_directional_view = [
                    populated_locations[idx]
                    for idx in directional_check_locations[mover_idx]
                ]
                if not any(this_directional_view):
                    # this is the way we will go..
                    increment_x, increment_y = directional_increments[mover_idx]
                    next_x, next_y = elf_x + increment_x, elf_y + increment_y
                    planned_moves[this_elf] = (next_x, next_y)
                    break
            # I guess there's a chance we can't make a move..
            if this_elf not in planned_moves:
                planned_moves[this_elf] = this_elf

    # ok, all the elves have a planned move
    assert len(elves) == len(planned_moves.keys())
    # check for duplicate planned moves and cancel the people with those moves..
    move_counts = count_dict_for_iterable(planned_moves.values())
    for this_elf in planned_moves:
        if 1 < move_counts[planned_moves[this_elf]]:
            # oh no, a clash - no move for you mr. elf
            planned_moves[this_elf] = this_elf

    # and we now have the final list, cool
    result = list(planned_moves.values())
    return result


def part1(filename: str):
    elves = load_elves(filename)
    print(elves)
    print_elf_field(elves)

    # execute 10 iterations of the elf walking logic
    for this_iteration in range(10):
        elves = walk_the_elves(elves, this_iteration)
        print(f"Elves after iteration {this_iteration}")
        print_elf_field(elves)

    # and get the scope of the field
    x_min, x_max, y_min, y_max, free_spaces = field_info(elves)

    result = free_spaces
    print(f"after 10 iterations, the free space in {filename} is {result}")
    return result


if __name__ == "__main__":
    puzzle_filename = "input.txt"
    sample_filename = "sample.txt"
    sample_expected_result = 110

    sample_actual_result = part1(sample_filename)
    assert sample_actual_result == sample_expected_result

    puzzle_result = part1(puzzle_filename)
