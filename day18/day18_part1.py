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


def count_exposed_faces(cubes):
    total_faces = 0

    for this_cube in cubes:
        # calculate the location of all 6 neighbours..
        a, b, c = this_cube
        offsets = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
        neighbours = [(a+o[0], b+o[1], c+o[2]) for o in offsets]
        present_neighbours = [n for n in neighbours if n in cubes]
        present_neighbour_count = len(present_neighbours)
        total_faces += 6
        total_faces -= present_neighbour_count

    return total_faces

def part1(filename: str):
    # load the cubes
    cubes = load_cubes(filename)

    # count the exposed surfaces
    result = count_exposed_faces(cubes)

    print(f"exposed faces for the shape from {filename} is {result}")
    return result


if __name__ == "__main__":
    sample_filename = 'sample.txt'
    puzzle_filename = 'input.txt'
    sample_expected_result = 64

    sample_actual_result = part1(sample_filename)
    assert sample_actual_result == sample_expected_result

    puzzle_result = part1(puzzle_filename)
