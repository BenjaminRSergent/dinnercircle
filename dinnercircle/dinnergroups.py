import math

from collections import defaultdict

from dinnercircle.util import to_ft_str, min_safe_dist_ft, is_unsafe


class Circle:
    def __init__(self):
        self.circumference = 0
        self.radius = 0
        self.area = 0

    @staticmethod
    def from_circumference_ft(circumference_ft):
        ret = Circle()
        ret.circumference = circumference_ft
        ret.radius = circumference_ft / (2*math.pi)
        ret.area = math.pi * ret.radius**2

        return ret

    def __str__(self):
        diameter = self.radius*2
        ret = "Circle Properties\n"
        if is_unsafe(diameter):
            ret += f"Warning, the diameter {to_ft_str(diameter)} is less than {to_ft_str(min_safe_dist_ft)}\n"

        ret += f"Radius: {to_ft_str(self.radius)}\n"
        ret += f"Diameter: {to_ft_str(2*self.radius)}\n"
        ret += f"Circumference: {to_ft_str(self.circumference)}\n"
        ret += f"Area: {to_ft_str(self.area)}\n"

        return ret


class DinnerGroups:
    def __init__(self):
        self.group_of_size_cnt = defaultdict(int)

    def add_group_size_with_cnt(self, group_size, cnt):
        self.group_of_size_cnt[group_size] += cnt

    def calc_min_safe_circle(self, chair_width, intergroup_chair_dist, intragroup_chair_dist):
        if is_unsafe(intergroup_chair_dist):
            print(f"Warning: the distance between groups is unsafe at {to_ft_str(intergroup_chair_dist)}")

        circumference = 0
        for size, cnt in self.group_of_size_cnt.items():
            chair_length_per_group = size * chair_width
            # Beware fenceposts
            intragroup_space_per_group = (size - 1) * intragroup_chair_dist
            ft_added_per_group = (chair_length_per_group + intragroup_space_per_group + intergroup_chair_dist)
            circumference += cnt * ft_added_per_group

        return Circle.from_circumference_ft(circumference)
