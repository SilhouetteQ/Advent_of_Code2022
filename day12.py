# 1. find the fewest steps required to move from 'S' to 'E'
# 2. start is changed to any square with elevation 'a', find the same question as 1
def main():
    with open('day12.txt') as f:
        l = f.readlines()
        # edge, objs, start_info, end_info
        e, objs, start, end = read_graph(l)
        part1(e, start, end)
        all_a = find_a(objs, l)
        part2(all_a, e, end)


def part1(g, start, end):
    a = find_solution(g, start, end)
    print(a[start])


def part2(a, e, end):
    path = []
    for j in a:
        c = find_solution(e, j, end)
        if j in c:
            path.append(c[j])
    print(min(path))


class Node:
    def __init__(self, x, y, id):
        self.x = x
        self.y = y
        self.id = id


def read_graph(l0):
    edge = {}
    objs = []
    l = list()
    # change 'E' into z, change 'S' into a
    # by converting string to list, and converting list back to string
    for row_num, i in enumerate(l0):
        j_in_row = list(i)
        for col_num, j in enumerate(i.strip()):
            if j == 'E':
                j = 'z'
                j_in_row[col_num] = 'z'
                # store object E as end_info
                end_info = Node(row_num, col_num, j)
                objs.append(end_info)
                continue
            if j == 'S':
                j = 'a'
                j_in_row[col_num] = 'a'
                # store object S as start_info
                start_info = Node(row_num, col_num, j)
                objs.append(start_info)
                continue
            # store each letter as an object Node(), initialized by its coordinate and elevation.
            objs.append(Node(row_num, col_num, j))
        i1 = ''.join(j_in_row)
        l.append(i1)
    for row_num, i in enumerate(l):
        for col_num, j in enumerate(i.strip()):
            # key is the current object
            key = objs[row_num * (len(l[0]) - 1) + col_num]
            # edge is a dictionary with key as the current object
            # and value as all possible objects that can be reached by the current object
            edge[key] = []
            ### go down
            if row_num < len(l) - 1 and (
                    ord(l[row_num + 1][col_num]) - ord(j) == 0 or ord(l[row_num + 1][col_num]) - ord(j) == -1 or ord(
                l[row_num + 1][col_num]) > ord(j)):
                value = objs[(row_num + 1) * (len(l[0]) - 1) + col_num]
                edge[key].append(value)
            ### go right
            if col_num < len(i) - 1 and (
                    ord(l[row_num][col_num + 1]) - ord(j) == 0 or ord(l[row_num][col_num + 1]) - ord(j) == -1 or ord(
                l[row_num][col_num + 1]) > ord(j)):
                value = objs[(row_num) * (len(l[0]) - 1) + col_num + 1]
                edge[key].append(value)
            ### go up
            if row_num > 0 and (
                    ord(l[row_num - 1][col_num]) - ord(j) == 0 or ord(l[row_num - 1][col_num]) - ord(j) == -1 or ord(
                l[row_num - 1][col_num]) > ord(j)):
                value = objs[(row_num - 1) * (len(l[0]) - 1) + col_num]
                edge[key].append(value)
            ### go left
            if col_num > 0 and (
                    ord(l[row_num][col_num - 1]) - ord(j) == 0 or ord(l[row_num][col_num - 1]) - ord(j) == -1 or ord(
                l[row_num][col_num - 1]) > ord(j)):
                value = objs[(row_num) * (len(l[0]) - 1) + col_num - 1]
                edge[key].append(value)
    return edge, objs, start_info, end_info


def find_a(objs, l):
    a_info = []
    for row_num, i in enumerate(l):
        for col_num, j in enumerate(i.strip()):
            if j == 'a':
                a_info.append(objs[row_num * (len(l[0]) - 1) + col_num])
    return a_info


def find_solution(e, start, end):
    # explore_set store objects to be explored
    explore_set = [end]
    # dis is a dictionary with the object as key and
    # the steps moved so far as value
    dis = {end: 0}
    while explore_set:
        cur = explore_set.pop(0)
        for i in e[cur]:
            if i not in dis:
                dis[i] = dis[cur] + 1
                if i == start:
                    return dis
                explore_set.append(i)
    return dis


if __name__ == '__main__':
    main()
