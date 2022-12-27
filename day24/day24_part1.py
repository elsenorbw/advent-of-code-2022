# --- Day 24: Blizzard Basin ---
# With everything replanted for next year (and with elephants and monkeys to tend the grove), you and the Elves leave for the extraction point.

# Partway up the mountain that shields the grove is a flat, open area that serves as the extraction point. It's a bit of a climb, but nothing the expedition can't handle.

# At least, that would normally be true; now that the mountain is covered in snow, things have become more difficult than the Elves are used to.

# As the expedition reaches a valley that must be traversed to reach the extraction site, you find that strong, turbulent winds are pushing small blizzards of snow and sharp ice around the valley. It's a good thing everyone packed warm clothes! To make it across safely, you'll need to find a way to avoid them.

# Fortunately, it's easy to see all of this from the entrance to the valley, so you make a map of the valley and the blizzards (your puzzle input). For example:

# #.#####
# #.....#
# #>....#
# #.....#
# #...v.#
# #.....#
# #####.#
# The walls of the valley are drawn as #; everything else is ground. Clear ground - where there is currently no blizzard - is drawn as .. Otherwise, blizzards are drawn with an arrow indicating their direction of motion: up (^), down (v), left (<), or right (>).

# The above map includes two blizzards, one moving right (>) and one moving down (v). In one minute, each blizzard moves one position in the direction it is pointing:

# #.#####
# #.....#
# #.>...#
# #.....#
# #.....#
# #...v.#
# #####.#
# Due to conservation of blizzard energy, as a blizzard reaches the wall of the valley, a new blizzard forms on the opposite side of the valley moving in the same direction. After another minute, the bottom downward-moving blizzard has been replaced with a new downward-moving blizzard at the top of the valley instead:

# #.#####
# #...v.#
# #..>..#
# #.....#
# #.....#
# #.....#
# #####.#
# Because blizzards are made of tiny snowflakes, they pass right through each other. After another minute, both blizzards temporarily occupy the same position, marked 2:

# #.#####
# #.....#
# #...2.#
# #.....#
# #.....#
# #.....#
# #####.#
# After another minute, the situation resolves itself, giving each blizzard back its personal space:

# #.#####
# #.....#
# #....>#
# #...v.#
# #.....#
# #.....#
# #####.#
# Finally, after yet another minute, the rightward-facing blizzard on the right is replaced with a new one on the left facing the same direction:

# #.#####
# #.....#
# #>....#
# #.....#
# #...v.#
# #.....#
# #####.#
# This process repeats at least as long as you are observing it, but probably forever.

# Here is a more complex example:

# #.######
# #>>.<^<#
# #.<..<<#
# #>v.><>#
# #<^v^^>#
# ######.#
# Your expedition begins in the only non-wall position in the top row and needs to reach the only non-wall position in the bottom row. On each minute, you can move up, down, left, or right, or you can wait in place. You and the blizzards act simultaneously, and you cannot share a position with a blizzard.

# In the above example, the fastest way to reach your goal requires 18 steps. Drawing the position of the expedition as E, one way to achieve this is:

# Initial state:
# #E######
# #>>.<^<#
# #.<..<<#
# #>v.><>#
# #<^v^^>#
# ######.#

# Minute 1, move down:
# #.######
# #E>3.<.#
# #<..<<.#
# #>2.22.#
# #>v..^<#
# ######.#

# Minute 2, move down:
# #.######
# #.2>2..#
# #E^22^<#
# #.>2.^>#
# #.>..<.#
# ######.#

# Minute 3, wait:
# #.######
# #<^<22.#
# #E2<.2.#
# #><2>..#
# #..><..#
# ######.#

# Minute 4, move up:
# #.######
# #E<..22#
# #<<.<..#
# #<2.>>.#
# #.^22^.#
# ######.#

# Minute 5, move right:
# #.######
# #2Ev.<>#
# #<.<..<#
# #.^>^22#
# #.2..2.#
# ######.#

# Minute 6, move right:
# #.######
# #>2E<.<#
# #.2v^2<#
# #>..>2>#
# #<....>#
# ######.#

# Minute 7, move down:
# #.######
# #.22^2.#
# #<vE<2.#
# #>>v<>.#
# #>....<#
# ######.#

# Minute 8, move left:
# #.######
# #.<>2^.#
# #.E<<.<#
# #.22..>#
# #.2v^2.#
# ######.#

# Minute 9, move up:
# #.######
# #<E2>>.#
# #.<<.<.#
# #>2>2^.#
# #.v><^.#
# ######.#

# Minute 10, move right:
# #.######
# #.2E.>2#
# #<2v2^.#
# #<>.>2.#
# #..<>..#
# ######.#

# Minute 11, wait:
# #.######
# #2^E^2>#
# #<v<.^<#
# #..2.>2#
# #.<..>.#
# ######.#

