# find the sum of the indices of pairs in right order

def main():
    with open('day13.txt') as f:
        l = f.readlines()
        pair1 = {}
        pair2 = {}
        pair_num = 1
        p2 = 0
        for num, i in enumerate(l):
            # line 1
            if num % 3 == 0:
                # convert the string into list
                ie = eval(i)
                pair1[pair_num] = ie
                p2 += 1
            # line 2
            elif num % 3 == 1:
                ie = eval(i)
                pair2[pair_num] = ie
                pair_num += 1
                p2 += 1

        part1(pair1, pair2, pair_num)
        part2(p2, pair1, pair2)


def part1(pair1, pair2, pair_num):
    right_pair = []
    for i in range(1, pair_num):
        # compare() is a boolean function that compare the order of a pair and return True or False
        if compare(pair1[i], pair2[i]):
            right_pair.append(i)
    print(sum(right_pair))


def part2(p2, pair1, pair2):
    # p2 is the number of total pairs
    for i in range(1, int(p2 / 2 + 1)):
        if i == 1:
            # make the first item in pair one as root
            # sort the items in a tree structure
            root = Tree(pair1[i])
            # insert node to the left of the tree if it is smaller else insert to the right
            if compare(pair1[i], pair2[i]):
                root.right = Tree(pair2[i])
            else:
                root.left = Tree(pair2[i])
        else:
            ele1 = pair1[i]
            ele2 = pair2[i]
            # tree_compare() is a function that add node into the tree
            tree_compare(root, ele1)
            tree_compare(root, ele2)

    # insert two new node to the tree
    tree_compare(root, [[2]])
    tree_compare(root, [[6]])
    # convert the tree information in a list using recursion
    # refer to the tree sort algorithm, https://www.geeksforgeeks.org/tree-sort/
    a = []
    inorderRec(root, a)
    decode = (a.index([[2]]) + 1) * (a.index([[6]]) + 1)
    print(decode)


class Tree:
    def __init__(self, value, small=None, large=None):
        self.value = value
        self.left = small
        self.right = large


def compare(l1, l2):
    com = min(len(l1), len(l2))
    # one of them run out
    if com == 0:
        if len(l1) == 0 and len(l2) > 0:
            return True
        elif len(l1) > 0 and len(l2) == 0:
            return False
    for i in range(com):
        # both are integers
        if isinstance(l1[i], int) and isinstance(l2[i], int):
            if l1[i] > l2[i]:
                return False
            elif l1[i] < l2[i]:
                return True
            # when these two integers are equal and one of them is the last item in the list
            if i == com - 1:
                if len(l1) > len(l2):
                    return False
                else:
                    return True
        # list exist
        else:
            # compare them with specified index
            x = l1[i]
            y = l2[i]
            if isinstance(l1[i], int):
                x = [x]
            if isinstance(l2[i], int):
                y = [y]
            if x == y:
                if i == com - 1:
                    if len(l1) > len(l2):
                        return False
                    elif len(l1) < len(l2):
                        return True
            else:
                return compare(x, y)


def tree_compare(node, val):
    # should be on the right branch
    if compare(node.value, val):
        if node.right is None:
            node.right = Tree(val)
        else:
            node = node.right
            tree_compare(node, val)
    # should be on the left branch
    else:
        if node.left is None:
            node.left = Tree(val)
        else:
            node = node.left
            tree_compare(node, val)


def inorderRec(root, a):
    if root is not None:
        inorderRec(root.left, a)
        a.append(root.value)
        inorderRec(root.right, a)


if __name__ == '__main__':
    main()
