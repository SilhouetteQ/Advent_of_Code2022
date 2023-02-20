# find the units tall of the tower after 2022 rocks
import itertools


def main():
    with open("day17.txt") as f:
        l = f.readlines()[0].strip()
        rocks = [[(0, 0), (1, 0), (2, 0), (3, 0)], [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],
                 [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
                 [(0, 0), (0, 1), (0, 2), (0, 3)], [(0, 0), (1, 0), (0, 1), (1, 1)]]
        height = 0
        # ground is a list that stores all rock locations
        ground = set([(-2 + x, 0) for x in range(7)])
        # use iterator for rock
        rc = itertools.cycle(rocks)
        # iterator for direction
        di = itertools.cycle(l)
        for i in range(2022):
            landed = False
            rock = next(rc)
            # falling is the position for rock dropping
            # e.g., [(0, 4), (1, 4), (2, 4), (3, 4)]
            falling = [(x[0], x[1] + height + 4) for x in rock]
            while not landed:
                blow = next(di)
                if blow == "<":
                    test = [(x[0] - 1, x[1]) for x in falling]
                else:
                    test = [(x[0] + 1, x[1]) for x in falling]
                blocked = False
                # test whether moving left or right is possible
                for x in test:
                    if x in ground:
                        blocked = True
                    if x[0] < -2 or x[0] > 4:
                        blocked = True
                if not blocked:
                    # implement moving
                    falling = test

                test1 = [(x[0], x[1] - 1) for x in falling]
                # check whether moving down is possible
                for x in test1:
                    if x in ground:
                        landed = True
                if landed:
                    # store rock positions to the ground list
                    for x in falling:
                        ground.add(x)
                    # update the current highest position
                    # note that the last item in each rock is the highest
                    if height < falling[len(falling) - 1][1]:
                        height = falling[len(falling) - 1][1]
                else:
                    # implement moving
                    falling = test1

        # part1
        print(height)


if __name__ == "__main__":
    main()
