# --- Day 15: Beacon Exclusion Zone ---
# You feel the ground rumble again as the distress signal leads you to a large network of subterranean 
# tunnels. You don't have time to search them all, but you don't need to: your pack contains a set of 
# deployable sensors that you imagine were originally built to locate lost Elves.

# The sensors aren't very powerful, but that's okay; your handheld device indicates that you're close 
# enough to the source of the distress signal to use them. You pull the emergency sensor system out of 
# your pack, hit the big button on top, and the sensors zoom off down the tunnels.

# Once a sensor finds a spot it thinks will give it a good reading, it attaches itself to a hard surface 
# and begins monitoring for the nearest signal source beacon. Sensors and beacons always exist at integer 
# coordinates. Each sensor knows its own position and can determine the position of a beacon precisely; 
# however, sensors can only lock on to the one beacon closest to the sensor as measured by the 
# Manhattan distance. (There is never a tie where two beacons are the same distance to a sensor.)

# It doesn't take long for the sensors to report back their positions and closest beacons (your puzzle input). 
# For example:

# Sensor at x=2, y=18: closest beacon is at x=-2, y=15
# Sensor at x=9, y=16: closest beacon is at x=10, y=16
# Sensor at x=13, y=2: closest beacon is at x=15, y=3
# Sensor at x=12, y=14: closest beacon is at x=10, y=16
# Sensor at x=10, y=20: closest beacon is at x=10, y=16
# Sensor at x=14, y=17: closest beacon is at x=10, y=16
# Sensor at x=8, y=7: closest beacon is at x=2, y=10
# Sensor at x=2, y=0: closest beacon is at x=2, y=10
# Sensor at x=0, y=11: closest beacon is at x=2, y=10
# Sensor at x=20, y=14: closest beacon is at x=25, y=17
# Sensor at x=17, y=20: closest beacon is at x=21, y=22
# Sensor at x=16, y=7: closest beacon is at x=15, y=3
# Sensor at x=14, y=3: closest beacon is at x=15, y=3
# Sensor at x=20, y=1: closest beacon is at x=15, y=3
# So, consider the sensor at 2,18; the closest beacon to it is at -2,15. For the sensor at 9,16, 
# the closest beacon to it is at 10,16.

# Drawing sensors as S and beacons as B, the above arrangement of sensors and beacons looks like this:

#                1    1    2    2
#      0    5    0    5    0    5
#  0 ....S.......................
#  1 ......................S.....
#  2 ...............S............
#  3 ................SB..........
#  4 ............................
#  5 ............................
#  6 ............................
#  7 ..........S.......S.........
#  8 ............................
#  9 ............................
# 10 ....B.......................
# 11 ..S.........................
# 12 ............................
# 13 ............................
# 14 ..............S.......S.....
# 15 B...........................
# 16 ...........SB...............
# 17 ................S..........B
# 18 ....S.......................
# 19 ............................
# 20 ............S......S........
# 21 ............................
# 22 .......................B....
# This isn't necessarily a comprehensive map of all beacons in the area, though. Because each sensor only identifies its closest beacon, if a sensor detects a beacon, you know there are no other beacons that close or closer to that sensor. There could still be beacons that just happen to not be the closest beacon to any sensor. Consider the sensor at 8,7:

#                1    1    2    2
#      0    5    0    5    0    5
# -2 ..........#.................
# -1 .........###................
#  0 ....S...#####...............
#  1 .......#######........S.....
#  2 ......#########S............
#  3 .....###########SB..........
#  4 ....#############...........
#  5 ...###############..........
#  6 ..#################.........
#  7 .#########S#######S#........
#  8 ..#################.........
#  9 ...###############..........
# 10 ....B############...........
# 11 ..S..###########............
# 12 ......#########.............
# 13 .......#######..............
# 14 ........#####.S.......S.....
# 15 B........###................
# 16 ..........#SB...............
# 17 ................S..........B
# 18 ....S.......................
# 19 ............................
# 20 ............S......S........
# 21 ............................
# 22 .......................B....
# This sensor's closest beacon is at 2,10, and so you know there are no beacons that close or closer 
# (in any positions marked #).

