#!/usr/bin/py

with open('File1', 'r') as file1:
    with open('index.html', 'r') as file2:
        same = set(file1).symmetric_difference(file2)

with open('output_file.txt', 'w') as file_out:
    for line in same:
        file_out.write(line)

