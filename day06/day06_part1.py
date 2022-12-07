# --- Day 6: Tuning Trouble ---
# The preparations are finally complete; you and the Elves leave camp on foot and begin to make your way toward the star fruit grove.

# As you move through the dense undergrowth, one of the Elves gives you a handheld device. He says that it has many fancy features, but 
# the most important one to set up right now is the communication system.

# However, because he's heard you have significant experience dealing with signal-based systems, he convinced the other Elves that it 
# would be okay to give you their one malfunctioning device - surely you'll have no problem fixing it.

# As if inspired by comedic timing, the device emits a few colorful sparks.

# To be able to communicate with the Elves, the device needs to lock on to their signal. The signal is a series of seemingly-random 
# characters that the device receives one at a time.

# To fix the communication system, you need to add a subroutine to the device that detects a start-of-packet marker in the datastream. 
# In the protocol being used by the Elves, the start of a packet is indicated by a sequence of four characters that are all different.

# The device will send your subroutine a datastream buffer (your puzzle input); your subroutine needs to identify the first position 
# where the four most recently received characters were all different. Specifically, it needs to report the number of characters from 
# the beginning of the buffer to the end of the first such four-character marker.

# For example, suppose you receive the following datastream buffer:

# mjqjpqmgbljsphdztnvjfqwrcgsmlb
# After the first three characters (mjq) have been received, there haven't been enough characters received yet to find the marker. 
# The first time a marker could occur is after the fourth character is received, making the most recent four characters mjqj. 
# Because j is repeated, this isn't a marker.

# The first time a marker appears is after the seventh character arrives. Once it does, the last four characters received are jpqm, 
# which are all different. In this case, your subroutine should report the value 7, because the first start-of-packet marker is 
# complete after 7 characters have been processed.

# Here are a few more examples:

# bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 5
# nppdvjthqldpwncqszvftbrmjlhg: first marker after character 6
# nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 10
# zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 11

# How many characters need to be processed before the first start-of-packet marker is detected?


def load_file_to_string(filename: str):
    result = ''
    with open(filename, 'r') as f:
        for this_line in f:
            this_line = this_line.strip()
            result += this_line
    return result 

def part1(signal: str):
    # identify the first character where there are no repeats in the previous 4 characters 
    # input is small so naive version is probably fine
    signal_idx = 3  # first possible location
    while(signal_idx < len(signal)):
        # is this the one ?
        signal_chunk = signal[signal_idx - 3: signal_idx + 1]
        signal_set = set(signal_chunk)
        if len(signal_set) == 4:
            # this is the one, off we go
            result = signal_idx + 1
            break
        # next
        signal_idx += 1
    # and we're done
    print(f'Found a non-repeating sequence after {result} characters') 
    return result 



if __name__ == "__main__":
    puzzle_input = load_file_to_string('input.txt')
    sample_inputs = [
        ('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 7),
        ('bvwbjplbgvbhsrlpgdmjqwftvncz', 5),
        ('nppdvjthqldpwncqszvftbrmjlhg', 6),
        ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 10),
        ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 11),
    ]

    for this_sample, this_expected in sample_inputs:
        this_result = part1(this_sample)
        assert this_expected == this_result

    this_actual = part1(puzzle_input)