# None of the detected beacons seem to be producing the distress signal, so you'll need to work out 
# where the distress beacon is by working out where it isn't. For now, keep things simple by counting 
# the positions where a beacon cannot possibly be along just a single row.

# So, suppose you have an arrangement of beacons and sensors like in the example above and, just in the 
# row where y=10, you'd like to count the number of positions a beacon cannot possibly exist. The coverage 
# from all sensors near that row looks like this:

#                  1    1    2    2
#        0    5    0    5    0    5
#  9 ...#########################...
# 10 ..####B######################..
# 11 .###S#############.###########.
# In this example, in the row where y=10, there are 26 positions where a beacon cannot be present.

# Consult the report from the sensors you just deployed. In the row where y=2000000, how many positions 
# cannot contain a beacon?

# To begin, get your puzzle input.

# Your puzzle answer was 5256611.

# The first half of this puzzle is complete! It provides one gold star: *

# --- Part Two ---
# Your handheld device indicates that the distress signal is coming from a beacon nearby. 
# The distress beacon is not detected by any sensor, but the distress beacon must have x and y coordinates 
# each no lower than 0 and no larger than 4000000.

# To isolate the distress beacon's signal, you need to determine its tuning frequency, 
# which can be found by multiplying its x coordinate by 4000000 and then adding its y coordinate.

# In the example above, the search space is smaller: instead, the x and y coordinates can each be at most 20. 
# With this reduced search area, there is only a single position that could have a beacon: x=14, y=11. 
# The tuning frequency for this distress beacon is 56000011.

# Find the only possible position for the distress beacon. What is its tuning frequency?


# dev notes: 
# ok, this implies that if we limit the grid width to the specified margins then we should find one row where
# there is a broken pair of ranges covering the specified field, that line and more specifically where it breaks
# will determine where the beacon can be. The program is asking for THE answer, so we can stop when we find one.



class Sensor:
    def __init__(self, x, y, beacon_x, beacon_y):
        self.x = x
        self.y = y
        self.beacon_x = beacon_x
        self.beacon_y = beacon_y
        self.manhattan_range = abs(x - beacon_x) + abs(y - beacon_y)

    def print(self):
        print(f"<Sensor {self.x},{self.y} detects nearest at {self.beacon_x},{self.beacon_y} manhattan={self.manhattan_range}>")

    def __repr__(self):
        s = f"<Sensor {self.x},{self.y} detects nearest at {self.beacon_x},{self.beacon_y} manhattan={self.manhattan_range}>"
        return s

    def exclude_range(self, target_y: int, min_x: int, max_x: int):
        # ok, for the specified y index, which range of positions on the row cannot have a new beacon
        # since we know that the manhattan distance for new beacons must be greater than our current 
        # manhattan distance to the beacon, we can figure out which range of locations on that row
        # are within the current manhattan distance from this sensor..
        result = None
        distance_to_row = abs(target_y - self.y)
        remaining_distance = self.manhattan_range - distance_to_row
        if remaining_distance > 0:
            range_start = self.x - remaining_distance
            range_end = self.x + remaining_distance
            # keep them inside the specified boundaries
            range_start = max(range_start, min_x)
            range_end = min(range_end, max_x)
            # and just check that we're not completely outside the boundaries
            if range_start > max_x or range_end < min_x:
                print(f"Completely discounting range {self.x}+/- {remaining_distance}")
                result = None
            else:
                result = (range_start, range_end)
        return result


def getxy(s: str):
    idx = s.index('x=') + 2
    comma_idx = s.index(', y=')
    xs = s[idx:comma_idx]
    ys = s[comma_idx+4:]
    return int(xs), int(ys)


def sensor_from_line(s: str):
    # line looks like : Sensor at x=2, y=18: closest beacon is at x=-2, y=15
    parts = s.split(':')
    x, y = getxy(parts[0])
    bx, by = getxy(parts[1])
    sensor = Sensor(x, y, bx, by)
    return sensor

def load_sensors_from_file(filename: str):
    sensors = []

    with open(filename, 'r') as f:
        for this_line in f:
            this_line = this_line.strip()
            if '' != this_line:
                # turn a line into a sensor
                this_sensor = sensor_from_line(this_line)
                sensors.append(this_sensor)

    return sensors


