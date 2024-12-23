"""
Day 2: Red-Nosed Reports
"""

import numpy as np


def part1(filename):
    safe_reports = 0
    with open(filename) as file:
        for line in file:
            extracted_line = line.rstrip().split()
            numerical_list = np.zeros(len(extracted_line))
            for i in range(len(extracted_line)):
                numerical_list[i] = extracted_line[i]
            diffs = np.diff(numerical_list)
            if np.all(diffs > 0):
                if np.all(diffs <= 3):
                    safe_reports += 1
            elif np.all(diffs < 0):
                if np.all(diffs >= -3):
                    safe_reports += 1
    return safe_reports


def part2(filename):
    safe_reports = 0
    with open(filename) as file:
        for line in file:
            extracted_line = line.rstrip().split()
            numerical_list = np.zeros(len(extracted_line))
            for i in range(len(extracted_line)):
                numerical_list[i] = extracted_line[i]
            diffs = np.diff(numerical_list)
            positive_diffs = 0
            negative_diffs = 0
            for diff in diffs:
                if diff > 0:
                    positive_diffs += 1
                else:
                    negative_diffs += 1
            if (positive_diffs > 0 and negative_diffs <= 1):
                diff_greater_than_3 = 0
                for diff in diffs:
                    if diff >= 3:
                        diff_greater_than_3 += 1
                if (diff_greater_than_3 <= 1):
                    safe_reports += 1
            if (negative_diffs > 0 and positive_diffs <= 1):
                diff_less_than_minus3 = 0
                for diff in diffs:
                    if diff <= -3:
                        diff_less_than_minus3 += 1
                if (diff_less_than_minus3 <= 1):
                    safe_reports += 1
    return safe_reports


if __name__ == "__main__":
    print(part1("day2/input.txt"))
