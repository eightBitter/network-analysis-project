# python 3.7.0. This script pulls out specified fields from ProQuest's text file
# and transforms the data to a csv

# import libraries
import re
import csv
import itertools

# set up list of records
records = []

# set search patterns to find keywords and titles
keyword_pattern = re.compile("Keywords - ")
title_pattern = re.compile("Title: ")

# open input file

with open ('input.txt', 'rt') as in_file:
    # go through input file, find matching patterns, and append the matches to appropriate lists
    lines = []
    for line in in_file:
        lines.append(line)

# groups lines into sublists based on the long underscore
lineGroups = [list(v) for k,v in itertools.groupby(lines,key=lambda x: x.startswith("____________________________________________________________")) if not k]

# iterate over sublists
for group in lineGroups:
    # reset "combined" dictionary
    combined = None
    combined = {"title": [],"keywords": []}
    # iterate over each line in a sublist
    for line in group:
        # search for title pattern
        if title_pattern.search(line) != None:
            # append matching line to dictionary
            combined["title"].append(line.rstrip('\n'))
        # search for keyword pattern
        if keyword_pattern.search(line) != None:
            # append matching line to dictionary
            combined["keywords"].append(line.rstrip('\n'))
    # append "combined" dictionary to "records" list
    records.append(combined)

# open output file
with open("output.csv", "w") as output:
    # set up headers
    wcsv = csv.DictWriter(output, fieldnames=["title","keywords"])
    wcsv.writeheader()
    # insert new rows from the data
    for record in records:
        wcsv.writerow(record)
print("done")
