# --- Day 18: Boiling Boulders ---
# You and the elephants finally reach fresh air. You've emerged near the base of a large volcano 
# that seems to be actively erupting! Fortunately, the lava seems to be flowing away from you and 
# toward the ocean.

# Bits of lava are still being ejected toward you, so you're sheltering in the cavern exit a little 
# longer. Outside the cave, you can see the lava landing in a pond and hear it loudly hissing as it 
# solidifies.

# Depending on the specific compounds in the lava and speed at which it cools, it might be forming 
# obsidian! The cooling rate should be based on the surface area of the lava droplets, so you take a 
# quick scan of a droplet as it flies past you (your puzzle input).

# Because of how quickly the lava is moving, the scan isn't very good; its resolution is quite low 
# and, as a result, it approximates the shape of the lava droplet with 1x1x1 cubes on a 3D grid, each 
# given as its x,y,z position.

# To approximate the surface area, count the number of sides of each cube that are not immediately 
# connected to another cube. So, if your scan were only two adjacent cubes like 1,1,1 and 2,1,1, 
# each cube would have a single side covered and five sides exposed, a total surface area of 10 sides.

# Here's a larger example:

# 2,2,2
# 1,2,2
# 3,2,2
# 2,1,2
# 2,3,2
# 2,2,1
# 2,2,3
# 2,2,4
# 2,2,6
# 1,2,5
# 3,2,5
# 2,1,5
# 2,3,5
# In the above example, after counting up all the sides that aren't connected to another cube, the 
# total surface area is 64.

# What is the surface area of your scanned lava droplet?

# Your puzzle answer was 3522.

# The first half of this puzzle is complete! It provides one gold star: *

# --- Part Two ---
# Something seems off about your calculation. The cooling rate depends on exterior surface area, 
# but your calculation also included the surface area of air pockets trapped in the lava droplet.

# Instead, consider only cube sides that could be reached by the water and steam as the lava droplet 
# tumbles into the pond. The steam will expand to reach as much as possible, completely displacing any 
# air on the outside of the lava droplet but never expanding diagonally.

# In the larger example above, exactly one cube of air is trapped within the lava droplet (at 2,2,5), 
# so the exterior surface area of the lava droplet is 58.

# What is the exterior surface area of your scanned lava droplet?



def load_cubes(filename: str):
    cubes = set()

    with open(filename, 'r') as f:
        for this_line in f:
            this_line = this_line.strip()
            if '' != this_line:
                parts = this_line.split(',')
                int_parts = [int(x) for x in parts]
                cubes.add(tuple(int_parts))

    return cubes


def neighbours_for(location):
    offsets = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    a, b, c = location
    candidates = [(a+o[0], b+o[1], c+o[2]) for o in offsets]
    return candidates

def in_zone(location, min_x, max_x, min_y, max_y, min_z, max_z):
    result = True 
    x, y, z = location
    if x < min_x or x > max_x:
        result = False
    elif y < min_y or y > max_y:
        result = False
    elif z < min_z or z > max_z:
        result = False
    return result

def run_the_steam(cubes):
    # return all the locations where steam can exist (and is therefore counting as an external surface)
    # 1) calculate the current object dimensions
    steam = set()
    min_x = 90000
    max_x = 0
    min_y = 90000
    max_y = 0
    min_z = 90000
    max_z = 0

    for this_cube in cubes:
        min_x = min(this_cube[0], min_x)
        max_x = max(this_cube[0], max_x)
        min_y = min(this_cube[1], min_y)
        max_y = max(this_cube[1], max_y)
        min_z = min(this_cube[2], min_z)
        max_z = max(this_cube[2], max_z)

    # so, we know how big the object is..
    print(f"steam: object dimensions are {min_x},{min_y},{min_z} - {max_x},{max_y},{max_z}")
    # give ourselves a cordon around that..
    min_x -= 1
    min_y -= 1
    min_z -= 1
    max_x += 1
    max_y += 1
    max_z += 1

    # so let's get some steam going from the minimum corner and see which spaces are externally facing
    starting_position = (min_x, min_y, min_z)
    walk_list = [starting_position]
    walk_idx = 0

    while walk_idx < len(walk_list):
        # get the location in question 
        location = walk_list[walk_idx]

        # see if this one can be steam..
        if location not in cubes and location not in steam:
            # this one is steam..
            steam.add(location) 
            # find the 6 neighbours 
            candidates = neighbours_for(location)
            # exclude anything that is outside the cordon zone..
            in_zone_candidates = [x for x in candidates if in_zone(x, min_x, max_x, min_y, max_y, min_z, max_z)]
            # add these ones..
            walk_list.extend(in_zone_candidates)

        # next in the list 
        walk_idx += 1

    return steam

def count_exposed_faces(cubes, steam):
    total_faces = 0

    for this_cube in cubes:
        # calculate the location of all 6 neighbours..
        a, b, c = this_cube
        offsets = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
        neighbours = [(a+o[0], b+o[1], c+o[2]) for o in offsets]
        steam_neighbours = [n for n in neighbours if n in steam]
        total_faces += len(steam_neighbours)

    return total_faces



def part2(filename: str):
    # load the cubes
    cubes = load_cubes(filename)

    steam_cubes = run_the_steam(cubes)

    # count the exposed surfaces
    result = count_exposed_faces(cubes, steam_cubes)

    print(f"exposed faces for the shape from {filename} is {result}")
    return result


if __name__ == "__main__":
    sample_filename = 'sample.txt'
    puzzle_filename = 'input.txt'
    sample_expected_result = 58

    sample_actual_result = part2(sample_filename)
    assert sample_actual_result == sample_expected_result

    puzzle_result = part2(puzzle_filename)
