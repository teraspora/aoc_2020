# aoc_2020_01b

from itertools import combinations

def iget(file):
    with open(file, 'r') as f:
        return f.read()
        
# lines = iget('aoc_2020_01a_input.txt')
# nums = (int(n) for n in lines.split())
# triples = combinations(nums, 3)
# xs = [(p, q, r) for p, q, r in triples if p + q + r == 2020]
# if len(xs) == 1:
#     print(xs[0][0] * xs[0][1] * xs[0][2])

print(__file__[:-3])

