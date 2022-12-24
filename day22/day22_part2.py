# --- Day 22: Monkey Map ---
# The monkeys take you on a surprisingly easy trail through the jungle. They're even going in roughly the right direction according to your handheld device's Grove Positioning System.

# As you walk, the monkeys explain that the grove is protected by a force field. To pass through the force field, you have to enter a password; doing so involves tracing a specific path on a strangely-shaped board.

# At least, you're pretty sure that's what you have to do; the elephants aren't exactly fluent in monkey.

# The monkeys give you notes that they took when they last saw the password entered (your puzzle input).

# For example:

#         ...#
#         .#..
#         #...
#         ....
# ...#.......#
# ........#...
# ..#....#....
# ..........#.
#         ...#....
#         .....#..
#         .#......
#         ......#.

# 10R5L5R10L4R5L5
# The first half of the monkeys' notes is a map of the board. It is comprised of a set of open tiles (on which you can move, drawn .) and solid walls (tiles which you cannot enter, drawn #).

# The second half is a description of the path you must follow. It consists of alternating numbers and letters:

# A number indicates the number of tiles to move in the direction you are facing. If you run into a wall, you stop moving forward and continue with the next instruction.
# A letter indicates whether to turn 90 degrees clockwise (R) or counterclockwise (L). Turning happens in-place; it does not change your current tile.
# So, a path like 10R5 means "go forward 10 tiles, then turn clockwise 90 degrees, then go forward 5 tiles".

# You begin the path in the leftmost open tile of the top row of tiles. Initially, you are facing to the right (from the perspective of how the map is drawn).

# If a movement instruction would take you off of the map, you wrap around to the other side of the board. In other words, if your next tile is off of the board,
# you should instead look in the direction opposite of your current facing as far as you can until you find the opposite edge of the board, then reappear there.

# For example, if you are at A and facing to the right, the tile in front of you is marked B; if you are at C and facing down, the tile in front of you is marked D:

#         ...#
#         .#..
#         #...
#         ....
# ...#.D.....#
# ........#...
# B.#....#...A
# .....C....#.
#         ...#....
#         .....#..
#         .#......
#         ......#.
# It is possible for the next tile (after wrapping around) to be a wall; this still counts as there being a wall in front of you, and so movement stops before you actually wrap to the other side of the board.

# By drawing the last facing you had with an arrow on each tile you visit, the full path taken by the above example looks like this:

#         >>v#
#         .#v.
#         #.v.
#         ..v.
# ...#...v..v#
# >>>v...>#.>>
# ..#v...#....
# ...>>>>v..#.
#         ...#....
#         .....#..
#         .#......
#         ......#.
# To finish providing the password to this strange input device, you need to determine numbers for your final row, column, and facing as your final position appears from the perspective of the original map.
# Rows start from 1 at the top and count downward; columns start from 1 at the left and count rightward. (In the above example, row 1, column 1 refers to the empty space with no tile on it in the top-left corner.)
# Facing is 0 for right (>), 1 for down (v), 2 for left (<), and 3 for up (^). The final password is the sum of 1000 times the row, 4 times the column, and the facing.

# In the above example, the final row is 6, the final column is 8, and the final facing is 0. So, the final password is 1000 * 6 + 4 * 8 + 0: 6032.

# Follow the path given in the monkeys' notes. What is the final password?

# Your puzzle answer was 103224.

# The first half of this puzzle is complete! It provides one gold star: *

# --- Part Two ---
# As you reach the force field, you think you hear some Elves in the distance. Perhaps they've already arrived?

# You approach the strange input device, but it isn't quite what the monkeys drew in their notes. Instead, you are met with a large cube; each of its six faces is a square of 50x50 tiles.

# To be fair, the monkeys' map does have six 50x50 regions on it. If you were to carefully fold the map, you should be able to shape it into a cube!

# In the example above, the six (smaller, 4x4) faces of the cube are:

#         1111
#         1111
#         1111
#         1111
# 222233334444
# 222233334444
# 222233334444
# 222233334444
#         55556666
#         55556666
#         55556666
#         55556666
# You still start in the same position and with the same facing as before, but the wrapping rules are different. Now, if you would walk off the board, you instead proceed around the cube. From the perspective of the map, this can look a little strange. In the above example, if you are at A and move to the right, you would arrive at B facing down; if you are at C and move down, you would arrive at D facing up:

