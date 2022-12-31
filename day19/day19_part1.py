# --- Day 19: Not Enough Minerals ---
# Your scans show that the lava did indeed form obsidian!

# The wind has changed direction enough to stop sending lava droplets toward you, so you and the elephants exit the cave. As you do, you notice a collection of geodes around the pond. Perhaps you could use the obsidian to create some geode-cracking robots and break them open?

# To collect the obsidian from the bottom of the pond, you'll need waterproof obsidian-collecting robots. Fortunately, there is an abundant amount of clay nearby that you can use to make them waterproof.

# In order to harvest the clay, you'll need special-purpose clay-collecting robots. To make any type of robot, you'll need ore, which is also plentiful but in the opposite direction from the clay.

# Collecting ore requires ore-collecting robots with big drills. Fortunately, you have exactly one ore-collecting robot in your pack that you can use to kickstart the whole operation.

# Each robot can collect 1 of its resource type per minute. It also takes one minute for the robot factory (also conveniently from your pack) to construct any type of robot, although it consumes the necessary resources available when construction begins.

# The robot factory has many blueprints (your puzzle input) you can choose from, but once you've configured it with a blueprint, you can't change it. You'll need to work out which blueprint is best.

# For example:

# Blueprint 1:
#   Each ore robot costs 4 ore.
#   Each clay robot costs 2 ore.
#   Each obsidian robot costs 3 ore and 14 clay.
#   Each geode robot costs 2 ore and 7 obsidian.

# Blueprint 2:
#   Each ore robot costs 2 ore.
#   Each clay robot costs 3 ore.
#   Each obsidian robot costs 3 ore and 8 clay.
#   Each geode robot costs 3 ore and 12 obsidian.
# (Blueprints have been line-wrapped here for legibility. The robot factory's actual assortment of blueprints are provided one blueprint per line.)

# The elephants are starting to look hungry, so you shouldn't take too long; you need to figure out which blueprint would maximize the number of opened geodes after 24 minutes by figuring out which robots to build and when to build them.

# Using blueprint 1 in the example above, the largest number of geodes you could open in 24 minutes is 9. One way to achieve that is:

# == Minute 1 ==
# 1 ore-collecting robot collects 1 ore; you now have 1 ore.

# == Minute 2 ==
# 1 ore-collecting robot collects 1 ore; you now have 2 ore.

# == Minute 3 ==
# Spend 2 ore to start building a clay-collecting robot.
# 1 ore-collecting robot collects 1 ore; you now have 1 ore.
# The new clay-collecting robot is ready; you now have 1 of them.

# == Minute 4 ==
# 1 ore-collecting robot collects 1 ore; you now have 2 ore.
# 1 clay-collecting robot collects 1 clay; you now have 1 clay.

# == Minute 5 ==
# Spend 2 ore to start building a clay-collecting robot.
# 1 ore-collecting robot collects 1 ore; you now have 1 ore.
# 1 clay-collecting robot collects 1 clay; you now have 2 clay.
# The new clay-collecting robot is ready; you now have 2 of them.

# == Minute 6 ==
# 1 ore-collecting robot collects 1 ore; you now have 2 ore.
# 2 clay-collecting robots collect 2 clay; you now have 4 clay.

# == Minute 7 ==
# Spend 2 ore to start building a clay-collecting robot.
# 1 ore-collecting robot collects 1 ore; you now have 1 ore.
# 2 clay-collecting robots collect 2 clay; you now have 6 clay.
# The new clay-collecting robot is ready; you now have 3 of them.

# == Minute 8 ==
# 1 ore-collecting robot collects 1 ore; you now have 2 ore.
# 3 clay-collecting robots collect 3 clay; you now have 9 clay.

# == Minute 9 ==
# 1 ore-collecting robot collects 1 ore; you now have 3 ore.
# 3 clay-collecting robots collect 3 clay; you now have 12 clay.

# == Minute 10 ==
# 1 ore-collecting robot collects 1 ore; you now have 4 ore.
# 3 clay-collecting robots collect 3 clay; you now have 15 clay.

