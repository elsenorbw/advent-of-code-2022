# --- Day 16: Proboscidea Volcanium ---
# The sensors have led you to the origin of the distress signal: yet another handheld device, just like the one the Elves gave you. However, you don't see any Elves around; instead, the device is surrounded by elephants! They must have gotten lost in these tunnels, and one of the elephants apparently figured out how to turn on the distress signal.

# The ground rumbles again, much stronger this time. What kind of cave is this, exactly? You scan the cave with your handheld device; it reports mostly igneous rock, some ash, pockets of pressurized gas, magma... this isn't just a cave, it's a volcano!

# You need to get the elephants out of here, quickly. Your device estimates that you have 30 minutes before the volcano erupts, so you don't have time to go back out the way you came in.

# You scan the cave for other options and discover a network of pipes and pressure-release valves. You aren't sure how such a system got into a volcano, but you don't have time to complain; your device produces a report (your puzzle input) of each valve's flow rate if it were opened (in pressure per minute) and the tunnels you could use to move between the valves.

# There's even a valve in the room you and the elephants are currently standing in labeled AA. You estimate it will take you one minute to open a single valve and one minute to follow any tunnel from one valve to another. What is the most pressure you could release?

# For example, suppose you had the following scan output:

# Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
# Valve BB has flow rate=13; tunnels lead to valves CC, AA
# Valve CC has flow rate=2; tunnels lead to valves DD, BB
# Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
# Valve EE has flow rate=3; tunnels lead to valves FF, DD
# Valve FF has flow rate=0; tunnels lead to valves EE, GG
# Valve GG has flow rate=0; tunnels lead to valves FF, HH
# Valve HH has flow rate=22; tunnel leads to valve GG
# Valve II has flow rate=0; tunnels lead to valves AA, JJ
# Valve JJ has flow rate=21; tunnel leads to valve II
# All of the valves begin closed. You start at valve AA, but it must be damaged or jammed or something: its flow rate is 0, so there's no point in opening it. However, you could spend one minute moving to valve BB and another minute opening it; doing so would release pressure during the remaining 28 minutes at a flow rate of 13, a total eventual pressure release of 28 * 13 = 364. Then, you could spend your third minute moving to valve CC and your fourth minute opening it, providing an additional 26 minutes of eventual pressure release at a flow rate of 2, or 52 total pressure released by valve CC.

# Making your way through the tunnels like this, you could probably open many or all of the valves by the time 30 minutes have elapsed. However, you need to release as much pressure as possible, so you'll need to be methodical. Instead, consider this approach:

# == Minute 1 ==
# No valves are open.
# You move to valve DD.

# == Minute 2 ==
# No valves are open.
# You open valve DD.

# == Minute 3 ==
# Valve DD is open, releasing 20 pressure.
# You move to valve CC.

# == Minute 4 ==
# Valve DD is open, releasing 20 pressure.
# You move to valve BB.

# == Minute 5 ==
# Valve DD is open, releasing 20 pressure.
# You open valve BB.

# == Minute 6 ==
# Valves BB and DD are open, releasing 33 pressure.
# You move to valve AA.

# == Minute 7 ==
# Valves BB and DD are open, releasing 33 pressure.
# You move to valve II.

# == Minute 8 ==
# Valves BB and DD are open, releasing 33 pressure.
# You move to valve JJ.

# == Minute 9 ==
# Valves BB and DD are open, releasing 33 pressure.
# You open valve JJ.

# == Minute 10 ==
# Valves BB, DD, and JJ are open, releasing 54 pressure.
# You move to valve II.

# == Minute 11 ==
# Valves BB, DD, and JJ are open, releasing 54 pressure.
# You move to valve AA.

# == Minute 12 ==
# Valves BB, DD, and JJ are open, releasing 54 pressure.
# You move to valve DD.

# == Minute 13 ==
# Valves BB, DD, and JJ are open, releasing 54 pressure.
# You move to valve EE.

# == Minute 14 ==
# Valves BB, DD, and JJ are open, releasing 54 pressure.
# You move to valve FF.

# == Minute 15 ==
# Valves BB, DD, and JJ are open, releasing 54 pressure.
# You move to valve GG.

