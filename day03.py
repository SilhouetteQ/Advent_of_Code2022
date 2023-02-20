# find the sum of the priorities of specific item types
import string


def part1(l, prior_dict):
    prior_sum = 0
    for _ in l:
        sl = len(_.strip())
        # letters from the first half
        fh = _[:int(sl / 2)]
        # letters from the second half
        sh = _[int(sl / 2):]
        overlap = []
        # find shared letters and sum up their priorities
        for i in sh:
            if i in fh and i not in overlap:
                prior_value = prior_dict[i]
                prior_sum += prior_value
                overlap.append(i)
    print(prior_sum)


def part2(l, prior_dict):
    prior_sum = 0
    overlap = []
    for num, line in enumerate(l, start=1):
        # line 1 in each iteration
        if num % 3 == 1:
            l1 = line.strip()
        # line 2 in each iteration
        elif num % 3 == 2:
            overlap = []
            for i in l1:
                if i in line.strip() and i not in overlap:
                    overlap.append(i)
        # line 3 in each iteration
        else:
            for i in overlap:
                if i in line.strip():
                    prior_value = prior_dict[i]
                    prior_sum += prior_value
    print(prior_sum)


def main():
    prior_dict = {}
    start = 1
    # give priority to lowercase and uppercase letters
    for letter in string.ascii_lowercase:
        prior_dict[letter] = start
        start += 1
    for letter in string.ascii_uppercase:
        prior_dict[letter] = start
        start += 1

    with open('day03.txt') as f:
        l = f.readlines()
        part1(l, prior_dict)
        part2(l, prior_dict)


if __name__ == '__main__':
    main()
