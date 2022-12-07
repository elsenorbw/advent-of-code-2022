# --- Day 7: No Space Left On Device ---
# You can hear birds chirping and raindrops hitting leaves as the expedition proceeds. Occasionally, you can even hear much louder sounds in the distance; how big do the animals get out here, anyway?

# The device the Elves gave you has problems with more than just its communication system. You try to run a system update:

# $ system-update --please --pretty-please-with-sugar-on-top
# Error: No space left on device
# Perhaps you can delete some files to make space for the update?

# You browse around the filesystem to assess the situation and save the resulting terminal output (your puzzle input). For example:

# $ cd /
# $ ls
# dir a
# 14848514 b.txt
# 8504156 c.dat
# dir d
# $ cd a
# $ ls
# dir e
# 29116 f
# 2557 g
# 62596 h.lst
# $ cd e
# $ ls
# 584 i
# $ cd ..
# $ cd ..
# $ cd d
# $ ls
# 4060174 j
# 8033020 d.log
# 5626152 d.ext
# 7214296 k
# The filesystem consists of a tree of files (plain data) and directories (which can contain other directories or files). The outermost directory is called /.
# You can navigate around the filesystem, moving into or out of directories and listing the contents of the directory you're currently in.

# Within the terminal output, lines that begin with $ are commands you executed, very much like some modern computers:

# cd means change directory. This changes which directory is the current directory, but the specific result depends on the argument:
# cd x moves in one level: it looks in the current directory for the directory named x and makes it the current directory.
# cd .. moves out one level: it finds the directory that contains the current directory, then makes that directory the current directory.
# cd / switches the current directory to the outermost directory, /.
# ls means list. It prints out all of the files and directories immediately contained by the current directory:
# 123 abc means that the current directory contains a file named abc with size 123.
# dir xyz means that the current directory contains a directory named xyz.
# Given the commands and output in the example above, you can determine that the filesystem looks visually like this:

# - / (dir)
#   - a (dir)
#     - e (dir)
#       - i (file, size=584)
#     - f (file, size=29116)
#     - g (file, size=2557)
#     - h.lst (file, size=62596)
#   - b.txt (file, size=14848514)
#   - c.dat (file, size=8504156)
#   - d (dir)
#     - j (file, size=4060174)
#     - d.log (file, size=8033020)
#     - d.ext (file, size=5626152)
#     - k (file, size=7214296)
# Here, there are four directories: / (the outermost directory), a and d (which are in /), and e (which is in a). These directories also contain files of various sizes.

# Since the disk is full, your first step should probably be to find directories that are good candidates for deletion. To do this, you need to determine the total size of each directory.
# The total size of a directory is the sum of the sizes of the files it contains, directly or indirectly. (Directories themselves do not count as having any intrinsic size.)

# The total sizes of the directories above can be found as follows:

# The total size of directory e is 584 because it contains a single file i of size 584 and no other directories.
# The directory a has total size 94853 because it contains files f (size 29116), g (size 2557), and h.lst (size 62596), plus file i indirectly (a contains e which contains i).
# Directory d has total size 24933642.
# As the outermost directory, / contains every file. Its total size is 48381165, the sum of the size of every file.
# To begin, find all of the directories with a total size of at most 100000, then calculate the sum of their total sizes.
# In the example above, these directories are a and e; the sum of their total sizes is 95437 (94853 + 584). (As in this example, this process can count files more than once!)

# Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those directories?

# To begin, get your puzzle input.

# Your puzzle answer was 1367870.

# The first half of this puzzle is complete! It provides one gold star: *

# --- Part Two ---
# Now, you're ready to choose a directory to delete.

# The total disk space available to the filesystem is 70000000. To run the update, you need unused space of at least 30000000.
# You need to find a directory you can delete that will free up enough space to run the update.

# In the example above, the total size of the outermost directory (and thus the total amount of used space) is 48381165;
# this means that the size of the unused space must currently be 21618835, which isn't quite the 30000000 required by the update.
# Therefore, the update still requires a directory with total size of at least 8381165 to be deleted before it can run.

# To achieve this, you have the following options:

# Delete directory e, which would increase unused space by 584.
# Delete directory a, which would increase unused space by 94853.
# Delete directory d, which would increase unused space by 24933642.
# Delete directory /, which would increase unused space by 48381165.
# Directories e and a are both too small; deleting them would not free up enough space. However, directories d and / are both big enough! Between these, choose the smallest: d, increasing unused space by 24933642.

# Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update. What is the total size of that directory?


# - so the plan is to load everything into a directory structure and then answer the questions from there..


class DirectoryNode:
    def __init__(self, node_name: str, parent_node=None) -> None:
        self.name = node_name
        self.files = {}
        self.subdirs = {}
        self.parent_node = parent_node

    def __repr__(self):
        return f"<<DirectoryNode name={self.name} ({len(self.files)} files, {len(self.subdirs)} subdirs, {self.total_size()} total bytes)>>"

    def add_file(self, filename: str, filesize: int):
        self.files[filename] = filesize

    def add_directory(self, directory_name):
        # if we are adding a directory that already exists then we can just skip this
        if directory_name not in self.subdirs:
            self.subdirs[directory_name] = DirectoryNode(directory_name, self)

    def get_relative_directory(self, directory_name):
        if ".." == directory_name:
            result = self.parent_node
        else:
            result = self.subdirs[directory_name]
        return result

    def total_size(self):
        result = sum(self.files.values())
        for this_subdir in self.subdirs.values():
            result += this_subdir.total_size()
        return result

    def all_directories(self):
        # return a list of all the directories
        result = []
        nodelist = [self]
        nodelist_idx = 0

        # keep looping..
        while nodelist_idx < len(nodelist):
            # add any new directories to the list to be considered
            this_node = nodelist[nodelist_idx]
            for this_subdir in this_node.subdirs.values():
                nodelist.append(this_subdir)

            # and add this one to the result
            result.append(this_node)

            # next
            nodelist_idx += 1

        return result

    def print(self, indent=0):
        spacing = "  " * indent
        print(f"{spacing}- {self.name} (total size={self.total_size()})")
        for subdir in self.subdirs.values():
            subdir.print(indent + 1)
        for thisfile in self.files:
            print(f"{spacing} +{thisfile} ({self.files[thisfile]})")


def load_filesystem(filename: str):
    # create the filesystem structure in memory
    with open(filename, "r") as f:
        for this_line in f:
            this_line = this_line.strip()
            # ignoring blanks
            if "" != this_line:
                # one true start..
                if "$ cd /" == this_line:
                    # initialise the setup
                    result = DirectoryNode("/")
                    current_node = result

                # It's either a command
                elif "$" == this_line[0]:
                    if this_line.startswith("$ cd "):
                        target_dir = this_line[5:]
                        current_node = current_node.get_relative_directory(target_dir)

                # or it is a directory entry
                elif this_line.startswith("dir"):
                    parts = this_line.split(" ")
                    assert 2 == len(parts)
                    directory_name = parts[1]
                    current_node.add_directory(directory_name)
                # or it is a file entry we presume..
                else:
                    parts = this_line.split(" ")
                    assert 2 == len(parts)
                    filesize = int(parts[0])
                    filename = parts[1]
                    current_node.add_file(filename, filesize)
    return result


def part2(filename: str):
    fs = load_filesystem(filename)
    fs.print()

    total_system_disksize = 70000000
    space_required_for_update = 30000000

    # how much free space is there currently ?
    current_free_space = total_system_disksize - fs.total_size()
    # and therefore how much do we need to free up ?
    need_to_free = space_required_for_update - current_free_space

    print(
        f"We have a system size of {total_system_disksize}, we need {space_required_for_update} for the update, currently the filesystem contains {fs.total_size()} leaving {current_free_space} free, so we need to free {need_to_free} more"
    )

    # get all the directories
    all_dirs = fs.all_directories()

    # get all their sizes
    dir_sizes = [x.total_size() for x in all_dirs]
    deletion_candidates = [x for x in dir_sizes if x >= need_to_free]
    result = min(deletion_candidates)

    print(f"result for {filename} is {result}")

    return result


if __name__ == "__main__":
    sample_filename = "sample.txt"
    filename = "input.txt"
    expected_sample_result = 24933642

    sample_actual = part2(sample_filename)
    assert sample_actual == expected_sample_result

    result = part2(filename)