# == Minute 11 ==
# Spend 3 ore and 14 clay to start building an obsidian-collecting robot.
# 1 ore-collecting robot collects 1 ore; you now have 2 ore.
# 3 clay-collecting robots collect 3 clay; you now have 4 clay.
# The new obsidian-collecting robot is ready; you now have 1 of them.

# == Minute 12 ==
# Spend 2 ore to start building a clay-collecting robot.
# 1 ore-collecting robot collects 1 ore; you now have 1 ore.
# 3 clay-collecting robots collect 3 clay; you now have 7 clay.
# 1 obsidian-collecting robot collects 1 obsidian; you now have 1 obsidian.
# The new clay-collecting robot is ready; you now have 4 of them.

# == Minute 13 ==
# 1 ore-collecting robot collects 1 ore; you now have 2 ore.
# 4 clay-collecting robots collect 4 clay; you now have 11 clay.
# 1 obsidian-collecting robot collects 1 obsidian; you now have 2 obsidian.

# == Minute 14 ==
# 1 ore-collecting robot collects 1 ore; you now have 3 ore.
# 4 clay-collecting robots collect 4 clay; you now have 15 clay.
# 1 obsidian-collecting robot collects 1 obsidian; you now have 3 obsidian.

# == Minute 15 ==
# Spend 3 ore and 14 clay to start building an obsidian-collecting robot.
# 1 ore-collecting robot collects 1 ore; you now have 1 ore.
# 4 clay-collecting robots collect 4 clay; you now have 5 clay.
# 1 obsidian-collecting robot collects 1 obsidian; you now have 4 obsidian.
# The new obsidian-collecting robot is ready; you now have 2 of them.

# == Minute 16 ==
# 1 ore-collecting robot collects 1 ore; you now have 2 ore.
# 4 clay-collecting robots collect 4 clay; you now have 9 clay.
# 2 obsidian-collecting robots collect 2 obsidian; you now have 6 obsidian.

# == Minute 17 ==
# 1 ore-collecting robot collects 1 ore; you now have 3 ore.
# 4 clay-collecting robots collect 4 clay; you now have 13 clay.
# 2 obsidian-collecting robots collect 2 obsidian; you now have 8 obsidian.

# == Minute 18 ==
# Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
# 1 ore-collecting robot collects 1 ore; you now have 2 ore.
# 4 clay-collecting robots collect 4 clay; you now have 17 clay.
# 2 obsidian-collecting robots collect 2 obsidian; you now have 3 obsidian.
# The new geode-cracking robot is ready; you now have 1 of them.

# == Minute 19 ==
# 1 ore-collecting robot collects 1 ore; you now have 3 ore.
# 4 clay-collecting robots collect 4 clay; you now have 21 clay.
# 2 obsidian-collecting robots collect 2 obsidian; you now have 5 obsidian.
# 1 geode-cracking robot cracks 1 geode; you now have 1 open geode.

# == Minute 20 ==
# 1 ore-collecting robot collects 1 ore; you now have 4 ore.
# 4 clay-collecting robots collect 4 clay; you now have 25 clay.
# 2 obsidian-collecting robots collect 2 obsidian; you now have 7 obsidian.
# 1 geode-cracking robot cracks 1 geode; you now have 2 open geodes.

# == Minute 21 ==
# Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
# 1 ore-collecting robot collects 1 ore; you now have 3 ore.
# 4 clay-collecting robots collect 4 clay; you now have 29 clay.
# 2 obsidian-collecting robots collect 2 obsidian; you now have 2 obsidian.
# 1 geode-cracking robot cracks 1 geode; you now have 3 open geodes.
# The new geode-cracking robot is ready; you now have 2 of them.

# == Minute 22 ==
# 1 ore-collecting robot collects 1 ore; you now have 4 ore.
# 4 clay-collecting robots collect 4 clay; you now have 33 clay.
# 2 obsidian-collecting robots collect 2 obsidian; you now have 4 obsidian.
# 2 geode-cracking robots crack 2 geodes; you now have 5 open geodes.

# == Minute 23 ==
# 1 ore-collecting robot collects 1 ore; you now have 5 ore.
# 4 clay-collecting robots collect 4 clay; you now have 37 clay.
# 2 obsidian-collecting robots collect 2 obsidian; you now have 6 obsidian.
# 2 geode-cracking robots crack 2 geodes; you now have 7 open geodes.

