# 1. find the sum of the total sizes of directories
# 2. find the total size of the smallest directory that, if deleted,
# would free up enough space on the filesystem to run the update

class Node:
    def __init__(self, parent):
        self.size = 0
        self.child = {}
        self.parent = parent
    # a recursive function, increasing the size of parent nodes upwardly
    def increase_size(self, x):
        self.size += x
        if self.parent is not None:
            self.parent.increase_size(x)


def find_under(limit, m, under):
    for _ in m.child.values():
        # only apply to node
        if isinstance(_, Node):
            # sum up all directories that have an under limit size
            if _.size <= limit:
                under += _.size
            under = find_under(limit, _, under)
    return under


def find_above(limit, m, above):
    for _ in m.child.values():
        if isinstance(_, Node):
            # add all qualified sizes in a set
            if _.size > limit:
                above.add(_.size)
            find_above(limit, _, above)


def buildNode(l):
    # represent root node, which has no parent
    node = Node(None)
    # store information in a linked list mode, with each directory represented by a node.
    for _, j in enumerate(l):
        s = j.split()
        # input line
        if s[0] == '$':
            if s[1] == 'cd':
                # node.child is a dictionary, with the name of the node as key,
                # and the corresponding node object as value
                if s[2] in node.child:
                    # node travels down to the child node
                    node = node.child[s[2]]
                # represent $ cd ..
                # node travels up to the parent node
                elif node.parent is not None:
                    node = node.parent
                # only root node has no parent
                else:
                    continue
            # represent $ ls
            else:
                continue
        # output line
        else:
            # encounter a directory, store the name as key and
            # its corresponding node object as value
            if s[0] == 'dir':
                node.child[s[1]] = Node(node)
            # encounter a file, add its size to all parent nodes
            else:
                node.increase_size(int(s[0]))
    # iterate node back to the root directory
    while node.parent is not None:
        node = node.parent
    return node


def main():
    with open('day07.txt') as f:
        l = f.readlines()
        # node is the root directory
        node = buildNode(l)
        # part1
        a = find_under(100000, node, 0)
        print(a)
        # part2
        above = set()
        find_above(30000000 + node.size - 70000000, node, above)
        print(min(above))


if __name__ == '__main__':
    main()
