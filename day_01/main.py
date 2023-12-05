#!/bin/python

import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

f = open("input.txt", "r")
lines = f.read().splitlines()
f.close()

result = 0;

for line in lines:
    line = line.replace("one", "o1ne")
    line = line.replace("two", "t2wo")
    line = line.replace("three", "t3hree")
    line = line.replace("four", "f4our")
    line = line.replace("five", "f5ive")
    line = line.replace("six", "s6ix")
    line = line.replace("seven", "s7even")
    line = line.replace("eight", "e8ight")
    line = line.replace("nine", "n9ine")

    line     = [x for x in line if x.isdigit()]
    result += int(line[0] + line[-1])

print(f"result: {result}");

