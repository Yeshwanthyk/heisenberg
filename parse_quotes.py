# -*- coding: utf-8 -*-

# The list of all the lines in the files
alist = []

# Temp list to hold and process the lines from
# alist
quote = []

# The dict of all the quotes as seperated by
# the delimiter
output = {}

# The counter for setting the key of the
# dict
count = 0


def parse_quotes():
    """ This helps parse all the quotes from the txt file given based
        on a delimiter (in this case "EOL")
    """
    f = open("BreakingBadQuotes.txt")

    for line in f.readlines():
        alist.append(line.strip())

    return alist[0]

if __name__ == '__main__':

    answer = parse_quotes()
    print answer