#         ...#
#         .#..
#         #...
#         ....
# ...#.......#
# ........#..A
# ..#....#....
# .D........#.
#         ...#..B.
#         .....#..
#         .#......
#         ..C...#.
# Walls still block your path, even if they are on a different face of the cube. If you are at E facing up, your movement is blocked by the wall marked by the arrow:

#         ...#
#         .#..
#      -->#...
#         ....
# ...#..E....#
# ........#...
# ..#....#....
# ..........#.
#         ...#....
#         .....#..
#         .#......
#         ......#.
# Using the same method of drawing the last facing you had with an arrow on each tile you visit, the full path taken by the above example now looks like this:

#         >>v#
#         .#v.
#         #.v.
#         ..v.
# ...#..^...v#
# .>>>>>^.#.>>
# .^#....#....
# .^........#.
#         ...#..v.
#         .....#v.
#         .#v<<<<.
#         ..v...#.
# The final password is still calculated from your final position and facing from the perspective of the map. In this example, the final row is 5, the final column is 7, and the final facing is 3,
# so the final password is 1000 * 5 + 4 * 7 + 3 = 5031.


# Fold the map into a cube, then follow the path given in the monkeys' notes. What is the final password?


from enum import Enum

# class syntax
class Directions(Enum):
    RIGHT = 1001
    LEFT = 1002
    UP = 1003
    DOWN = 1004


def caret_for_direction(d: Directions):
    a = {
        Directions.RIGHT: ">",
        Directions.LEFT: "<",
        Directions.UP: "^",
        Directions.DOWN: "v",
    }
    return a[d]


def get_directional_increments(d: Directions):
    a = {
        Directions.RIGHT: (1, 0),
        Directions.LEFT: (-1, 0),
        Directions.UP: (0, -1),
        Directions.DOWN: (0, 1),
    }
    return a[d]


def turn_right(d: Directions):
    a = {
        Directions.RIGHT: Directions.DOWN,
        Directions.DOWN: Directions.LEFT,
        Directions.LEFT: Directions.UP,
        Directions.UP: Directions.RIGHT,
    }
    return a[d]


def turn_left(d: Directions):
    # lazy..
    return turn_right(turn_right(turn_right(d)))


