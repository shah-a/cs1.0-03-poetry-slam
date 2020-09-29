#Ali Shah, github.com/shah-a
#September 29th, 2020

from random import randint

def get_file_lines(filename):

    with open(filename, "r") as poem_lines:
        poem_lines = poem_lines.readlines() #saves list of each poem lines in file_lines

    for _ in range(len(poem_lines)):
        poem_lines[_] = poem_lines[_].rstrip() #removes newline char from right-side end of each poem line

    return poem_lines

def lines_printed_backwards(lines_list):

    for _ in range(len(lines_list)):
        lines_list[_] = f"{_ + 1} {lines_list[_]}" #adds line number to beginning of each string in list

    lines_list.reverse()

    for _ in lines_list:
        print(_)

    #  for _ in range(len(lines_list)):
    #     print(lines_list[::-1][_])
    #
    # #Alternate solution to print the list in reverse order
    # #Previous solution uses list reverse() method, which reassigns to the variable
    # #This solution uses slicing with a negative step; it does not reassign any values to the list
    # #Though this one is super neat :), I chose the previous solution in favour of code readability

    return None

def lines_printed_random(lines_list):

    for _ in range(len(lines_list)):
        i = len(lines_list) - 1
        print(
            lines_list[randint(0, i)]
        )

    return None

def equivalence_cycles(lines_list): #This function is for the lines_printed_custom() section of the assignment; I preferred to name it differently than instructed

    #Soo... I got curious and wrote this function to count how many cycles it takes for every element to randomly be assigned the same value
    #It took 21530 cycles the first time I tried this with the poem from tanka.txt. I believe second and third attempts were around 64000 and 96000 cycles respectively
    #All three attempts, each element ended up being 'A faint clap of thunder,' which makes sense because the poem has that line twice (lines 1 and 5)
    #To maximize likelihood for most number of cycles, each list element should be unique

    new_list = []
    counter = 0
    while True:
        new_list.clear()
        counter += 1
        for _ in range(len(lines_list)):
            new_list.append(lines_list[randint(0, len(lines_list) - 1)])

        #print(new_list) #uncomment to print each list variation per cycle
        #input()         #uncomment to receive keyboard prompt to step through cycles; not recommended for lists with more than 3 unique elements

        if new_list[1:] == new_list[:-1]:
            break
        elif counter > 99999: #limits loop to 100,000 cycles; comment out to let program continue until all lines are equivalent
            break

    print(f"Cycles: {counter}")

    for line in new_list:
        print(line[::-1])

    return None

poem_lines = get_file_lines("tanka.txt")

#lines_printed_backwards(poem_lines)
#lines_printed_random(poem_lines)
equivalence_cycles(poem_lines)

#equivalence_cycles(["one", "two", "three"])