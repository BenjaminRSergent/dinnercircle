import argparse

from dinnercircle.dinnergroups import DinnerGroups


def calc_dinner_circle(args):
    if args.run_tests:
        from dinnercircle.dinnergrouptests import test_dinner_groups
        test_dinner_groups()
    elif args.chair_width:
        if len(args.groups) % 2 == 1:
            print("Error: Odd number of group arguments.")
            return False

        group_cnts = [(args.groups[idx + 1], args.groups[idx]) for idx in range(0, len(args.groups), 2)]

        run_calc(args.chair_width, args.group_spacing, args.chair_spacing, group_cnts)
    else:
        manual_test()

    return True


def manual_test():
    # Use this if you can't be arsed to use the cmd arguments
    chair_width = 2.5
    group_spacing = 6
    chair_spacing = 1
    group_cnts = [(3, 1), (2, 2), (1,3)]
    run_calc(chair_width, group_spacing, chair_spacing, group_cnts)


def run_calc(chair_width, group_spacing, chair_spacing, group_cnts):
    groups = DinnerGroups()

    for pair in group_cnts:
        groups.add_group_size_with_cnt(pair[0], pair[1])

    print(groups.calc_min_safe_circle(chair_width, group_spacing, chair_spacing))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Calculate the size of socially distanced circle for dinner groups.'
                    'If the caller does not provide arguments, '
                    'the manual_test function will run')
    parser.add_argument('--run_tests', required=False, action='store_true',
                        help='run the tests')
    parser.add_argument('--chair_width', type=float,
                        help='The width of each chair from the left edge to the right edge in feet')
    parser.add_argument('--chair_spacing', type=float, default=1,
                        help='The spacing between chairs in a group in feet')
    parser.add_argument('--group_spacing', type=float, default=6,
                        help='The spacing between groups of chairs')

    parser.add_argument('--groups', type=int, nargs='+',
                        help='Counts of each group size. For example, the following uses 3 groups of size 1, 2'
                             ' groups of size 2 and 1 group of size 3\n'
                             'calc-dinner-circle --chair_width=2.5 --groups 3 1 2 2 1 3')

    args = parser.parse_args()
    if not calc_dinner_circle(args):
        parser.print_help()
