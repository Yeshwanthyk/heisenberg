# -*- coding: utf-8 -*-

from random import randint

def parse_quotes():
    """ This helps parse all the quotes from the txt file given based
        on a delimiter (in this case "EOL")
    """
    # The list of all the lines in the files
    alist = []

    # The dict of all the quotes as seperated by
    # the delimiter
    output = {}

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
        quote.append(i.decode("utf-8"))
        if i == "EOL":
            quote.pop()
            output[count] = quote
            count += 1
            quote = []
            pass

    f.close()

    return output[randint(0,len(output))]