# == Minute 24 ==
# 1 ore-collecting robot collects 1 ore; you now have 6 ore.
# 4 clay-collecting robots collect 4 clay; you now have 41 clay.
# 2 obsidian-collecting robots collect 2 obsidian; you now have 8 obsidian.
# 2 geode-cracking robots crack 2 geodes; you now have 9 open geodes.
# However, by using blueprint 2 in the example above, you could do even better: the largest number of geodes you could open in 24 minutes is 12.

# Determine the quality level of each blueprint by multiplying that blueprint's ID number with the largest number of geodes that can be opened in 24 minutes using that blueprint. In this example, the first blueprint has ID 1 and can open 9 geodes, so its quality level is 9. The second blueprint has ID 2 and can open 12 geodes, so its quality level is 24. Finally, if you add up the quality levels of all of the blueprints in the list, you get 33.

# Determine the quality level of each blueprint using the largest number of geodes it could produce in 24 minutes. What do you get if you add up the quality level of all of the blueprints in your list?

# To begin, get your puzzle input.

# Dev notes:
# Interesting one, we should be trying to maximise for delivery of geode cracking machines, but to get those we always need at least one of the other sorts of machines
# I wonder if we should build a second X machine if there will be enough time to recuperate whatever is required to build the next X+1 machine after we use these resources - that would suggest that we can
# (and potentially should) build as many of the things as we can. Obviously if there are no X machines at the moment then we should build one.
# might be that actually for each machine we need to consider ALL the machines >x to make sure that we only build the ones we should.
# a little concerned that this will mean we may miss a trick about doubling up production speed / ratios for production but that's something we shall look at when we're going..
# certainly this is my starter for 10 plan.

# can't help but thinking that there's a reverse way to calculate this as I can only imagine that part 2 will be something like 'cool - now find out which is best over 24 million minutes..'
# again, problems for future Bryan

# on reflection, going to implement the simple multi-path walk and see where that gets us for part 1
# Oh, and Charlie loves : https://www.youtube.com/watch?v=dtfXakTi9II

import re