class Maze:
    def __init__(self) -> None:
        self.locations = dict()
        self.current_position = (-1, -1)
        self.current_facing = Directions.RIGHT
        self.min_x = 9000
        self.max_x = 0
        self.min_y = 9000
        self.max_y = 0
        self.zone_size = None

    def sanity_check(self, wrap_logic_function):
        tests = [
            ((51, 1), Directions.UP, (1, 151), "Top of 1"),
            ((100, 1), Directions.UP, (1, 200), "Top of 1 - rhs"),
            ((51, 1), Directions.LEFT, (1, 150), "Left of 1 - top"),
            ((51, 50), Directions.LEFT, (1, 101), "Left of 1 - bottom"),
            ((1, 151), Directions.LEFT, (51, 1), "Left of 9 - top"),
            ((1, 200), Directions.LEFT, (100, 1), "Left of 9 - bottom"),
            ((1, 200), Directions.DOWN, (101, 1), "Bottom of 9 - left"),
            ((50, 200), Directions.DOWN, (150, 1), "Bottom of 9 - right"),
            ((50, 151), Directions.RIGHT, (51, 150), "Right of 9 - top"),
            ((50, 200), Directions.RIGHT, (100, 150), "Right of 9 - bottom"),
            ((101, 50), Directions.DOWN, (100, 51), "Bottom of 2 - left"),
            ((150, 50), Directions.DOWN, (100, 100), "Bottom of 2 - right"),
            ((101, 1), Directions.UP, (1, 200), "Top of 2 - left"),
            ((150, 1), Directions.UP, (50, 200), "Top of 2 - right"),
            ((150, 1), Directions.RIGHT, (100, 150), "Right of 2 - top"),
            ((150, 50), Directions.RIGHT, (100, 101), "Right of 2 - bottom"),
            ((100, 51), Directions.RIGHT, (101, 50), "Right of 4 - top"),
            ((100, 100), Directions.RIGHT, (150, 50), "Right of 4 - bottom"),
            ((51, 51), Directions.LEFT, (1, 101), "Left of 4 - top"),
            ((51, 100), Directions.LEFT, (50, 101), "Left of 4 - bottom"),
            ((100, 101), Directions.RIGHT, (150, 50), "Right of 7 - top"),
            ((100, 150), Directions.RIGHT, (150, 1), "right of 7 - bottom"),
            ((51, 150), Directions.DOWN, (50, 151), "bottom of 7 - left"),
            ((100, 150), Directions.DOWN, (50, 200), "bottom of 7 - right"),
            ((1, 101), Directions.UP, (51, 51), "top of 6 - left"),
            ((50, 101), Directions.UP, (51, 100), "top of 6 - right"),
            ((1, 101), Directions.LEFT, (51, 50), "left of 6 - top"),
        ]

        for this_test in tests:
            starting_position, direction, expected_position, title = this_test

            # run the logic..
            x, y = starting_position
            zone = self.get_zone_for(x, y)
            zone_x, zone_y = self.current_zone_location_for(x, y)
            # ok, we need to see where this should wrap around to..
            new_zone, new_zone_xy, new_direction = wrap_logic_function(
                starting_position, direction, zone, zone_x, zone_y
            )
            ((51, 1), Directions.LEFT, (1, 150), "Left of 1 - top"),
            # target_zone, (target_zone_x, target_zone_y), target_direction
            new_zone_x, new_zone_y = new_zone_xy
            next_x, next_y = self.location_from_zone(new_zone, new_zone_x, new_zone_y)

            print(
                f"testing {title} - starting at {starting_position} heading {direction}, expecting to end at {expected_position}, actually ended at {next_x, next_y}"
            )
            actual = (next_x, next_y)
            if expected_position != actual:
                self.print_zones(
                    self.zone_size,
                    {starting_position: "A", expected_position: "B", actual: "?"},
                )

            assert expected_position == actual

        print(f"All tests passed..")

    def set_zone_size(self, the_size):
        self.zone_size = the_size
        self.zones_per_line = (self.max_x - self.min_x + 1) // the_size

    def score_current_location(self):
        # The final password is the sum of 1000 times the row, 4 times the column, and the facing.
        # Facing is 0 for right (>), 1 for down (v), 2 for left (<), and 3 for up (^).
        column, row = self.current_position
        facing_values = {
            Directions.RIGHT: 0,
            Directions.DOWN: 1,
            Directions.LEFT: 2,
            Directions.UP: 3,
        }
        facing = facing_values[self.current_facing]

        score = 1000 * row + 4 * column + facing
        return score

    def get_location(self, x, y):
        result = " "
        key = (x, y)
        if key in self.locations:
            result = self.locations[key]
        return result

    def reset_to_start_position(self):
        self.current_facing = Directions.RIGHT
        x = self.min_x
        y = 1
        while "." != self.get_location(x, y):
            x += 1
        self.current_position = (x, y)

    def turn_left(self):
        self.current_facing = turn_left(self.current_facing)

    def turn_right(self):
        self.current_facing = turn_right(self.current_facing)

    def current_zone(self):
        x, y = self.current_position
        return self.get_zone_for(x, y)

    def get_zone_for(self, x, y):
        zone_x = (x - self.min_x) // self.zone_size
        zone_y = (y - self.min_y) // self.zone_size
        zone_location_idx = zone_y * self.zones_per_line + zone_x
        zone_location = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[zone_location_idx]
        return zone_location

    def current_zone_location(self):
        x, y = self.current_position
        return self.current_zone_location_for(x, y)

    def current_zone_location_for(self, x, y):
        zone_x = (x - self.min_x) // self.zone_size
        zone_y = (y - self.min_y) // self.zone_size
        zone_x_start = zone_x * self.zone_size
        zone_y_start = zone_y * self.zone_size
        the_x = x - zone_x_start
        the_y = y - zone_y_start
        return the_x, the_y

    def location_from_zone(self, zone, zone_x_offset, zone_y_offset):
        # calculate real x,y from a zone and a zone x,y
        zone_location_idx = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ".index(zone)
        zone_y = zone_location_idx // self.zones_per_line
        zones_in_y = zone_y * self.zones_per_line
        zone_x = zone_location_idx - zones_in_y
        print(
            f"location from zone.. zone={zone} zone_idx={zone_location_idx} zone_y={zone_y} zone_x={zone_x} zone_x_offset={zone_x_offset},zone_y_offset={zone_y_offset}"
        )
        target_x = (zone_x * self.zone_size) + zone_x_offset
        target_y = (zone_y * self.zone_size) + zone_y_offset
        return target_x, target_y

    def walk(self, steps: int, wrap_logic_function):
        # try to walk forward x paces..
        x_inc, y_inc = get_directional_increments(self.current_facing)
        x, y = self.current_position
        print(f" starting to walk from {x},{y}")
        for this_step in range(steps):
            # find the next location in this direction..
            while True:
                # self.print(f"Stepping - before {this_step}")
                next_x = x + x_inc
                next_y = y + y_inc
                # if next_x < self.min_x:
                #     next_x = self.max_x
                # if next_x > self.max_x:
                #     next_x = self.min_x
                # if next_y < self.min_y:
                #     next_y = self.max_y
                # if next_y > self.max_y:
                #     next_y = self.min_y
                # and we have the location, what's there ?

                key = (next_x, next_y)
                print(f" considering {key} for step {this_step}")

                # have we walked off an edge ?
                new_direction = self.current_facing
                if key not in self.locations:
                    self.print("Walking off the edge", (x, y))
                    zone = self.current_zone()
                    zone_x, zone_y = self.current_zone_location()
                    # ok, we need to see where this should wrap around to..
                    new_zone, new_zone_xy, new_direction = wrap_logic_function(
                        key, self.current_facing, zone, zone_x, zone_y
                    )

                    # target_zone, (target_zone_x, target_zone_y), target_direction
                    new_zone_x, new_zone_y = new_zone_xy
                    next_x, next_y = self.location_from_zone(
                        new_zone, new_zone_x, new_zone_y
                    )

                    self.print("Popped back out", (next_x, next_y))

                # ok, we're in the right place now..
                key = (next_x, next_y)
                x, y = key

                assert key in self.locations

                if key in self.locations:
                    # we have a result..
                    if "#" == self.locations[key]:
                        # this is the end, my friend..
                        return self.current_position
                    elif "." == self.locations[key]:
                        self.current_position = key
                        self.current_facing = new_direction
                        x_inc, y_inc = get_directional_increments(self.current_facing)
                        # and we're onto the next one..
                        break

    def run_instructions(self, the_instructions, wrap_logic_function):
        for this_instruction in the_instructions:
            print(f"Executing {this_instruction}")
            # do the thing..
            if "L" == this_instruction:
                self.turn_left()
            elif "R" == this_instruction:
                self.turn_right()
            else:
                # we are walking..
                self.walk(this_instruction, wrap_logic_function)

            # and print the new state..
            # self.print()

    def set_location(self, x, y, the_value):
        key = (x, y)
        assert key not in self.locations
        self.locations[key] = the_value
        self.min_x = min(self.min_x, x)
        self.max_x = max(self.max_x, x)
        self.min_y = min(self.min_y, y)
        self.max_y = max(self.max_y, y)

    def print_zones(self, zone_size: int, points=None):
        print(f"Maze zones (size {zone_size}x{zone_size})")
        print(f"Maze min/max x : {self.min_x} - {self.max_x}")
        zones_per_line = (self.max_x - self.min_x + 1) // zone_size
        print(f"Maze zones per line : {zones_per_line}")
        for this_y in range(self.min_y, self.max_y + 1, 1):
            s = ""
            for this_x in range(self.min_x, self.max_x + 1, 1):
                key = (this_x, this_y)
                if key not in self.locations:
                    s += " "
                else:
                    zone_x = (this_x - self.min_x) // zone_size
                    zone_y = (this_y - self.min_y) // zone_size
                    zone_location_idx = zone_y * zones_per_line + zone_x
                    zone_location = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[
                        zone_location_idx
                    ]

                    # and just see if we're overriding this
                    if points is not None and key in points:
                        zone_location = points[key]

                    s += str(zone_location)
            print(s)

    def print(self, title=None, highlight=None):
        if title is None:
            print(
                f"Maze with {len(self.locations)} locations, currently at {self.current_position}"
            )
        else:
            print(f"Maze - {title}")

        for this_y in range(self.min_y, self.max_y + 1, 1):
            s = ""
            for this_x in range(self.min_x, self.max_x + 1, 1):
                key = (this_x, this_y)
                if highlight is not None and key == highlight:
                    s += "X"
                elif self.current_position == key:
                    s += caret_for_direction(self.current_facing)
                elif key not in self.locations:
                    s += " "
                else:
                    s += self.locations[key]
            print(s)


