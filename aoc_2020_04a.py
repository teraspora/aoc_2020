import sys, string
from aoc_io import get_input

def is_valid(ppd):
    if not all(key in ppd for key in keys[:-1]):
        return False
    for k in ppd:
        v = ppd[k]
        if k == 'byr':
            if len(v) != 4 or not v.isdigit():
                return False
            iv = int(v)
            if not 1920 <= iv <= 2002:
                return False
            continue
        if k == 'iyr':
            if len(v) != 4 or not v.isdigit():
                return False
            iv = int(v)
            if not 2010 <= iv <= 2020:
                return False
            continue
        if k == 'eyr':
            if len(v) != 4 or not v.isdigit():
                return False
            iv = int(v)
            if not 2020 <= iv <= 2030:
                return False
            continue
        if k == 'hgt':
            n = v[:-2]
            unit = v[-2:]
            if not (unit in ['cm', 'in'] and n.replace('.', '', 1).isdigit()):
                return False
            n = float(n)
            if not ((unit == 'cm' and 150 <= n <= 193) or (unit == 'in' and 59 <= n <= 76)):
                return False
            continue
        if k == 'hcl':
            if len(v) != 7 or v[0] != '#' or not all(ch in valid_hex for ch in v[1:]):
                return False
            continue
        if k == 'ecl':
            if v not in valid_ecl:
                return False
            continue
        if k == 'pid':
            if not (len(v) == 9 and v.isdigit()):
                return False
    return True


inp = get_input(__file__, test=False if len(sys.argv) == 1 else True)
keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
valid_hex = ''.join([*set(string.hexdigits.lower())])
valid_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

pps = inp.split('\n\n')
ppds = [dict([kv.split(':') for kv in pp.split()]) for pp in pps]
total_valid = sum(is_valid(ppd) for ppd in ppds)
print(f"{total_valid=}")
