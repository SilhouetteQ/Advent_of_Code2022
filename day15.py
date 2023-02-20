# 1. find how many positions cannot contain a beacon in row 2000000.
# 2. find tuning frequency of the only possible position for the distress beacon.
import re


def main():
    with open('day15.txt') as f:
        l = f.readlines()
        # sb is a dictionary with sensor position as key and beacon position as value
        sb = {}
        for _ in l:
            # the number can be negative
            s = re.findall(r'-?\d+', _)
            sensor = (int(s[0]), int(s[1]))
            beacon = (int(s[2]), int(s[3]))
            sb[sensor] = beacon
        part1(sb)
        for row in range(4000000 + 1):
            m = part2(sb, row)
            if m is not None:
                print(m)
                break


def find_range(sb, row):
    col = []
    for i in sb.keys():
        # gap is the Manhattan distance between sensor and beacon
        gap = abs(sb[i][0] - i[0]) + abs(sb[i][1] - i[1])
        # over is the horizontal distance away from projected point on specific row
        over = gap - abs(row - i[1])
        # over > 0 means this point is within the range
        if over >= 0:
            # col stores all possible ranges that cannot contain a beacon
            col.append([i[0] - over, i[0] + over])
    b = []
    # integrate all possible ranges
    for left, right in sorted(col):
        # if b is not empty and
        # the largest value of b is larger than the current leftmost range
        if b and b[-1][1] >= left - 1:
            # update the new largest value of b
            b[-1][1] = max(b[-1][1], right)
        else:
            b.append([left, right])
    return b


def part1(sb):
    row = 2000000
    b = find_range(sb, row)
    total = 0
    for i in b:
        # count the total value out of b
        total += i[1] - i[0] + 1

    # find beacons in targeted row
    bec_out = []
    for j in sb.values():
        if j[1] == row:
            if j[0] not in bec_out:
                bec_out.append(j[0])
    out = 0
    # find beacons that are in the above possible ranges
    for i in bec_out:
        for j in b:
            if j[0] <= i <= j[1]:
                out += 1
    print(total - out)


def part2(sb, row):
    b = find_range(sb, row)
    if len(b) > 1:
        # consider the only possible position, it should be a value in the middle of two ranges
        return row + 4000000 * (b[0][1] + 1)


if __name__ == '__main__':
    main()
