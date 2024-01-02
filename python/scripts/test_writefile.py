#!/usr/bin/env python

mylines = ["line1\n", "line2\n"]

with open("myfile", "w") as fd:
    fd.writelines(mylines)

ensure_line = "line3\n"
with open("myfile", "r") as fd:
    current_lines = fd.readlines()

with open("myfile", "w") as wd:
    if ensure_line not in current_lines:
        current_lines.append(ensure_line)
        wd.writelines(current_lines)
