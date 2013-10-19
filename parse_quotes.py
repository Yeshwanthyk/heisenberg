# -*- coding: utf-8 -*-

# The list of all the lines in the files
alist = []

# The dict of all the quotes as seperated by
# the delimiter
output = {}



def parse_quotes():
    """ This helps parse all the quotes from the txt file given based
        on a delimiter (in this case "EOL")
    """
    # Temp list to hold and process the lines from
    # alist
    quote = []

    # The counter for setting the key of the
    # dict
    count = 0

    f = open("BreakingBadQuotes.txt")

    for line in f.readlines():
        alist.append(line.strip())

    for i in alist:
        quote.append(i)
        if i == "EOL":
            quote.pop()
            output[count] = quote
            count += 1
            quote = []
            pass

    return output

if __name__ == '__main__':

    answer = parse_quotes()
    print answer

