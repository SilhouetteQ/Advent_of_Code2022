# find how many units of sand come to rest

def main():
    with open('day14.txt') as f:
        l = f.readlines()
        info = {}
        for num, _ in enumerate(l):
            info_value = []
            s = _.split()
            for i in s:
                if i[0].isdigit():
                    j = i.split(',')
                    x = int(j[0])
                    y = int(j[1])
                    info_value.append([x, y])
            # info is a dictionary with line number as key and a position list as value
            info[num] = info_value
    # x is a list with all possible horizontal values
    x = all_poss(info, 0)
    # y is a list with all possible vertical values
    y = all_poss(info, 1)
    # calculate the limit of the cave, the min_y is 0 by default
    max_x = max(x)
    min_x = min(x)
    max_y = max(y)
    # use a 2d array to store the rock(True) and sand(False)
    # (min_x, 0),       ...,    (max_x, 0)
    #                   ...
    # (min_x, max_y),   ...,    (max_x, max_y)
    scan = [[False for x in range(min_x, max_x + 1)] for y in range(0, max_y + 1)]
    # fill the rocks
    fill(min_x, info, scan, 0)
    # [pour_x, pour_y] is the relative position of pouring site
    pour_x = 500 - min_x
    pour_y = 0
    part1 = count_sand(0, scan, pour_x, pour_y, max_x - min_x, max_y)
    print(part1)

    max_y += 2
    # max_x can be determined by max_y
    max_x = 2 * (max_y + 1) - 1
    # pour_x1 is the relative position of horizontal pouring site
    # it can be determined by max_x because of symmetry
    pour_x1 = int((max_x - 1) / 2)
    up_scan = [[False for x in range(max_x)] for y in range(max_y + 1)]
    adj = pour_x1 - pour_x
    # fill the rocks
    fill(min_x, info, up_scan, adj)
    # the bottom is also a line of rocks
    up_scan[max_y] = [True for x in range(max_x)]
    # for part2, it stops when the sand reach y=0,
    # but the sand is not counted yet, so here the starting value is 1
    part2 = count_sand(1, up_scan, pour_x1, pour_y, max_x, max_y)
    print(part2)


def all_poss(info, num):
    a = [[i[num] for i in info[j]] for j in info.keys()]
    flat = [_ for sub in a for _ in sub]
    return flat


def fill(min_x, info, scan, adjust):
    # iterate through each line
    for i in info:
        # iterate through the transition, j is the coordinate [x, y]
        for _, j in enumerate(info[i]):
            # designed for part 2, adjusting the horizontal position
            j[0] += adjust
            if _ == 0:
                cur_x = j[0] - min_x
                cur_y = j[1]
            else:
                # horizontal line
                if j[0] - min_x != cur_x:
                    gap = gap_value(j[0] - min_x, cur_x)
                    for g in gap:
                        scan[cur_y][g] = True
                    cur_x = j[0] - min_x
                # vertical line
                else:
                    gap = gap_value(j[1], cur_y)
                    for g in gap:
                        scan[g][cur_x] = True
                    cur_y = j[1]


def count_sand(n, scan, pour_x, pour_y, max_x, max_y):
    # pour() is a boolean function that determines whether the sand can be poured
    while pour(scan, pour_x, pour_y, max_x, max_y):
        n += 1
    return n


def pour(scan, x, y, max_x, max_y):
    # if pouring is within the cave
    if 0 <= x < max_x and y < max_y:
        # check moving one step down, if True, it means there is a rock blocking
        if scan[y + 1][x]:
            # check moving left down
            if scan[y + 1][x - 1]:
                # check moving right down
                if scan[y + 1][x + 1]:
                    scan[y][x] = True
                    # ending for part2, when the sand reach the top
                    if y == 0:
                        return False
                else:
                    # move left down and check
                    if not pour(scan, x + 1, y + 1, max_x, max_y):
                        return False
            else:
                # move left down and check
                if not pour(scan, x - 1, y + 1, max_x, max_y):
                    return False
        else:
            # move one step down and check
            if not pour(scan, x, y + 1, max_x, max_y):
                return False
        # base case, which means this position can be poured
        return True
    else:
        return False


# find the values between val1 and val2
def gap_value(val1, val2):
    if val1 > val2:
        return list(range(val2, val1 + 1))
    else:
        return list(range(val1, val2 + 1))


if __name__ == '__main__':
    main()
