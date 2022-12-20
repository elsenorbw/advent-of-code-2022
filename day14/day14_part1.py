# --- Day 14: Regolith Reservoir ---
# The distress signal leads you to a giant waterfall! Actually, hang on - the signal seems like 
# it's coming from the waterfall itself, and that doesn't make any sense. However, you do notice 
# a little path that leads behind the waterfall.

# Correction: the distress signal leads you behind a giant waterfall! There seems to be a large 
# cave system here, and the signal definitely leads further inside.

# As you begin to make your way deeper underground, you feel the ground rumble for a moment. Sand begins 
# pouring into the cave! If you don't quickly figure out where the sand is going, you could quickly become 
# trapped!

# Fortunately, your familiarity with analyzing the path of falling material will come in handy here. You 
# scan a two-dimensional vertical slice of the cave above you (your puzzle input) and discover that it is 
# mostly air with structures made of rock.

# Your scan traces the path of each solid rock structure and reports the x,y coordinates that form the 
# shape of the path, where x represents distance to the right and y represents distance down. Each path 
# appears as a single line of text in your scan. After the first point of each path, each point indicates 
# the end of a straight horizontal or vertical line to be drawn from the previous point. For example:

# 498,4 -> 498,6 -> 496,6
# 503,4 -> 502,4 -> 502,9 -> 494,9
# This scan means that there are two paths of rock; the first path consists of two straight lines, and the 
# second path consists of three straight lines. (Specifically, the first path consists of a line of rock 
# from 498,4 through 498,6 and another line of rock from 498,6 through 496,6.)

# The sand is pouring into the cave from point 500,0.

# Drawing rock as #, air as ., and the source of the sand as +, this becomes:


#   4     5  5
#   9     0  0
#   4     0  3
# 0 ......+...
# 1 ..........
# 2 ..........
# 3 ..........
# 4 ....#...##
# 5 ....#...#.
# 6 ..###...#.
# 7 ........#.
# 8 ........#.
# 9 #########.
# Sand is produced one unit at a time, and the next unit of sand is not produced until the previous unit 
# of sand comes to rest. A unit of sand is large enough to fill one tile of air in your scan.

# A unit of sand always falls down one step if possible. If the tile immediately below is blocked 
# (by rock or sand), the unit of sand attempts to instead move diagonally one step down and to the left. 
# If that tile is blocked, the unit of sand attempts to instead move diagonally one step down and to the 
# right. Sand keeps moving as long as it is able to do so, at each step trying to move down, then down-left, 
# then down-right. If all three possible destinations are blocked, the unit of sand comes to rest and no 
# longer moves, at which point the next unit of sand is created back at the source.

# So, drawing sand that has come to rest as o, the first unit of sand simply falls straight down and 
# then stops:

# ......+...
# ..........
# ..........
# ..........
# ....#...##
# ....#...#.
# ..###...#.
# ........#.
# ......o.#.
# #########.
# The second unit of sand then falls straight down, lands on the first one, and then comes to rest to its 
# left:

# ......+...
# ..........
# ..........
# ..........
# ....#...##
# ....#...#.
# ..###...#.
# ........#.
# .....oo.#.
# #########.
# After a total of five units of sand have come to rest, they form this pattern:

# ......+...
# ..........
# ..........
# ..........
# ....#...##
# ....#...#.
# ..###...#.
# ......o.#.
# ....oooo#.
# #########.
# After a total of 22 units of sand:

# ......+...
# ..........
# ......o...
# .....ooo..
# ....#ooo##
# ....#ooo#.
# ..###ooo#.
# ....oooo#.
# ...ooooo#.
# #########.
# Finally, only two more units of sand can possibly come to rest:

# ......+...
# ..........
# ......o...
# .....ooo..
# ....#ooo##
# ...o#ooo#.
# ..###ooo#.
# ....oooo#.
# .o.ooooo#.
# #########.
# Once all 24 units of sand shown above have come to rest, all further sand flows out the bottom, 
# falling into the endless void. Just for fun, the path any new sand takes before falling forever is 
# shown here with ~:

# .......+...
# .......~...
# ......~o...
# .....~ooo..
# ....~#ooo##
# ...~o#ooo#.
# ..~###ooo#.
# ..~..oooo#.
# .~o.ooooo#.
# ~#########.
# ~..........
# ~..........
# ~..........
# Using your scan, simulate the falling sand. How many units of sand come to rest before sand starts 
# flowing into the abyss below?