# Minute 12, move down:
# #.######
# #>>.<^<#
# #.<E.<<#
# #>v.><>#
# #<^v^^>#
# ######.#

# Minute 13, move down:
# #.######
# #.>3.<.#
# #<..<<.#
# #>2E22.#
# #>v..^<#
# ######.#

# Minute 14, move right:
# #.######
# #.2>2..#
# #.^22^<#
# #.>2E^>#
# #.>..<.#
# ######.#

# Minute 15, move right:
# #.######
# #<^<22.#
# #.2<.2.#
# #><2>E.#
# #..><..#
# ######.#

# Minute 16, move right:
# #.######
# #.<..22#
# #<<.<..#
# #<2.>>E#
# #.^22^.#
# ######.#

# Minute 17, move down:
# #.######
# #2.v.<>#
# #<.<..<#
# #.^>^22#
# #.2..2E#
# ######.#

# Minute 18, move down:
# #.######
# #>2.<.<#
# #.2v^2<#
# #>..>2>#
# #<....>#
# ######E#
# What is the fewest number of minutes required to avoid the blizzards and reach the goal?

# To begin, get your puzzle input.


class Blizzard:
    def __init__(self, x, y, direction) -> None:
        self.x = x
        self.y = y
        self.direction = direction


def manhattan_distance(a, b):
    x = abs(a[0] - b[0])
    y = abs(a[1] - b[1])
    return x + y


class OrderedExplorer:
    def __init__(self) -> None:
        self.the_items = dict()

    def add_item(self, location, minutes, manhattan_distance):
        if manhattan_distance not in self.the_items:
            self.the_items[manhattan_distance] = list()
        self.the_items[manhattan_distance].append((location, minutes))

    def next_item(self):
        # find the smallest possible manhattan distance
        smallest_manhattan_distance = min(self.the_items.keys())

        # get the first one in the list..
        result = self.the_items[smallest_manhattan_distance][0]
        # and adjust the list
        if 1 == len(self.the_items[smallest_manhattan_distance]):
            # remove the key entirely
            del self.the_items[smallest_manhattan_distance]
        else:
            self.the_items[smallest_manhattan_distance] = self.the_items[
                smallest_manhattan_distance
            ][1:]

        the_full_result = (result[0], result[1], smallest_manhattan_distance)

        return the_full_result

    def has_remaining_items(self):
        return 0 < len(self.the_items.keys())


