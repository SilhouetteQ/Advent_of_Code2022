# convert sum of SNAFU numbers to decimal, and convert it back to SNAFU
def main():
    with open('day25.txt') as f:
        l = f.readlines()
        tol = 0
        for _ in l:
            tol += to_decimal(_.strip())
        print(to_snafu(tol))

    print(to_snafu(12345))

def to_snafu(val):
    # base case: value = 0
    if val == 0:
        return ''
    match val % 5:
        case 1:
            # iterate through the power of 5: 1, 5, 25, ...
            return to_snafu(val // 5) + '1'
        case 2:
            return to_snafu(val // 5) + '2'
        case 3:
            return to_snafu(1 + val // 5) + '='
        case 4:
            return to_snafu(1 + val // 5) + '-'
        case 0:
            return to_snafu(val // 5) + '0'


def to_decimal(line):
    cl = len(line)
    val = 0
    # iterate the line from left to right
    for num, i in enumerate(line):
        base = pow(5, cl - num - 1)
        match i:
            case '1':
                val += base
            case '2':
                val += base * 2
            case '0':
                pass
            case '-':
                val -= base
            case '=':
                val -= base * 2
    return val


if __name__ == '__main__':
    main()