def ranges_overlap(a, b):
    # we always want the left-most range in "a"
    if b[0] < a[0]:
        a,b = b,a
    # so, we have a starting on the left-most side..
    # this means that for there to be an overlap, the start of b must be within the range of a
    # if it is not then there is a gap
    # added the +1, it is acceptable for ranges next to each other to be merged providing there is no gap   
    if b[0] <= a[1] + 1:
        result = True
    else:
        result = False
    return result

def range_merge(a, b):
    new_min = min(a[0], b[0])
    new_max = max(a[1], b[1])
    return (new_min, new_max)


def merge_the_ranges(range_list):
    ranges = range_list.copy()

    able_to_merge_something = True # this language is missing do..while

    while able_to_merge_something:
        # haven't merged anything yet this time..
        able_to_merge_something = False

        # Working through the ranges, can we merge this one with any other one ?
        # This loop works backwards towards 1, no sense in comparing the 0th element to nothing
        for candidate_idx in range(len(ranges)-1, 0, -1):
            candidate_range = ranges[candidate_idx]
            # now can we merge this into any other range ?
            for target_idx in range(candidate_idx - 1, -1, -1):
                target_range = ranges[target_idx]
                #print(f"Considering merging candidate {candidate_range}({candidate_idx}) with {target_range}({target_idx})")
                if ranges_overlap(candidate_range, target_range):
                    # it does, cool..
                    new_range = range_merge(candidate_range, target_range)
                    #print(f"range overlap - merging {candidate_range} and {target_range} -> {new_range}")
                    ranges[target_idx] = new_range
                    # and burn the candidate - it has been merged..
                    del ranges[candidate_idx]
                    # and remember that we merged something, it changes things..
                    able_to_merge_something = True
                    # and next in the loop
                    break

    return ranges


def ranges_for_a_given_y(sensors, target_y, min_limit, max_limit):
    # return the ranges, of impossible locatons within the min/max sent..

    # generate all the ranges of banned beacon positions on the given y
    excluded_ranges = [s.exclude_range(target_y, min_limit, max_limit) for s in sensors]
    active_ranges = [r for r in excluded_ranges if r is not None]
    # print(f"ranges_for_a_given_y({target_y})--active-> {active_ranges}")

    # ok, we need to merge any ranges that should merge
    merged_ranges = merge_the_ranges(active_ranges)
    # print(f"ranges_for_a_given_y({target_y})--merged-> {merged_ranges}")
    return merged_ranges


def frequency_for_beacon(x, y):
    return (x * 4000000) + y


def part2(filename: str, max_x: int, max_y: int):
    # load the sensors..
    sensors = load_sensors_from_file(filename)
    print(sensors)

    # gotta catch em all (this feels dumb)
    for this_y in range(max_y + 1):
        # get the ranges for this area
        the_ranges = ranges_for_a_given_y(sensors, this_y, 0, max_x)
        # if we have 2 ranges then we're in the right place..
        if len(the_ranges) == 2:
            print(f"We have found a split range on row {this_y} : {the_ranges}")
            # get the two ranges..
            a = the_ranges[0]
            b = the_ranges[1]
            # we want the smaller finish value and the bigger start value 
            end_of_first_range = min(a[1], b[1])
            start_of_second_range = max(a[0], b[0])
            print(f"We have the target at y={this_y}, between {end_of_first_range} and {start_of_second_range}")
            assert 2 == start_of_second_range - end_of_first_range
            beacon_x = end_of_first_range + 1
            beacon_y = this_y
            beacon_frequency = frequency_for_beacon(beacon_x, beacon_y)
            print(f"The beacon is at {beacon_x}, {beacon_y} with a frequency of {beacon_frequency}")
            break


    result = beacon_frequency
    print(f"puzzle result for {filename} is {result}")
    return result



if __name__ == "__main__":
    sample_filename = 'sample.txt'
    puzzle_filename = 'input.txt'
    sample_y_max_value = 20
    sample_x_max_value = 20
    sample_expected_result = 56000011
    puzzle_y_max_value = 4000000
    puzzle_x_max_value = 4000000

    sample_actual_result = part2(sample_filename, sample_x_max_value, sample_y_max_value)
    assert sample_actual_result == sample_expected_result

    puzzle_result = part2(puzzle_filename, puzzle_x_max_value, puzzle_y_max_value)

