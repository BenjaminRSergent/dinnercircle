
# These test would belong in another file if this wasn't an online interpreter with one file.
# These are sloppy adhoc sanity checks for common cases rather than proper unit testing
import math

from dinnercircle.dinnergroups import DinnerGroups
from dinnercircle.util import to_ft_str


def test_dinner_groups():
    test_same_size_dinner_groups()
    test_mixed_size_dinner_groups()


def test_same_size_dinner_groups():
    print(" ----------------------------")
    print("| Testing single chair groups |")
    print(" ----------------------------")
    test_num = 1
    test_groups = DinnerGroups()

    test_chair_width = 2
    test_intragroup_dist = 1
    test_intergroup_dist = 6
    test_groups.add_group_size_with_cnt(1, 3)
    expected_circumference = 24

    circle = test_groups.calc_min_safe_circle(test_chair_width, test_intergroup_dist, test_intragroup_dist)
    if not expect_circle_by_circumference(circle,
                                          expected_circumference):
        print(f"Single chair test {test_num} failed")

    test_num = 2
    test_groups = DinnerGroups()
    test_chair_width = 2
    test_intragroup_dist = 1
    test_intergroup_dist = 6
    test_groups.add_group_size_with_cnt(1, 4)
    expected_circumference = 32

    circle = test_groups.calc_min_safe_circle(test_chair_width, test_intergroup_dist, test_intragroup_dist)
    if not expect_circle_by_circumference(circle,
                                          expected_circumference):
        print(f"Single chair test {test_num} failed")

    test_num = 3
    test_groups = DinnerGroups()
    test_chair_width = 0
    test_intragroup_dist = 0
    test_intergroup_dist = 6
    test_groups.add_group_size_with_cnt(1, 3)
    expected_circumference = 18

    circle = test_groups.calc_min_safe_circle(test_chair_width, test_intergroup_dist, test_intragroup_dist)
    if not expect_circle_by_circumference(circle,
                                          expected_circumference):
        print(f"Single chair test {test_num} failed")

    test_num = 4
    test_groups = DinnerGroups()
    test_chair_width = 2
    test_intragroup_dist = 1
    test_intergroup_dist = 0
    test_groups.add_group_size_with_cnt(1, 3)
    expected_circumference = 6

    circle = test_groups.calc_min_safe_circle(test_chair_width, test_intergroup_dist, test_intragroup_dist)
    if not expect_circle_by_circumference(circle,
                                          expected_circumference):
        print(f"Single chair test {test_num} failed")

    test_num = 5
    test_groups = DinnerGroups()

    test_chair_width = 2
    test_intragroup_dist = 1
    test_intergroup_dist = 6
    test_groups.add_group_size_with_cnt(2, 3)
    expected_circumference = 33

    circle = test_groups.calc_min_safe_circle(test_chair_width, test_intergroup_dist, test_intragroup_dist)
    if not expect_circle_by_circumference(circle,
                                          expected_circumference):
        print(f"Single chair test {test_num} failed")


def test_mixed_size_dinner_groups():
    print(" ----------------------------")
    print("| Testing multi chair groups |")
    print(" ----------------------------")
    test_num = 1
    test_groups = DinnerGroups()

    test_chair_width = 2
    test_intragroup_dist = 1
    test_intergroup_dist = 6
    test_groups.add_group_size_with_cnt(1, 3)
    test_groups.add_group_size_with_cnt(2, 2)
    test_groups.add_group_size_with_cnt(3, 3)
    expected_circumference = 88

    circle = test_groups.calc_min_safe_circle(test_chair_width, test_intergroup_dist, test_intragroup_dist)
    if not expect_circle_by_circumference(circle,
                                          expected_circumference):
        print(f"Multi chair test {test_num} failed")

    test_num = 2
    test_groups = DinnerGroups()

    test_chair_width = 2
    test_intragroup_dist = 1
    test_intergroup_dist = 6
    test_groups.add_group_size_with_cnt(1, 3)
    test_groups.add_group_size_with_cnt(2, 2)
    test_groups.add_group_size_with_cnt(3, 3)
    test_groups.add_group_size_with_cnt(3, 3)
    expected_circumference = 130

    circle = test_groups.calc_min_safe_circle(test_chair_width, test_intergroup_dist, test_intragroup_dist)
    if not expect_circle_by_circumference(circle,
                                          expected_circumference):
        print(f"Multi chair test {test_num} failed")


def expect_circle_by_circumference(circle, expected_circumference, tol=0.01):
    expected_radius = expected_circumference / (2 * math.pi)
    expected_area = math.pi * expected_radius ** 2

    success = True
    if not test_float(circle.radius, expected_radius, tol):
        success = False
        print(f"Incorrect radius. Expected {to_ft_str(expected_radius)},"
              f" Actual {to_ft_str(circle.radius)}")

    if not test_float(circle.circumference, expected_circumference, tol):
        success = False
        print(f"Incorrect circumference. Expected {to_ft_str(expected_circumference)},"
              f" Actual {to_ft_str(circle.circumference)}")

    if not test_float(circle.area, expected_area, tol):
        success = False
        print(f"Incorrect area. Expected {to_ft_str(expected_area)},"
              f" Actual {to_ft_str(circle.area)}")

    if not success:
        print(circle)

    return success


def test_float(actual, expected, tol):
    return abs(actual - expected) < tol