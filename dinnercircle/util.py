# Constants
min_safe_dist_ft = 6


def is_unsafe(dist):
    return dist < min_safe_dist_ft


def to_ft_str(length_ft):
    ft = int(length_ft)
    inches = 12 * (length_ft - ft)
    return f"{ft:0}'{round(inches)}\""