import day1

example1_data = day1.read_data("day1_example1.txt")


def test_part1_example1():
    example1_ans = day1.part1(example1_data)
    assert example1_ans == 11


def test_part2_example2():
    example2_ans = day1.part2(example1_data)
    assert example2_ans == 31