# To begin, get your puzzle input.


class Cave:
    def __init__(self):
        self.places = dict()
        self.min_x = 90000
        self.max_x = 0
        self.min_y = 90000
        self.max_y = 0

    def store_thing(self, thing, x, y):
        self.places[(x, y)] = thing
        self.min_x = min(self.min_x, x)
        self.min_y = min(self.min_y, y)
        self.max_x = max(self.max_x, x)
        self.max_y = max(self.max_y, y)

    def store_brick(self, x, y):
        self.store_thing('#', x, y)

    def store_sand(self, x, y):
        self.store_thing('o', x, y)

    def can_fall(self, x, y):
        return (x, y) not in self.places

    def add_one_section(self, points):
        # we get a list of (x1,y1), (x2, y2), (x3, y3) etc... 
        # always an orthoganal change at each point

        # so, get to the first place and pop down some brick..
        x, y = points[0]
        self.store_brick(x, y)

        # now, handle each of the remaining waypoints
        target_idx = 1
        while target_idx < len(points):
            # we are now walking to..
            target_x, target_y = points[target_idx]
            # need to decide on our increments..
            # so if we are at x 1000 and the target is 1008 then we need a +1 increment..
            x_inc = target_x - x
            y_inc = target_y - y
            # max moves is 1..
            x_inc = min(1, x_inc)
            x_inc = max(-1, x_inc)
            y_inc = min(1, y_inc)
            y_inc = max(-1, y_inc)

            print(f"walking from {x},{y} to {target_x},{target_y} in increments of {x_inc},{y_inc}")
            # keep looping until we're at the target
            while x != target_x or y != target_y:
                # move and put down bricks
                x += x_inc
                y += y_inc
                self.store_brick(x, y)

            # next target
            target_idx += 1

    def pour_one_sand(self):
        # return True if the sand came to rest, False if it fell forever..
        x, y = 500, 0

        while y < self.max_y:
            # drop further straight ?
            if self.can_fall(x, y + 1):
                y += 1
            elif self.can_fall(x - 1, y + 1):
                y += 1
                x -= 1
            elif self.can_fall(x + 1, y + 1):
                y += 1
                x += 1
            else:
                # can't fall.. sad.
                self.store_sand(x, y)
                return True

        return False


    def pour(self):
        print(f"Pouring the sand.. whoosh..")
        pour_count = 0
        while self.pour_one_sand():
            pour_count += 1
            self.print(f"After {pour_count} drops")
        return pour_count


    def print(self, caption=None):
        print(f"Cave ({self.min_x},{self.min_y})-({self.max_x},{self.max_y}) - {caption}")
        for y in range(self.min_y - 1, self.max_y + 2, 1):
            s = ''
            for x in range(self.min_x - 1, self.max_x + 2, 1):
                key = (x, y)
                if key in self.places:
                    s += self.places[key]
                else:
                    s += '.'
            print(s)
        print("")




def load_cave_from_file(filename: str):
    cave = Cave()

    # winch through the file
    with open(filename, 'r') as f:
        for this_line in f:
            this_line = this_line.strip()
            if '' != this_line:
                # ok, we have a list of coordinates split up by -> 
                parts = this_line.split('->')
                # each of the parts is a pair of integers split by ,
                points = []
                for this_part in parts:
                    coords = this_part.split(',')
                    assert 2 == len(coords)
                    x = int(coords[0].strip())
                    y = int(coords[1].strip())
                    points.append((x, y))
                # now we have the list, add it to the cave
                cave.add_one_section(points)


    return cave


def part1(filename: str):
    # load the cave
    cave = load_cave_from_file(filename)
    cave.print()

    # pour the sand 
    result = cave.pour()

    # return the result 
    print(f"Cave loaded from {filename} allows {result} sand units")
    return result


if __name__ == "__main__":
    puzzle_filename = 'input.txt'
    sample_filename = 'sample.txt'
    sample_expected_result = 24

    sample_actual_result = part1(sample_filename)
    assert sample_actual_result == sample_expected_result

    puzzle_result = part1(puzzle_filename)