# == Minute 16 ==
# Valves BB, DD, and JJ are open, releasing 54 pressure.
# You move to valve HH.

# == Minute 17 ==
# Valves BB, DD, and JJ are open, releasing 54 pressure.
# You open valve HH.

# == Minute 18 ==
# Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
# You move to valve GG.

# == Minute 19 ==
# Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
# You move to valve FF.

# == Minute 20 ==
# Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
# You move to valve EE.

# == Minute 21 ==
# Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
# You open valve EE.

# == Minute 22 ==
# Valves BB, DD, EE, HH, and JJ are open, releasing 79 pressure.
# You move to valve DD.

# == Minute 23 ==
# Valves BB, DD, EE, HH, and JJ are open, releasing 79 pressure.
# You move to valve CC.

# == Minute 24 ==
# Valves BB, DD, EE, HH, and JJ are open, releasing 79 pressure.
# You open valve CC.

# == Minute 25 ==
# Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

# == Minute 26 ==
# Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

# == Minute 27 ==
# Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

# == Minute 28 ==
# Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

# == Minute 29 ==
# Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

# == Minute 30 ==
# Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.
# This approach lets you release the most pressure possible in 30 minutes with this valve layout, 1651.

# Work out the steps to release the most pressure in 30 minutes. What is the most pressure you can release?

# To begin, get your puzzle input.


# developer notes:
# expecting to have to run all the scenarios to decide which combo is best.
# my puzzle input has 15 interesting valves (non-zero) so with 30 minutes on the clock we're 
# not getting to the end in every run
# planning on : 
# load the valves and locations
# find the shortest route from each valve to each other valve
# run the various options and see which one gives the best result


class Solution:
    def __init__(self, pressure_released_so_far: int, current_location: str, remaining_time: int, remaining_options, visited_so_far=None):
        self.pressure_released_so_far = pressure_released_so_far
        self.remaining_time = remaining_time
        self.remaining_options = remaining_options
        self.current_location = current_location
        if visited_so_far is None:
            visited_so_far = []
        self.visited_so_far = visited_so_far

    def __repr__(self):
        s = f"<Solution at={self.current_location} released={self.pressure_released_so_far} time_left={self.remaining_time} remaining={self.remaining_options}>"
        return s
    


class Valve:
    def __init__(self, valve_name: str, flow_rate: int, connections):
        self.name = valve_name
        self.flow_rate = flow_rate
        self.connections = connections
        self.distances = None

    def __repr__(self):
        s = f"<Valve {self.name} flow={self.flow_rate} connections={self.connections} distances={self.distances}>"
        return s


