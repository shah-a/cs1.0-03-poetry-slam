def get_file_lines(filename):

    with open(filename, "r") as poem_lines:
        poem_lines = poem_lines.readlines() #saves list of each poem lines in file_lines

    for _ in range(len(poem_lines)):
        poem_lines[_] = poem_lines[_].rstrip() #removes newline char from right-side end of each poem line

    return poem_lines

def lines_printed_backwards(lines_list):

    for _ in range(len(lines_list)):
        lines_list[_] = f"{_ + 1} {lines_list[_]}"

    lines_list.reverse()

    for _ in lines_list:
        print(_)

    #  for _ in range(len(lines_list)):
    #     print(lines_list[::-1][_])
    # #Alternate solution to print the list in reverse order
    # #Previous solution uses list reverse() method, which reassigns to the variable
    # #This solution uses slicing with a negative step; it does not reassign any values to the list
    # #Though this one is super neat :), I chose the previous solution in favour of code readability

    return None

lines_list = get_file_lines("tanka.txt")
lines_printed_backwards(lines_list)