# Introduction

This tool allows you to log open files for a process over time. 
This might be ideal to debug 'too many open files' problems.

# Requirements
1. Bash
2. lsof
3. Python 3

# Usage

    ./log.sh 123 0.5

The log.sh script will log open files for the pid (123) for each amount of seconds (0.5).
This will produce logs in the logs directory. 
Each timer tick will produce a log file with the names of the open files. 

    log_to_csv.py

The log_to_csv.py script will search the logs directory and for each opened file in lsof produce a row in a csv file. 
Important: It will only produce a line if the amount of occurrences of said file changes.
The result is a results.csv file with the lsof log result file in each column, and the opened file as a row.

Example:

| . | logs/0.log | logs/1.log | logs/2.log | logs/3.log |
| - | ---------- | ---------- | ---------- | ---------- |
| file | 2 | 2 | 0 | 0 |
|/memfd:mozilla-ipc|157|157|157|151|

 
