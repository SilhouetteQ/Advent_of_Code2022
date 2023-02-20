# find the crate ends up on top of each stack
import re
from collections import defaultdict

def ind(s):
    it = re.finditer(r"\d+", s)
    char_pos = []
    for _ in it:
        # find the index of the matched string
        char_pos.append(_.start())
    return char_pos


# store corresponding letters list in each position
def build_dict(pos, l):
    nd = defaultdict(list)
    ### store each letter in list
    for _ in l[:8]:
        for i, j in enumerate(pos, start=1):
            if _[j] != ' ':
                nd[i].append(_[j])
    return nd


def p(nd):
    strl = []
    for i in range(1, 10):
        if nd[i] != []:
            strl.append(nd[i][0])
    print(''.join(strl))


def part1(l, pos):
    nd = build_dict(pos, l)
    for _ in l[10:]:
        # extract rearrangement
        m = re.findall("\d+", _)
        m1 = int(m[0])
        m2 = int(m[1])
        m3 = int(m[2])
        # move crates in a one-by-one mode
        for i in range(m1):
            nd[m3].insert(0, nd[m2].pop(0))
    # find the top crate on each stack
    p(nd)


def part2(l, pos):
    nd = build_dict(pos, l)
    for _ in l[10:]:
        m = re.findall("\d+", _)
        m1 = int(m[0])
        m2 = int(m[1])
        m3 = int(m[2])
        # move crates in a whole mode
        nd[m3] = nd[m2][:(m1)] + nd[m3]
        del nd[m2][0:m1]
    # find the top crate on each stack
    p(nd)


def main():
    with open('day05.txt') as f:
        l = f.readlines()
        index_line = l[8]
        ### find the position of each letters
        pos = ind(index_line)
        part1(l, pos)
        part2(l, pos)


if __name__ == '__main__':
    main()
