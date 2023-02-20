# 1. find the number of trees that are visible
# 2. find the highest scenic score

class Point():
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.east, self.sou, self.west, self.nor = False, False, False, False
        self.e_acc, self.s_acc, self.w_acc, self.n_acc = 0, 0, 0, 0

    def vis(self, val1, val2):
        # trees on the edge can be visible
        if self.x == val1 or self.y == val2:
            return True
        # trees that can be visible in at least one direction
        elif self.east or self.sou or self.west or self.nor:
            return True
        else:
            return False

    def judge(self, dir):
        match dir:
            case 'E':
                self.east = True
            case 'S':
                self.sou = True
            case 'W':
                self.west = True
            case 'N':
                self.nor = True


def w_n(l, objs):
    max_w = {}
    max_n = {}
    for row_num in range(len(l)):
        for col_num in range(len(l[0]) - 1):
            cur = l[row_num][col_num]
            # record the tree height around the edge
            if row_num == 0:
                max_n[col_num] = cur
                continue
            if col_num == 0:
                max_w[row_num] = cur
                continue
            # if current height is larger than the current maximum west height
            if max_w[row_num] < cur:
                max_w[row_num] = cur
                objs[(row_num * (len(l[0]) - 1)) + col_num].judge('W')
            # if current height is larger than the current maximum north height
            if max_n[col_num] < cur:
                max_n[col_num] = cur
                objs[(row_num * (len(l[0]) - 1)) + col_num].judge('N')


def e_s(l, objs):
    max_e = {}
    max_s = {}
    for row_num in reversed(range(len(l))):
        for col_num in reversed(range(len(l[0]) - 1)):
            cur = l[row_num][col_num]
            # record the tree height around the edge
            if row_num == len(l) - 1:
                max_s[col_num] = cur
                continue
            if col_num == len(l[0]) - 2:
                max_e[row_num] = cur
                continue
            # if current height is larger than the current maximum east height
            if max_e[row_num] < cur:
                max_e[row_num] = cur
                objs[(row_num * (len(l[0]) - 1)) + col_num].judge('E')
            # if current height is larger than the current maximum south height
            if max_s[col_num] < cur:
                max_s[col_num] = cur
                objs[(row_num * (len(l[0]) - 1)) + col_num].judge('S')


def w_n1(l, objs):
    max_w = {}
    max_n = {}
    for row_num in range(len(l)):
        for col_num in range(len(l[0]) - 1):
            cur = l[row_num][col_num]
            if row_num == 0:
                max_n[col_num] = [cur]
                continue
            if col_num == 0:
                max_w[row_num] = [cur]
                continue
            # count how many trees are blocking the view in the west
            w_acc = 1
            for i, _ in enumerate(reversed(max_w[row_num])):
                if _ < cur:
                    if i == len(max_w[row_num]) - 1:
                        pass
                    else:
                        w_acc += 1
                else:
                    break
            objs[(row_num * (len(l[0]) - 1)) + col_num].w_acc = w_acc
            # count how many trees are blocking the view in the north
            n_acc = 1
            for i, _ in enumerate(reversed(max_n[col_num])):
                if _ < cur:
                    if i == len(max_n[col_num]) - 1:
                        pass
                    else:
                        n_acc += 1
                else:
                    break
            objs[(row_num * (len(l[0]) - 1)) + col_num].n_acc = n_acc
            max_w[row_num].append(cur)
            max_n[col_num].append(cur)


def e_s1(l, objs):
    max_e = {}
    max_s = {}
    for row_num in reversed(range(len(l))):
        for col_num in reversed(range(len(l[row_num]) - 1)):
            cur = l[row_num][col_num]
            if row_num == len(l) - 1:
                max_s[col_num] = [cur]
                continue
            if col_num == len(l[0]) - 2:
                max_e[row_num] = [cur]
                continue
            # count how many trees are blocking the view in the east
            e_acc = 1
            for i, _ in enumerate(reversed(max_e[row_num])):
                if _ < cur:
                    if i == len(max_e[row_num]) - 1:
                        pass
                    else:
                        e_acc += 1
                else:
                    break
            objs[(row_num * (len(l[0]) - 1)) + col_num].e_acc = e_acc
            # count how many trees are blocking the view in the south
            s_acc = 1
            for i, _ in enumerate(reversed(max_s[col_num])):
                if _ < cur:
                    if i == len(max_s[col_num]) - 1:
                        pass
                    else:
                        s_acc += 1
                else:
                    break
            objs[(row_num * (len(l[0]) - 1)) + col_num].s_acc = s_acc
            max_e[row_num].append(cur)
            max_s[col_num].append(cur)


def part1(l):
    # each letter becomes an object
    # store each object as a tree in a list
    objs = [Point(x, y) for x in range(len(l)) for y in range(len(l[0]) - 1)]
    # iterate from top-left, check whether the tree is visible in east and south direction
    e_s(l, objs)
    # iterate from bottom-right, check whether the tree is visible in west and north direction
    w_n(l, objs)

    vis_sum = 0
    for i in objs:
        # if the tree is visible in any direction
        if i.vis(0, 0) or i.vis(len(l) - 1, len(l[0]) - 2):
            vis_sum += 1
    print(vis_sum)


def part2(l):
    objs = [Point(x, y) for x in range(len(l)) for y in range(len(l[0]) - 1)]
    w_n1(l, objs)
    e_s1(l, objs)
    # find the highest scenic score
    val = max([(i.w_acc * i.n_acc * i.s_acc * i.e_acc) for i in objs])
    print(val)


def main():
    with open('day08.txt') as f:
        l = f.readlines()
        part1(l)
        part2(l)


if __name__ == '__main__':
    main()
