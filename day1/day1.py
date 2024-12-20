"""
Day 1: Historian hysteria
"""

import numpy as np

def read_data(filename):
    data = np.loadtxt(filename)
    return data

def part1(data):
    column1 = data[:,0]
    column2 = data[:,1]
    sorted1 = np.sort(column1)
    sorted2 = np.sort(column2)
    difference = np.abs(sorted2 - sorted1)
    total_difference = difference.sum()
    return total_difference


def part2(data):
    column1 = data[:,0]
    column2 = data[:,1]
    total_sum = 0
    for i in column1:
        count = 0
        for j in column2:
            if (i == j):
                count = count + 1
        similarity_score = count * i
        total_sum = total_sum + similarity_score
    return total_sum



if __name__ == "__main__":
    example1_data = read_data("day1_example1.txt")
    example1_ans = part1(example1_data)
    day1_data = read_data("day1.txt")
    day1_ans = part1(day1_data)
    day1_part2_ans = part2(day1_data)
    print(day1_ans)
    print(day1_part2_ans)