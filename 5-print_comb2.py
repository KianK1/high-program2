#!/usr/bin/python3
range1 = range(100)
comma_range1 = comma_range1 = ", ".join("{:02d}".format(num) for num in range1)
print(f"{comma_range1}")
