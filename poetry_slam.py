# Bismillah al-Rahmaan al-Raheem
# Ali Shah | Sept. 29, 2020
# CS1.0 Assignment 3: Poetry Slam

"""This program reads poem lines from a file and manipulates them in various ways"""

from random import randint


def get_file_lines(filename):
    """Reads poem file, removes newline char, and returns lines in a list"""

    with open(filename, "r") as lines:
        lines = lines.readlines()  # Saves list of each poem line in lines

    for _ in range(len(lines)):
        lines[_] = lines[_].rstrip()  # Removes newline char from right-side end of each poem line

    return lines

def lines_printed_backwards(lines_list):
    """Adds numbers to poem's lines and reverses line order; prints result"""

    numbered_poem = []
    for _, line in enumerate(lines_list):
        numbered_poem.append(f"{_ + 1} {line}")  # Adds line number to each string

    numbered_poem.reverse()  # Reassigns all numbered_poem elements in reverse order

    for _ in numbered_poem:
        print(_)

    # Alternate solution without reassignment to numbered_poem:
    # for _ in range(len(numbered_poem)):
    #     print(numbered_poem[::-1][_])  # [::-1] -> negative step, start at last index

def lines_printed_random(lines_list):
    """Prints random lines from poem until reaching original line count number of prints"""

    for _ in range(len(lines_list)):
        i = len(lines_list) - 1
        print(
            lines_list[randint(0, i)]
        )

def equivalence_cycles(lines_list):  # lines_printed_custom() section of assignment
    """Fills list with random lines from poem, loops until the same line occupies
    every index in the list, and then prints result backwards. If loop cycles max_cycle
    times, loop stops and prints final generation of lines backwards. To maximize
    likelihood for most number of cycles, each line in poem should be unique"""

    new_list = []
    counter = 0
    i = len(lines_list) - 1
    max_cycles = 99999  # Used to limit attempts; recommended if len(list) > 5

    while True:
        new_list.clear()
        counter += 1
        for _ in range(len(lines_list)):
            new_list.append(
                lines_list[randint(0, i)]
            )

        #print(new_list)  # Uncomment to print each list variation per cycle
        #input()          # Uncomment for keyboard prompt to step cycle-by-cycle

        if new_list[1:] == new_list[:-1]:
            break
        elif counter > max_cycles - 1:  # Limits loop to max_cycles attempts
            break

    print(f"Cycles: {counter}")

    for line in new_list:
        print(line[::-1])

poem_lines = get_file_lines("tanka.txt")

lines_printed_backwards(poem_lines)
print()  # Spacer
lines_printed_random(poem_lines)
print()  # Spacer
equivalence_cycles(poem_lines)
print()  # Spacer
