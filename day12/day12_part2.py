# --- Day 12: Hill Climbing Algorithm ---
# You try contacting the Elves using your handheld device, but the river you're following must be too low to get a decent signal.

# You ask the device for a heightmap of the surrounding area (your puzzle input). The heightmap shows the local area from above broken into a grid;
# the elevation of each square of the grid is given by a single lowercase letter, where a is the lowest elevation, b is the next-lowest, and so on up to the highest elevation, z.

# Also included on the heightmap are marks for your current position (S) and the location that should get the best signal (E).
# Your current position (S) has elevation a, and the location that should get the best signal (E) has elevation z.

# You'd like to reach E, but to save energy, you should do it in as few steps as possible. During each step, you can move exactly one square up, down, left, or right.
# To avoid needing to get out your climbing gear, the elevation of the destination square can be at most one higher than the elevation of your current square; that is,
# if your current elevation is m, you could step to elevation n, but not to elevation o. (This also means that the elevation of the destination square can be much lower than the elevation of your current square.)

# For example:

# Sabqponm
# abcryxxl
# accszExk
# acctuvwj
# abdefghi
# Here, you start in the top-left corner; your goal is near the middle. You could start by moving down or right, but eventually you'll need to head toward the e at the bottom. From there, you can spiral around to the goal:

# v..v<<<<
# >v.vv<<^
# .>vv>E^^
# ..v>>>^^
# ..>>>>>^
# In the above diagram, the symbols indicate whether the path exits each square moving up (^), down (v), left (<), or right (>). The location that should get the best signal is still E, and . marks unvisited squares.

# This path reaches the goal in 31 steps, the fewest possible.

# What is the fewest steps required to move from your current position to the location that should get the best signal?

# To begin, get your puzzle input.

# Your puzzle answer was 437.

# The first half of this puzzle is complete! It provides one gold star: *

# --- Part Two ---
# As you walk up the hill, you suspect that the Elves will want to turn this into a hiking trail. The beginning isn't very scenic, though; perhaps you can find a better starting point.

# To maximize exercise while hiking, the trail should start as low as possible: elevation a. The goal is still the square marked E.
# However, the trail should still be direct, taking the fewest steps to reach its goal. So, you'll need to find the shortest path from any square at elevation a to the square marked E.

# Again consider the example from above:

# Sabqponm
# abcryxxl
# accszExk
# acctuvwj
# abdefghi
# Now, there are six choices for starting position (five marked a, plus the square marked S that counts as being at elevation a). If you start at the bottom-left square, you can reach the goal most quickly:

# ...v<<<<
# ...vv<<^
# ...v>E^^
# .>v>>>^^
# >^>>>>>^
# This path reaches the goal in only 29 steps, the fewest possible.

# What is the fewest steps required to move starting from any square with elevation a to the location that should get the best signal?


# just want to name my tuple, I'm sure there's some clever language feature for this..
class StepInfo:
    def __init__(self, this_location, came_from, steps_so_far) -> None:
        self.this_location = this_location
        self.came_from = came_from
        self.steps_so_far = steps_so_far

    def __repr__(self):
        s = f"<StepInfo ({self.this_location} at {self.steps_so_far} steps, coming from {self.came_from})>"
        return s