class RobotFactory:
    def __init__(self, description: str = None) -> None:
        if description is not None:
            numbers = re.findall(r"\d+", description)
            ints = [int(x) for x in numbers]
            assert 7 == len(ints)
            print(f" {description} -> {ints}")
            self.blueprint_id = ints[0]
            self.ore_robot_ore_cost = ints[1]
            self.clay_robot_ore_cost = ints[2]
            self.obsidian_robot_ore_cost = ints[3]
            self.obsidian_robot_clay_cost = ints[4]
            self.geode_robot_ore_cost = ints[5]
            self.geode_robot_obsidian_cost = ints[6]
        else:
            self.blueprint_id = None
            self.ore_robot_ore_cost = None
            self.clay_robot_ore_cost = None
            self.obsidian_robot_ore_cost = None
            self.obsidian_robot_clay_cost = None
            self.geode_robot_ore_cost = None
            self.geode_robot_obsidian_cost = None
        self.reset()

    def get_quality_level(self):
        result = None
        if self.blueprint_id is not None and self.best_geode_count is not None:
            result = self.blueprint_id * self.best_geode_count
        return result

    def reset(self):
        self.obsidian_robots = 0
        self.obsidian = 0
        self.geode_robots = 0
        self.geodes = 0
        self.clay_robots = 0
        self.clay = 0
        self.ore_robots = 1
        self.ore = 0
        self.minute = 0
        self.building_ore_robot = False
        self.building_clay_robot = False
        self.building_obsidian_robot = False
        self.building_geode_robot = False
        self.best_geode_count = None

    def copy(self):
        a = RobotFactory()
        a.blueprint_id = self.blueprint_id
        a.ore_robot_ore_cost = self.ore_robot_ore_cost
        a.clay_robot_ore_cost = self.clay_robot_ore_cost
        a.obsidian_robot_ore_cost = self.obsidian_robot_ore_cost
        a.obsidian_robot_clay_cost = self.obsidian_robot_clay_cost
        a.geode_robot_ore_cost = self.geode_robot_ore_cost
        a.geode_robot_obsidian_cost = self.geode_robot_obsidian_cost
        a.obsidian_robots = self.obsidian_robots
        a.obsidian = self.obsidian
        a.geode_robots = self.geode_robots
        a.geodes = self.geodes
        a.clay_robots = self.clay_robots
        a.clay = self.clay
        a.ore_robots = self.ore_robots
        a.ore = self.ore
        a.minute = self.minute
        a.building_ore_robot = self.building_ore_robot
        a.building_clay_robot = self.building_clay_robot
        a.building_obsidian_robot = self.building_obsidian_robot
        a.building_geode_robot = self.building_geode_robot

        return a

    def can_build_ore_robot(self):
        # can we afford it ?
        result = self.ore >= self.ore_robot_ore_cost
        # if we can, should we do this ?
        if result:
            # no sense in building more ore robots if we can already satisgy any robot build in a single iteration
            result = self.ore_robots < max(
                [
                    # self.ore_robot_ore_cost,  # this makes no sense, if the only thing we can't build is more ore robots then we don't need to..
                    self.clay_robot_ore_cost,
                    self.obsidian_robot_ore_cost,
                    self.geode_robot_ore_cost,
                ]
            )
        return result

    def can_build_clay_robot(self):
        result = self.ore >= self.clay_robot_ore_cost
        # if we can, should we ?
        if result:
            result = self.clay_robots < self.obsidian_robot_clay_cost
        return result

    def can_build_obsidian_robot(self):
        result = (
            self.ore >= self.obsidian_robot_ore_cost
            and self.clay >= self.obsidian_robot_clay_cost
        )
        if result:
            result = self.obsidian_robots < self.geode_robot_obsidian_cost
        return result

    def can_build_geode_robot(self):
        return (
            self.ore >= self.geode_robot_ore_cost
            and self.obsidian >= self.geode_robot_obsidian_cost
        )

    def can_build_anything(self):
        return (
            self.can_build_ore_robot()
            or self.can_build_clay_robot()
            or self.can_build_obsidian_robot()
            or self.can_build_geode_robot()
        )

    def build_option_count(self):
        # how many different types of thing can we build ?
        result = sum(
            [
                self.can_build_ore_robot(),
                self.can_build_clay_robot(),
                self.can_build_obsidian_robot(),
                self.can_build_geode_robot(),
            ]
        )
        return result

    def build_geode_robot(self):
        assert self.can_build_geode_robot()
        self.ore -= self.geode_robot_ore_cost
        self.obsidian -= self.geode_robot_obsidian_cost
        self.building_geode_robot = True

    def build_obsidian_robot(self):
        assert self.can_build_obsidian_robot()
        self.ore -= self.obsidian_robot_ore_cost
        self.clay -= self.obsidian_robot_clay_cost
        self.building_obsidian_robot = True

    def build_clay_robot(self):
        assert self.can_build_clay_robot()
        self.ore -= self.clay_robot_ore_cost
        self.building_clay_robot = True

    def build_ore_robot(self):
        assert self.can_build_ore_robot()
        self.ore -= self.ore_robot_ore_cost
        self.building_ore_robot = True

    def unable_to_build(self):
        # makes my loop nicer
        return not self.can_build_anything()

    def step(self):
        # execute one step of the logic.. we will already have decided whether to build a robot or not..
        # so.. part 1, all the robots mine one item each
        self.ore += self.ore_robots
        self.clay += self.clay_robots
        self.obsidian += self.obsidian_robots
        self.geodes += self.geode_robots

        # and we complete any robot builds..
        if self.building_clay_robot:
            self.clay_robots += 1
            self.building_clay_robot = False
        if self.building_ore_robot:
            self.ore_robots += 1
            self.building_ore_robot = False
        if self.building_obsidian_robot:
            self.obsidian_robots += 1
            self.building_obsidian_robot = False
        if self.building_geode_robot:
            self.geode_robots += 1
            self.building_geode_robot = False

        # and the next minute has happened..
        self.minute += 1

    def unstep(self):
        # reverse one mining operation - it doesn't handle unbuilding robots, nor will it need to
        self.ore -= self.ore_robots
        self.clay -= self.clay_robots
        self.obsidian -= self.obsidian_robots
        self.geodes -= self.geode_robots

        # and the next minute has happened..
        self.minute -= 1

    def solve(self, target_minutes=24):

        best_geode_count = 0
        best_geode_version = None

        # we can start with an initial value
        evaluation_options = [self.copy()]

        # while we have one to evaluate..
        while len(evaluation_options) > 0:
            # pop this option and walk it to a conclusion..
            this_option = evaluation_options.pop()

            # we always want to move forwards at least once.
            this_option.step()

            # wind forwards until we can do something..
            while this_option.unable_to_build() and this_option.minute < target_minutes:
                this_option.step()

            # are we done ?
            if this_option.minute >= target_minutes:
                if this_option.geodes > 0:
                    # print(f"Complete {len(evaluation_options)} -> {this_option}")
                    pass
                if this_option.geodes > best_geode_count:
                    best_geode_count = this_option.geodes
                    best_geode_version = this_option
                    print(f"New best geode count is {best_geode_count} - {this_option}")
            else:
                # we now have some decisions to make.. we can build something..
                if this_option.can_build_geode_robot():
                    new_path = this_option.copy()
                    new_path.build_geode_robot()
                    evaluation_options.append(new_path)
                    # print(f"Chose to build a geode robot -> {this_option}")
                if this_option.can_build_obsidian_robot():
                    new_path = this_option.copy()
                    new_path.build_obsidian_robot()
                    evaluation_options.append(new_path)
                    # print(f"Chose to build an obsidian robot -> {this_option}")
                if this_option.can_build_clay_robot():
                    new_path = this_option.copy()
                    new_path.build_clay_robot()
                    evaluation_options.append(new_path)
                if this_option.can_build_ore_robot():
                    new_path = this_option.copy()
                    new_path.build_ore_robot()
                    evaluation_options.append(new_path)
                # and we can always just not build anything..
                # but if we do this, it doesn't make sense to continue with the same options next time - we need to march on until the next step would give us new options..
                current_option_count = this_option.build_option_count()
                if 4 != current_option_count:
                    while (
                        this_option.build_option_count() == current_option_count
                        and this_option.minute < target_minutes
                    ):
                        # print(f"fast winding -> {this_option}")
                        this_option.step()
                    if this_option.minute < target_minutes:
                        this_option.unstep()
                        evaluation_options.append(this_option)

        # and we have a winner ?
        print(
            f"Most possible geodes for RobotFactory {self.blueprint_id} is {best_geode_count} - {best_geode_version}"
        )
        self.best_geode_count = best_geode_count
        return best_geode_count

    def __repr__(self) -> str:
        s = f"<RobotFactory {self.blueprint_id} min={self.minute} best={self.best_geode_count} quality={self.get_quality_level()}"
        s += f" costs(ore={self.ore_robot_ore_cost}, clay={self.clay_robot_ore_cost}, obsidian={self.obsidian_robot_ore_cost},{self.obsidian_robot_clay_cost}, geode={self.geode_robot_ore_cost},{self.geode_robot_obsidian_cost})"
        s += f" robots(ore={self.ore_robots}, clay={self.clay_robots}, obsidian={self.obsidian_robots}, geode={self.geode_robots}) "
        s += f" resources(ore={self.ore}, clay={self.clay}, obsidian={self.obsidian}, geodes={self.geodes} "
        s += f">"
        return s


def load_robot_factories(filename: str):
    factories = []
    with open(filename, "r") as f:
        for this_line in f:
            this_line = this_line.strip()
            if "" != this_line:
                this_factory = RobotFactory(this_line)
                factories.append(this_factory)

    return factories


def part1(filename: str):
    # load the various robot factories from the file..
    factories = load_robot_factories(filename)
    for this_factory in factories:
        print(this_factory)
        the_answer = this_factory.solve()

    # and now add up the quality levels..
    quality_scores = [x.get_quality_level() for x in factories]
    total_quality = sum(quality_scores)

    result = total_quality
    print(f"The total quality for {filename} is {result}")
    return result


if __name__ == "__main__":
    puzzle_filename = "input.txt"
    sample_filename = "sample.txt"
    sample_expected_result = 33

    sample_actual_result = part1(sample_filename)
    assert sample_expected_result == sample_actual_result

    puzzle_result = part1(puzzle_filename)
