#! /usr/local/bin/python3
import sys

out_of = int(sys.argv[1])
# This is a while loop
# Great comment

while 1:
    line = input()
    total = 0
    for num in line.split(" "):
        total += int(num)
    print("Total: %d (%f%%)" % (total, total * (100.0 / out_of)))