class Maze:
    def __init__(self) -> None:
        self.locations = dict()
        self.exits = dict()
        self.min_x = 0
        self.max_x = 0
        self.min_y = 0
        self.max_y = 0
        self.starting_point = None
        self.ending_point = None

    def store_location(self, x: int, y: int, the_value: str):
        self.min_x = min(x, self.min_x)
        self.max_x = max(x, self.max_x)
        self.min_y = min(y, self.min_y)
        self.max_y = max(y, self.max_y)
        if "S" == the_value:
            self.starting_point = (x, y)
            the_value = "a"  # from the rules, the starting point has elevation a
        elif "E" == the_value:
            self.ending_point = (x, y)
            the_value = (
                "z"  # and again, from the rules, the end point has an elevation of z
            )

        self.locations[(x, y)] = the_value

    def find_low_points(self):
        # return all the locations with a height of 'a'
        low_lands = []
        for location, height in self.locations.items():
            if height == "a":
                low_lands.append(location)

        return low_lands

    def calculate_exits(self):
        # we want a list of potential next steps from any given location
        for x in range(self.min_x, self.max_x + 1, 1):
            for y in range(self.min_y, self.max_y + 1, 1):
                exits = []
                this_location = self.locations[(x, y)]
                # try each orthoganal location
                for x_inc, y_inc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    target_x = x + x_inc
                    target_y = y + y_inc
                    target_key = (target_x, target_y)
                    # does this spot exist ?
                    if target_key in self.locations:
                        target_location = self.locations[target_key]

                        # now the logic, can we get to there from here
                        if ord(target_location) <= ord(this_location) + 1:
                            # sanity check, never cool to move back to the start..
                            if target_location != "S":
                                # this is a valid target move then :)
                                exits.append(target_key)
                self.exits[(x, y)] = exits

    def print(self):
        print(
            f"Maze ({self.max_x} x {self.max_y}) start={self.starting_point}, end={self.ending_point}"
        )
        for y in range(self.min_y, self.max_y + 1, 1):
            s = ""
            for x in range(self.min_x, self.max_x + 1, 1):
                s += self.locations[(x, y)]
            print(s)
        print("")

        print("exits...")
        for y in range(self.min_y, self.max_y + 1, 1):
            s = ""
            for x in range(self.min_x, self.max_x + 1, 1):
                s += str(len(self.exits[(x, y)]))
            print(s)
        print("")

    def get_shortest_route(self, starting_location):
        # ok, let's walk the maze..
        evaluation_list = [
            StepInfo(this_location, starting_location, 1)
            for this_location in self.exits[starting_location]
        ]

        best_routes = dict()

        eval_idx = 0
        while eval_idx < len(evaluation_list):
            # evaluate the next one..
            # 1) Is this the best way to get to this location (so far) ?
            good_move = True
            this_stepinfo = evaluation_list[eval_idx]
            location = this_stepinfo.this_location
            if location not in best_routes:
                best_routes[location] = this_stepinfo
            else:
                # ok, we've already been to this location, but is this route more efficient ?
                current_best = best_routes[location]
                if current_best.steps_so_far > this_stepinfo.steps_so_far:
                    # we're replacing it..
                    best_routes[location] = this_stepinfo
                else:
                    # we have been here before but this is slower, we're done..
                    good_move = False

            # ok, assuming that we made a good move then we should carry on from here..
            if good_move:
                # we want to add all the possible next steps from here into the list to be evaluated..
                new_targets = [
                    StepInfo(target_location, location, this_stepinfo.steps_so_far + 1)
                    for target_location in self.exits[location]
                    if target_location != this_stepinfo.came_from
                ]
                print(f"Found new targets : {new_targets}")
                evaluation_list.extend(new_targets)

            # and whatever happens.. we're moving on..
            eval_idx += 1

        # ok, we've got the best path to everywhere... so what's the answer ?
        if self.ending_point in best_routes:
            destination_info = best_routes[self.ending_point]
            print(f"best for the final location is {destination_info}")
            result = destination_info.steps_so_far
        else:
            print(f"Couldn't get to the end from the given start...")
            result = 123456789
        return result


def load_maze_from_file(filename: str):
    maze = Maze()
    y = 0
    with open(filename, "r") as f:
        for this_line in f:
            this_line = this_line.strip()
            if "" != this_line:
                # so something with this input..
                for x, the_value in enumerate(this_line):
                    maze.store_location(x, y, the_value)

                # and onto the next line..
                y += 1

    # and pre-calculate some stuff..
    maze.calculate_exits()

    return maze


def part2(filename: str):
    # load the maze..
    maze = load_maze_from_file(filename)
    maze.print()

    # ok, going to start with seeing how bad brute force is.. the solver is fairly efficient I think..

    # get all the low-lying lands..
    potential_start_points = maze.find_low_points()
    print(
        f"Considering these locations ({len(potential_start_points)}) -> {potential_start_points}"
    )

    # solve each one
    route_lengths = [maze.get_shortest_route(x) for x in potential_start_points]

    # and get the shortest
    result = min(route_lengths)

    # and we're done..
    print(
        f"The shortest route through the maze in {filename} from any given low region is {result}"
    )
    return result


if __name__ == "__main__":
    puzzle_input = "input.txt"
    sample_input = "sample.txt"
    sample_expected_result = 29

    sample_actual_result = part2(sample_input)
    assert sample_actual_result == sample_expected_result

    puzzle_result = part2(puzzle_input)
