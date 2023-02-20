# find the number of positions that have been visited
class Point:
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y

    def move(self, dir):
        match dir:
            case 'R':
                self.x += 1
            case 'D':
                self.y -= 1
            case 'L':
                self.x -= 1
            case 'U':
                self.y += 1

    def move_follow(self, other, dir):
        if not isinstance(other, type(self)):
            raise TypeError(f"{type(self)} is not the same as {type(other)}")
        # if the absolute distance is within 1, no need to move
        if abs(other.x - self.x) <= 1 and abs(other.y - self.y) <= 1:
            pass
        # if the absolute distance of x equals 2
        elif abs(other.x - self.x) == 2:
            if self.y == other.y:
                self.move(dir)
            else:
                self.y = other.y
                self.move(dir)
        # if the absolute distance of y equals 2
        elif abs(other.y - self.y) == 2:
            if self.x == other.x:
                self.move(dir)
            else:
                self.x = other.x
                self.move(dir)

    def child_move_follow(self, other):
        if not isinstance(other, type(self)):
            raise TypeError(f"{type(self)} is not the same as {type(other)}")
        if abs(other.x - self.x) <= 1 and abs(other.y - self.y) <= 1:
            pass
        elif abs(other.x - self.x) == 2:
            self.x = (other.x + self.x) / 2
            if self.y == other.y:
                pass
            elif abs(other.y - self.y) == 1:
                self.y = other.y
            else:
                self.y = (other.y + self.y) / 2
        elif abs(other.y - self.y) == 2:
            self.y = (other.y + self.y) / 2
            if self.x == other.x:
                pass
            else:
                self.x = other.x


def part1(l):
    # head
    p = Point(0, 0)
    # tail
    t = Point(0, 0)
    t_list = set()
    t_list.add((0, 0))
    for _ in l:
        ## s[0] is the direction, s[1] is the steps
        s = _.split()
        for i in range(int(s[1])):
            # change the position of p by direction
            p.move(s[0])
            t.move_follow(p, s[0])
            # keep track of pass-by positions
            t_list.add((t.x, t.y))
    print(len(t_list))


def part2(l):
    t_list = set()
    t_list.add((0, 0))
    p = Point(0, 0)
    objs = [Point() for i in range(9)]
    for _ in l:
        ## s[0] is the direction, s[1] is the steps
        s = _.split()
        iter_time = 9
        for i in range(int(s[1])):
            # head moves by file
            p.move(s[0])
            # first tail moves by head
            objs[0].move_follow(p, s[0])
            for i in range(1, iter_time):
                # other tails move along with the first tail
                objs[i].child_move_follow(objs[i - 1])
            # keep track of pass-by positions
            t_list.add((objs[iter_time - 1].x, objs[iter_time - 1].y))
    print(len(t_list))


def main():
    with open('day09.txt') as f:
        l = f.readlines()
        part1(l)
        part2(l)


if __name__ == '__main__':
    main()