class Maze:
    def __init__(self) -> None:
        self.locations = dict()
        self.blizzards = list()
        self.x_max = 0
        self.x_min = 90000
        self.y_max = 0
        self.y_min = 90000
        self.start_location = None
        self.end_location = None
        self.blizzard_locations = dict()

    def calculate_blizzards_for_minute(self, the_minute):
        if the_minute not in self.blizzard_locations:
            print(f"Calculating blizzard set for minute {the_minute}")
            blizzard_state = set()
            # for each blizzard..
            for this_blizzard in self.blizzards:
                # walk it the requisite number of times..
                location = (this_blizzard.x, this_blizzard.y)
                increment = this_blizzard.direction

                for this_minute in range(the_minute):
                    x = location[0] + increment[0]
                    y = location[1] + increment[1]
                    # if we stood on a wall then wrap that around..
                    if x == self.x_min:
                        x = self.x_max - 1
                    elif x == self.x_max:
                        x = self.x_min + 1
                    elif y == self.y_min:
                        y = self.y_max - 1
                    elif y == self.y_max:
                        y = self.y_min + 1
                    # wrapping is done.. coolio..
                    location = (x, y)
                # done walking, so store this location..
                blizzard_state.add(location)
            # we have the whole state for this minute.. cache it
            self.blizzard_locations[the_minute] = blizzard_state

        return self.blizzard_locations[the_minute]

    def print(self, the_minute: int = 0):
        blizzards = self.calculate_blizzards_for_minute(the_minute)
        print(
            f"Maze {len(self.locations)} locations, {len(self.blizzards)} blizzards - minute {the_minute}"
        )
        for y in range(self.y_min, self.y_max + 1, 1):
            s = ""
            for x in range(self.x_min, self.x_max + 1, 1):
                key = (x, y)
                if self.start_location == key:
                    s += "S"
                elif self.end_location == key:
                    s += "E"
                else:
                    the_location = self.locations[key]
                    if key in blizzards:
                        s += "B"
                    else:
                        s += the_location
            print(s)

    def store_value(self, x, y, the_value):
        self.locations[(x, y)] = the_value
        self.x_min = min(self.x_min, x)
        self.x_max = max(self.x_max, x)
        self.y_min = min(self.y_min, y)
        self.y_max = max(self.y_max, y)

    def store_wall(self, x, y):
        self.store_value(x, y, "#")

    def store_space(self, x, y):
        self.store_value(x, y, ".")

    def is_space(self, location):
        result = False
        if location in self.locations:
            if "." == self.locations[location]:
                result = True
        return result

    def add_blizzard(self, the_blizzard: Blizzard):
        self.blizzards.append(the_blizzard)

    def get_start_and_finish(self):
        # map is loaded, we need to calculate the start and finish locations..
        for x in range(self.x_min, self.x_max + 1, 1):
            if "." == self.locations[(x, self.y_min)]:
                start_location = (x, self.y_min)
                break
        for x in range(self.x_max, self.x_min - 1, -1):
            if "." == self.locations[(x, self.y_max)]:
                end_location = (x, self.y_max)
                break
        self.start_location = start_location
        self.end_location = end_location
        return start_location, end_location

    def solve(self):
        # solve the maze in the shortest time possible..
        best_so_far = None

        positions_to_evaluate = OrderedExplorer()
        positions_to_evaluate.add_item(
            self.start_location,
            0,
            manhattan_distance(self.start_location, self.end_location),
        )
        duplicate_prevention = set((self.start_location, 0))
        position_idx = 0

        while positions_to_evaluate.has_remaining_items():
            # evaluate this one..
            this_move = positions_to_evaluate.next_item()
            this_location = this_move[0]
            this_minute = this_move[1]
            manhattan_to_target = this_move[2]

            # 1) Is it now too late for this attempt to ever make it ?
            if best_so_far is not None:
                best_possible_from_here = this_minute + manhattan_to_target
                if best_possible_from_here > best_so_far:
                    # no point in continuing, this will never work out..
                    position_idx += 1
                    continue

            # 2) Ok, are we already dead here ?
            blizzards = self.calculate_blizzards_for_minute(this_minute)
            if this_location in blizzards:
                # oopsie poopsie.. we died.
                position_idx += 1
                continue

            # 3) Have we finished ??locations
            if this_location == self.end_location:
                # ah yeah man.. we're out !
                if best_so_far is None or best_so_far > this_minute:
                    print(
                        f"Found a new best route at {this_minute} minutes.. (previous was {best_so_far})"
                    )
                    best_so_far = this_minute
                    position_idx += 1
                    continue

            # ok, we're still alive and it's worth continuing as far as we know.. create new options for every viable direction
            options_from_here = [(1, 0), (0, 1), (0, 0), (0, -1), (-1, 0)]
            option_locations = [
                (x + this_location[0], y + this_location[1])
                for x, y in options_from_here
            ]
            future_blizzards = self.calculate_blizzards_for_minute(this_minute + 1)
            # see if they are possible on the map..
            additional_locations_to_evaluate = [
                (location, this_minute + 1)
                for location in option_locations
                if self.is_space(location)
                and (location, this_minute + 1) not in duplicate_prevention
                and location not in future_blizzards
            ]
            # and add them to the list
            print(
                f"Adding {len(additional_locations_to_evaluate)} to the current list from manhattan {manhattan_to_target}"
            )
            # add em..
            for this_one in additional_locations_to_evaluate:
                this_location = this_one[0]
                this_minutes = this_one[1]
                this_manhattan = manhattan_distance(this_location, self.end_location)
                positions_to_evaluate.add_item(
                    this_location, this_minutes, this_manhattan
                )
            duplicate_prevention.update(additional_locations_to_evaluate)
            # and move on..
            position_idx += 1

        return best_so_far


def load_the_maze(filename: str):
    maze = Maze()
    # munch through the maze file..
    with open(filename, "r") as f:
        y = 0
        for this_line in f:
            this_line = this_line.strip()
            if this_line != "":
                # we have maze data - cool..
                for x, the_tile in enumerate(this_line):
                    # handle each location..
                    if "#" == the_tile:
                        maze.store_wall(x, y)
                    elif "." == the_tile:
                        maze.store_space(x, y)
                    elif the_tile in "<>^v":
                        # this is a blizzard..
                        maze.store_space(
                            x, y
                        )  # this will be walkable once the blizzard moves
                        # and create the blizzard
                        directions = {
                            "<": (-1, 0),
                            ">": (1, 0),
                            "^": (0, -1),
                            "v": (0, 1),
                        }
                        this_direction = directions[the_tile]
                        this_blizzard = Blizzard(x, y, this_direction)
                        maze.add_blizzard(this_blizzard)

                # and next y
                y += 1

    # done loading, calculate the basics..
    maze.get_start_and_finish()

    return maze


def part1(filename: str):
    maze = load_the_maze(filename)
    for the_minute in range(20):
        maze.print(the_minute)

    result = maze.solve()
    print(f"The fastest path across the maze in {filename} is {result} minutes")
    return result


if __name__ == "__main__":
    puzzle_filename = "input.txt"
    sample_filename = "sample.txt"
    sample_expected_result = 18

    sample_actual_result = part1(sample_filename)
    assert sample_expected_result == sample_actual_result

    puzzle_result = part1(puzzle_filename)