def load_maze_instruction_file(filename: str):
    maze = Maze()
    instructions = []

    with open(filename, "r") as f:
        y = 0
        for this_line in f:
            if "" != this_line.strip():
                # ok, either this is an instruction line which starts with a digit..
                if this_line[0].isdigit():
                    # instructions!
                    # print(f"Found instructions:{this_line}")

                    s = ""
                    for this_char in this_line.strip():
                        # if this is a digit then just add it to the string we are building..
                        if this_char.isdigit():
                            s += this_char
                        else:
                            instructions.append(int(s))
                            instructions.append(this_char)
                            s = ""
                    # and store the last one..
                    if s != "":
                        instructions.append(int(s))

                else:
                    # maze line..
                    # print(f"Maze line: {this_line}")
                    y += 1
                    for x, the_value in enumerate(this_line.rstrip(), start=1):
                        if " " != the_value:
                            maze.set_location(x, y, the_value)

    maze.reset_to_start_position()

    return maze, instructions


def part2(filename: str, zone_size: int, wrap_function):
    maze, instructions = load_maze_instruction_file(filename)
    maze.print_zones(zone_size)
    maze.set_zone_size(zone_size)

    maze.sanity_check(wrap_function)

    maze.run_instructions(instructions, wrap_function)

    result = maze.score_current_location()
    print(f"puzzle result for {filename} is {result}")
    return result


