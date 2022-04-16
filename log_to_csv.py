#!/usr/bin/env python3
import os


import re

def tryint(s):
    try:
        return int(s)
    except:
        return s

def alphanum_key(s):
    """ Turn a string into a list of string and number chunks.
        "z23a" -> ["z", 23, "a"]
    """
    return [ tryint(c) for c in re.split('([0-9]+)', s) ]

def sort_nicely(l):
    """ Sort the given list in the way that humans expect.
    """
    l.sort(key=alphanum_key)

def find_log_files():
    log_files = []
    for file in os.listdir("logs"):
        if file.endswith(".log"):
            log_files.append(os.path.join("logs", file))

    sort_nicely(log_files)
    return log_files

def search_unique_filenames(log_files): 
    all_lines = set()
    for log_file in log_files:
        with open(log_file) as file:
            lines = file.readlines()
            for line in lines:
                all_lines.add(line.rstrip('\n'))
    return all_lines

def count_text_in_file(text, filename):
    file = open(filename, "r")
    data = file.read()
    occurrences = data.count(text)
    return occurrences

log_files = find_log_files()
unique_names = search_unique_filenames(log_files)

results_csv = open("results.csv", "w")

header = ","+','.join(log_files)+"\n"
results_csv.write(header)

for unique_name in unique_names:
    unique_name_vector = [unique_name]
    for logfile in log_files:
        unique_name_vector.append(str(count_text_in_file(unique_name, logfile)))
    results_csv.write(','.join(unique_name_vector)+"\n")

results_csv.close()