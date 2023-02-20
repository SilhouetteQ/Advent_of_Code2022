# Find the surface area of your scanned lava droplet
import re


def main():
    with open('day18.txt') as f:
        l = f.readlines()
        val_list = []
        for _ in l:
            s = re.findall(r'\d+', _)
            # store all possible positions in a list
            val_list.append((int(s[0]), int(s[1]), int(s[2])))
        part1(val_list)


def part1(val_list):
    total = len(val_list) * 6
    while len(val_list) > 0:
        a = val_list.pop()
        for b in val_list:
            # for each position, if it has an absolute distance of 1 to other position, the total area will deduce by 2
            if abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2]) == 1:
                total -= 2
    print(total)


if __name__ == '__main__':
    main()
