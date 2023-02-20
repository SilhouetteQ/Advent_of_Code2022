# find the number of characters need to be processed
import collections


### taken from the idea in itertools usage https://docs.python.org/3/library/itertools.html#itertools.count
def sliding_window(iterable, n):
    window = collections.deque(iterable[:n], n)
    # for the first n case
    if len(window) == n:
        yield list(window)
    # make use of deque property,
    # Once a bounded length deque is full, when new items are added,
    # a corresponding number of items are discarded from the opposite end.
    for x in iterable[n:]:
        window.append(x)
        yield list(window)


### use a set to store unique values
def dup(lis):
    s = set()
    for i in lis:
        if i not in s:
            s.add(i)
        else:
            return False
    return True


def findS(l, s):
    # iterate through the string with four letters each time.
    for num, four in enumerate(sliding_window(l[0], s), start=s):
        if dup(four):
            print(num)
            break
        else:
            pass


def part1(l):
    # after the 4th character arrives, the marker shows up.
    findS(l, 4)


def part2(l):
    # after the 14th character arrives, the marker shows up.
    findS(l, 14)


def main():
    with open('day06.txt') as f:
        l = f.readlines()
        part1(l)
        part2(l)


if __name__ == '__main__':
    main()