class ValveMap:
    def __init__(self):
        self.valves = dict()

    def add_valve(self, the_valve):
        self.valves[the_valve.name] = the_valve

    def print(self):
        print(f"ValveMap:")
        for this_valve in self.valves.values():
            print(f" - {this_valve}")

    def calculate_distances(self):
        # for each of our valves, calculate how far it is to get to every other valve..
        for this_valve in self.valves:
            the_valve = self.valves[this_valve]
            # we need a location and distance object for each 
            best_distances = dict()
            best_distances[this_valve] = 0
            walk_list = [(x, 1) for x in the_valve.connections]
            print(f"calculate_distances - {this_valve} starting with {walk_list}")
            walk_idx = 0
            while walk_idx < len(walk_list):
                # handle this step
                the_destination, the_distance = walk_list[walk_idx]
                if the_destination not in best_distances or                    best_distances[the_destination] > the_distance:
                    # we need to store this one and add all the kids..
                    best_distances[the_destination] = the_distance
                    print(f"calculate_distance - {this_valve} - adding new best for {the_destination} at {the_distance}")
                    next_steps = [(x, the_distance + 1) for x in self.valves[the_destination].connections]
                    print(f"calculate_distance - {this_valve} - adding new steps {next_steps}")
                    walk_list.extend(next_steps)
                # next step
                walk_idx += 1
            # and store the best distances for this valve
            the_valve.distances = best_distances

    def get_distance(self, start_location, end_location):
        return self.valves[start_location].distances[end_location]

    def pressure_release(self):
        # find the most optimal way to open the valves in sequence and release the most pressure
        start_location = 'AA'
        remaining_time = 30
        interesting_valves = [x.name for x in self.valves.values() if x.flow_rate > 0]
        print(f"pressure_release - start={start_location}, remaining_time={remaining_time}, interesting_valves({len(interesting_valves)})={interesting_valves}")

        # create an initial starting solution
        starting_solution = Solution(0, start_location, remaining_time, interesting_valves)

        # handle all the next steps until we run out..
        walk_list = [starting_solution]
        walk_idx = 0
        best_solution = None

        while walk_idx < len(walk_list):
            this_solution = walk_list[walk_idx]
            #print(f"pressure_release - handling {this_solution}")
            can_progress = False
            # ok, look at this one, can we go anywhere else from here ?
            for this_next_option in this_solution.remaining_options:
                # can we get to this location and do something useful ?
                distance_to_target = self.get_distance(this_solution.current_location, this_next_option)
                #print(f"pressure_release - potential_new_target {this_next_option} at a distance of {distance_to_target} (remaining={this_solution.remaining_time})")
                if distance_to_target + 2 <= this_solution.remaining_time:
                    # ok, we can usefully go there and do things..
                    new_remaining_time = this_solution.remaining_time - distance_to_target - 1
                    # calculate how much pressure will be released until the end of the simulation 
                    additional_pressure_released = new_remaining_time * self.valves[this_next_option].flow_rate
                    # fix up the lists..
                    new_visited = this_solution.visited_so_far.copy()
                    new_visited.append(this_next_option)
                    new_remaining_options = this_solution.remaining_options.copy()
                    new_remaining_options.remove(this_next_option)
                    # create the actual object 
                    next_solution = Solution(
                        this_solution.pressure_released_so_far + additional_pressure_released, 
                        this_next_option, 
                        new_remaining_time,
                        new_remaining_options,
                        new_visited
                    )
                    print(f"pressure_release - adding a next step -> {next_solution}")
                    # and add it to the list..
                    walk_list.append(next_solution)
                    can_progress = True
            # can't progress ? this is a response
            if not can_progress:
                # this is an end..
                if best_solution is None:
                    best_solution = this_solution
                    print(f"Initial best solution -> {this_solution}")
                elif this_solution.pressure_released_so_far > best_solution.pressure_released_so_far:
                    best_solution = this_solution
                    print(f"Improved best solution -> {this_solution}")

            # and in any event, off we go
            walk_idx += 1

        return best_solution.pressure_released_so_far


def valve_from_string(s: str):
    # Valve VR has flow rate=11; tunnels lead to valves LH, KV, BP
    assert s.startswith('Valve ')
    # name is always 2 characters..
    the_name = s[6:8]
    
    # split into the bits..
    parts = s.split(';')
    assert len(parts) == 2

    # get the flow rate..
    rate_str = parts[0][23:]
    flow_rate = int(rate_str)

    # and now get the connections list
    connection_list = parts[1][23:]
    targets = connection_list.split(',')
    connections = [t.strip() for t in targets]

    # and build the thing..
    valve = Valve(the_name, flow_rate, connections)
    return valve


def load_valves_from_file(filename: str):
    valvemap = ValveMap()

    with open(filename, 'r') as f:
        for this_line in f:
            this_line = this_line.strip()
            if '' != this_line:
                # turn one line into one valve..
                this_valve = valve_from_string(this_line)
                valvemap.add_valve(this_valve)

    return valvemap


def part1(filename: str):
    # get the valves from the file..
    valvemap = load_valves_from_file(filename)
    valvemap.print()

    # calculate the distances from everywhere to everywhere..
    valvemap.calculate_distances()
    valvemap.print()

    # pressure release..
    result = valvemap.pressure_release()
    print(f"releasing the valves for {filename} gives a max pressure of {result}")
    return result


if __name__ == "__main__":
    sample_filename = 'sample.txt'
    puzzle_filename = 'input.txt'
    sample_expected_result = 1651

    sample_actual_result = part1(sample_filename)
    assert sample_actual_result == sample_expected_result

    puzzle_result = part1(puzzle_filename)

