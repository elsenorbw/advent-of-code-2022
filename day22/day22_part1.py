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

    def walk(self, steps: int):
        # try to walk forward x paces..
        x_inc, y_inc = get_directional_increments(self.current_facing)
        x, y = self.current_position
        print(f" starting to walk from {x},{y}")
        for this_step in range(steps):
            # find the next location in this direction..
            while True:
                x += x_inc
                y += y_inc
                if x < self.min_x:
                    x = self.max_x
                if x > self.max_x:
                    x = self.min_x
                if y < self.min_y:
                    y = self.max_y
                if y > self.max_y:
                    y = self.min_y
                # and we have the location, what's there ?

                key = (x, y)
                print(f" considering {key} for step {this_step}")
                if key in self.locations:
                    # we have a result..
                    if "#" == self.locations[key]:
                        # this is the end, my friend..
                        return self.current_position
                    elif "." == self.locations[key]:
                        self.current_position = key
                        # and we're onto the next one..
                        break

    def run_instructions(self, the_instructions):
        for this_instruction in the_instructions:
            print(f"Executing {this_instruction}")
            # do the thing..
            if "L" == this_instruction:
                self.turn_left()
            elif "R" == this_instruction:
                self.turn_right()
            else:
                # we are walking..
                self.walk(this_instruction)

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

    def print(self):
        print(
            f"Maze with {len(self.locations)} locations, currently at {self.current_position}"
        )
        for this_y in range(self.min_y, self.max_y + 1, 1):
            s = ""
            for this_x in range(self.min_x, self.max_x + 1, 1):
                key = (this_x, this_y)
                if self.current_position == key:
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
                    print(f"Found instructions:{this_line}")

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
                    print(f"Maze line: {this_line}")
                    y += 1
                    for x, the_value in enumerate(this_line, start=1):
                        if " " != the_value:
                            maze.set_location(x, y, the_value)

    maze.reset_to_start_position()

    return maze, instructions


def part1(filename: str):
    maze, instructions = load_maze_instruction_file(filename)
    maze.print()
    print(instructions)

    maze.run_instructions(instructions)

    result = maze.score_current_location()
    print(f"puzzle result for {filename} is {result}")
    return result


if __name__ == "__main__":
    puzzle_filename = "input.txt"
    sample_filename = "sample.txt"
    sample_expected_result = 6032

    sample_actual_result = part1(sample_filename)
    assert sample_actual_result == sample_expected_result

    puzzle_result = part1(puzzle_filename)