def sample_mapper(src, src_facing, zone, zone_x, zone_y, zone_size=4):
    print(
        f"sample mapper: src={src}, src_facing={src_facing} zone={zone}, zone xy={zone_x},{zone_y}"
    )

    if zone == "5":
        if src_facing == Directions.UP:
            # walking off the top of zone 5 takes us to zone 2, on the left, moving right and
            # the x value from the source will be the y value for the target
            target_zone = "2"
            target_zone_x = 1
            target_zone_y = zone_x
            target_direction = Directions.RIGHT
            return target_zone, (target_zone_x, target_zone_y), target_direction

    if zone == "6":
        if src_facing == Directions.RIGHT:
            # walking off the right hand side of 6.. walks you onto B facing down..
            # the top edge is the inverse of the y in zone
            target_zone = "B"
            target_zone_x = zone_size - zone_y + 1
            target_zone_y = 1
            target_direction = Directions.DOWN
            return target_zone, (target_zone_x, target_zone_y), target_direction

    if zone == "A":
        if src_facing == Directions.DOWN:
            # walking off the bottom of A gets you to the bottom of 4, the x flips and the direction is up
            target_zone = "4"
            target_zone_x = zone_size - zone_x + 1
            target_zone_y = zone_size
            target_direction = Directions.UP
            return target_zone, (target_zone_x, target_zone_y), target_direction

    raise Exception(f"sample_mapper: no idea what to do with {zone} and {src_facing}")
    pass


