# find the 1000th, 2000th and 3000th number of a list that can be wrapped
from collections import deque

def main():
    with open('day20.txt') as f:
        l = f.readlines()
        part1(l)
        part2(l)

def part1(l):
    # create a list that store the original order (ori_list), a deque that store the numbers (de) and
    # a deque that store the corresponding index of the numbers (idx_to_de)
    ori_list, de, seq_len, idx_to_de = process1(l, 1)
    # mixing the numbers by  modifying de and idx_to_de
    process2(ori_list, de, seq_len, idx_to_de, False)
    a = find_numbers(seq_len, de)
    print(a)

def part2(l):
    # part2 is similar, except timing a key value and mix for 10 times
    ori_list, de, seq_len, idx_to_de = process1(l, 811589153)
    for i in range(10):
        process2(ori_list, de, seq_len, idx_to_de, True)
    a = find_numbers(seq_len, de)
    print(a)

def process1(l, key):
    seq_len = len(l)
    ori_list = []
    de = deque([])
    for i, _ in enumerate(l):
        t = int(_.strip()) * key
        ori_list.append(t)
        de.append(t)
    idx_to_de = deque(list(range(seq_len)))
    return ori_list, de, seq_len, idx_to_de

def process2(ori_list, de, seq_len, idx_to_de, p2):
    for num, j in enumerate(ori_list):
        # find the corresponding index of the number
        idx = idx_to_de.index(num)
        # if j = 0, do nothing
        if j != 0:
            # rotate left to the position of the target number,
            de.rotate(-idx)
            # pop out the number
            de.popleft()
            # rotate -j to reach the position of the number insertion site
            de.rotate(-j)
            # insert the number
            de.appendleft(j)
            # apply the same operation to idx_to_de
            idx_to_de.rotate(-idx)
            idx_to_de.popleft()
            idx_to_de.rotate(-j)
            idx_to_de.appendleft(num)
            # j > 0 means insert number to the right of the target
            if j > 0:
                # this happens when the number insert to its left due to rotation,
                # so when the sequence rotate back, it should rotate one more position
                if idx + j >= seq_len - 1:
                    de.rotate(j + 1)
                    idx_to_de.rotate(j + 1)
                else:
                    # when the number insert to its right
                    de.rotate(j)
                    idx_to_de.rotate(j)
            # when the number insert to the left of the target
            elif j < 0:
                de.rotate(j - 1)
                idx_to_de.rotate(j - 1)
            de.rotate(idx)
            idx_to_de.rotate(idx)
    # in p2, every mixing ends with 0 placed at the first position
    if p2:
        zero_pos = de.index(0)
        de.rotate(-zero_pos)
        idx_to_de.rotate(-zero_pos)


def find_numbers(seq_len, de):
    zero_pos = de.index(0)
    de.rotate(-zero_pos)
    par = [1000, 2000, 3000]
    # wrap the sequence until its length reach 3000
    add_numbers = 0
    for i in par:
        while seq_len <= i:
            de.extend(de)
            seq_len = len(de)
        add_numbers += de[i]
    return add_numbers


if __name__ == '__main__':
    main()
