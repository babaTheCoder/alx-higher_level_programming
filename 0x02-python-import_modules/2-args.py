#!/usr/bin/python3

import sys
i = 1

if len(sys.argv) == 1:
    print("0 arguments.")
elif len(sys.argv) == 2:
    print("1 argument:")
    print("1: {}".format(sys.argv[1]))
else:
    print("{} arguments:".format(len(sys.argv)-1))
    for x in sys.argv:
        if x == sys.argv[0]:
            continue
        print("{}: {}".format(i, x))
        i += 1 