def puzzle_mapper(src, src_facing, zone, zone_x, zone_y, zone_size=50):
    print(
        f"puzzle mapper: src={src}, src_facing={src_facing} zone={zone}, zone xy={zone_x},{zone_y}"
    )
    # leaving 1 UP -> 9, left hand side, going right, y= source x
    if zone == "1":
        if src_facing == Directions.UP:
            target_zone = "9"
            target_zone_x = 1
            target_zone_y = zone_x
            target_direction = Directions.RIGHT
            return target_zone, (target_zone_x, target_zone_y), target_direction
        # 1 LEFT -> left of 6 going right, src bottom= target top
        if src_facing == Directions.LEFT:
            target_zone = "6"
            target_zone_x = 1
            target_zone_y = zone_size - zone_y + 1
            target_direction = Directions.RIGHT
            return target_zone, (target_zone_x, target_zone_y), target_direction

    # and leaving 9 LEFT -> 1, top, going down, x = src y
    if zone == "9":
        if src_facing == Directions.LEFT:
            target_zone = "1"
            target_zone_x = zone_y
            target_zone_y = 1
            target_direction = Directions.DOWN
            return target_zone, (target_zone_x, target_zone_y), target_direction

        # 9 DOWN -> 2 at the top, going down, x=x
        if src_facing == Directions.DOWN:
            target_zone = "2"
            target_zone_x = zone_x
            target_zone_y = 1
            target_direction = Directions.DOWN
            return target_zone, (target_zone_x, target_zone_y), target_direction

        # 9 RIGHT -> 7 at the bottom, going up, x= src y
        if src_facing == Directions.RIGHT:
            target_zone = "7"
            target_zone_x = zone_y
            target_zone_y = zone_size
            target_direction = Directions.UP
            return target_zone, (target_zone_x, target_zone_y), target_direction

    # 2, DOWN -> 4 on the right, going left, target y = src x
    if zone == "2":
        if src_facing == Directions.DOWN:
            target_zone = "4"
            target_zone_x = zone_size
            target_zone_y = zone_x
            target_direction = Directions.LEFT
            return target_zone, (target_zone_x, target_zone_y), target_direction
        # 2, UP -> 9 at the bottom, going up, x=x
        if src_facing == Directions.UP:
            target_zone = "9"
            target_zone_x = zone_x
            target_zone_y = zone_size
            target_direction = Directions.UP
            return target_zone, (target_zone_x, target_zone_y), target_direction
        # 2, RIGHT -> 7 RIGHT going left, src y = inverse target y
        if src_facing == Directions.RIGHT:
            target_zone = "7"
            target_zone_x = zone_size
            target_zone_y = zone_size - zone_y + 1
            target_direction = Directions.LEFT
            return target_zone, (target_zone_x, target_zone_y), target_direction

    # 4, right -> bottom of 2 going up, x on 2 is depth on 4
    if zone == "4":
        if src_facing == Directions.RIGHT:
            target_zone = "2"
            target_zone_x = zone_y
            target_zone_y = zone_size
            target_direction = Directions.UP
            return target_zone, (target_zone_x, target_zone_y), target_direction

        # 4 LEFT -> 6 at the top, going down, x=src y
        if src_facing == Directions.LEFT:
            target_zone = "6"
            target_zone_x = zone_y
            target_zone_y = 1
            target_direction = Directions.DOWN
            return target_zone, (target_zone_x, target_zone_y), target_direction

    # 7 RIGHT -> 2 RIGHT, heading LEFT, y = inverse y
    if zone == "7":
        if src_facing == Directions.RIGHT:
            target_zone = "2"
            target_zone_x = zone_size
            target_zone_y = zone_size - zone_y + 1
            target_direction = Directions.LEFT
            return target_zone, (target_zone_x, target_zone_y), target_direction

        # 7 DOWN -> 9 on the right, going left, y=src x
        if src_facing == Directions.DOWN:
            target_zone = "9"
            target_zone_x = zone_size
            target_zone_y = zone_x
            target_direction = Directions.LEFT
            return target_zone, (target_zone_x, target_zone_y), target_direction

    # 6 UP -> 4 LEFT, heading RIGHT, y = src x
    if zone == "6":
        if src_facing == Directions.UP:
            target_zone = "4"
            target_zone_x = 1
            target_zone_y = zone_x
            target_direction = Directions.RIGHT
            return target_zone, (target_zone_x, target_zone_y), target_direction

        # 6 LEFT -> 1 LEFT going RIGHT y = inverse src y
        if src_facing == Directions.LEFT:
            target_zone = "1"
            target_zone_x = 1
            target_zone_y = zone_size - zone_y + 1
            target_direction = Directions.RIGHT
            return target_zone, (target_zone_x, target_zone_y), target_direction

    raise Exception(f"puzzle_mapper: no idea what to do with {zone} and {src_facing}")


if __name__ == "__main__":
    puzzle_filename = "input.txt"
    sample_filename = "sample.txt"
    sample_expected_result = 5031
    sample_zone_size = 4
    puzzle_zone_size = 50
    sample_map_func = sample_mapper
    puzzle_map_func = puzzle_mapper

    # sample_actual_result = part2(sample_filename, sample_zone_size, sample_map_func)
    # assert sample_actual_result == sample_expected_result

    puzzle_result = part2(puzzle_filename, puzzle_zone_size, puzzle_map_func)
