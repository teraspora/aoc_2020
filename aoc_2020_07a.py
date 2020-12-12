# aoc_2020_07a.py
"""
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""
"""
1. Change "bags" to "bag".                              >>> light red bag contain 1 bright white bag, 2 muted yellow bag.
2. Remove lines ending "contain no other bags."
3. Sort lines with "shiny gold bag" to top.
4. Strip spaces and "bag" from bag names.               >>> lightred contain 1 brightwhite, 2 mutedyellow
5. Replace "contain" with ":"and strip closing ".".     >>> lightred: 1 brightwhite, 2 mutedyellow
6. Separate multiple mappings.                          >>> lightred: 1 brightwhite
                                                        >>> lightred: 2 mutedyellow
7. Replace numbers with blanks.
"""

from aoc_io import get_input
import sys
import string


inp = get_input(__file__, test=False if len(sys.argv) == 1 else True)
rules = inp.split('\n\n')
print(f'{len(rules)=}')
for rule in rules[:12]:
    print(rule)

