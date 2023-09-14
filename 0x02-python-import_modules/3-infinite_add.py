#!/usr/bin/python3

import sys
def main():
    result = 0
    for x in sys.argv:
        if x == sys.argv[0]:
            continue
        result += int(x)

    print(result)

if __name__ == '__main__':
    main()
