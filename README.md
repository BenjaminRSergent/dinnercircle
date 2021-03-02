# Dinner Circle
Requires python 3

This is a calculator that determines the minimum circle size to socially distance dinner guests according to CDC guidelines.

It allows people in the same quarantine bubble to sit next to each other without distancing to further reduce the circle size and average distance between guests. It assumes all chairs are reasonable close in width.

Examples

three individuals with no bubbles using 2ft chairs
<pre>
python calc-dinner-circle --chair_width=2 --groups 3 1
</pre>

four individuals with two bubbles of size 2 using 2.5ft chairs
<pre>
python calc-dinner-circle --chair_width=2.5 --groups 4 1 2 2
</pre>

two individuals with two bubbles of size 2 and one group of 4 using 2.5ft chairs
<pre>
python calc-dinner-circle --chair_width=2.5 --groups 3 1 2 2 1 4
</pre>

<pre>
usage: calc-dinner-circle [-h] [--run_tests] [--chair_width CHAIR_WIDTH]
                          [--chair_spacing CHAIR_SPACING]
                          [--group_spacing GROUP_SPACING]
                          [--groups GROUPS [GROUPS ...]]

Calculate the size of socially distanced circle for dinner groups.If the
caller does not provide arguments, the manual_test function will run

optional arguments:
  -h, --help            show this help message and exit
  --run_tests           run the tests
  --chair_width CHAIR_WIDTH
                        The width of each chair from the left edge to the
                        right edge in feet
  --chair_spacing CHAIR_SPACING
                        The spacing between chairs in a group in feet. Default 1
  --group_spacing GROUP_SPACING
                        The spacing between groups of chairs. Default 6
  --groups GROUPS [GROUPS ...]
                        Counts of each group size. For example, the following
                        uses 3 groups of size 1, 2 groups of size 2 and 1
                        group of size 3 
                        calc-dinner-circle --chair_width=2.5 --groups 3 1 2 2 1 3

Process finished with exit code 0
</pre>
