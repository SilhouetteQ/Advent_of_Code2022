# 1. find assignment pairs that one range fully contain the other
# 2. find assignment pairs that ranges overlap
def main():
    ### PART 1
    import re
    with open('day04.txt') as f:
        l = f.readlines()
        cp = 0
        for _ in l:
            mat = re.split('(\d+)', _)
            # the number corresponds to pos 1, 3, 5, 7 in the list
            # consider two circumstances (1 (5, 7) 3) or (5 (1, 3) 7)
            if (int(mat[1]) <= int(mat[5]) and int(mat[3]) >= int(mat[7])) or (
                    int(mat[1]) >= int(mat[5]) and int(mat[3]) <= int(mat[7])):
                cp += 1
        print(cp)

        ### PART 2
        ncp = 0
        tot = 0
        for _ in l:
            tot += 1
            mat = re.split('(\d+)', _)
            # consider two circumstances (1, 3) (5, 7) or (5, 7) (1, 3)
            if (int(mat[3]) < int(mat[5])) or (int(mat[7]) < int(mat[1])):
                ncp += 1
        # partially overlap = all - non-overlap
        pcp = tot - ncp
        print(pcp)


if __name__ == '__main__':
    main()
