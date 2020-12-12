# aoc_2020_01b
INPUT_EXT = '.txt'
INPUT_DIR = 'data/'
def iget(file):
    with open(file, 'r') as f:
        return f.read()

inp = iget(INPUT_DIR + __file__[:-3] + INPUT_EXT)
items = (n for n in inp.splitlines())
xs = [item.split()[0].split('-') + [item.split()[1][:1]] + [item.split()[2]] for item in items]
num_good_pwds = sum(int(x[0]) <= x[3].count(x[2]) <= int(x[1]) for x in xs)
new_num_good_pwds = sum((x[3][int(x[0]) - 1] == x[2]) != (x[3][int(x[1]) - 1] == x[2]) for x in xs)
# part 1
print(num_good_pwds)
# part 2
print(new_num_good_pwds)
