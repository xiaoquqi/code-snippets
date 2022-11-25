#!/usr/bin/env python3

import filecmp
import os

current_path = os.path.dirname(os.path.abspath(__file__))

# Directory compare sample
left_path = os.path.join(current_path, "dir1")
right_path = os.path.join(current_path, "dir2")

compared = filecmp.dircmp(left_path, right_path)

print("Only in left: %s" % compared.left_only)
print("Only in right: %s" % compared.right_only)
print("Common files: %s" % compared.common_files)
print("Diff files: %s" % compared.diff_files)


# File compare sample
left_path_file = os.path.join(left_path, "common_file")
right_path_file = os.path.join(right_path, "common_file")

file_compred = filecmp.cmp(left_path_file, right_path_file)
print("File common files: %s" % file_compred)
