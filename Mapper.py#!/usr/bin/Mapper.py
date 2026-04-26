#!/usr/bin/python
import sys

next(sys.stdin)  # skip header

for line in sys.stdin:

    fields=line.strip().split(",")

    if len(fields)<5:
        continue

    depression=fields[4]

    print(depression+"\t1")
