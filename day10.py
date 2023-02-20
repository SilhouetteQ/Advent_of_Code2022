# 1. find the sum of these six signal strengths
# 2. find the eight capital letters appear on the CRT
def part1(l):
    x = 1
    buffer = []
    val = []
    cur_cyc = 0
    for _ in l:
        s = _.split()
        if s[0] == 'noop' or s[0] == 'addx':
            # record the cycle
            cur_cyc += 1
            # if buffer is not empty
            if buffer:
                x += buffer.pop(0)
            val.append(x)
        if s[0] == 'addx':
            cur_cyc += 1
            if buffer:
                x += buffer.pop(0)
            buffer.append(int(s[1]))
            val.append(x)
    # build a dictionary with key as the cycle number and value as the signal strength
    s_th = dict(zip(list(range(1, cur_cyc + 1)), val))
    a = sum([s_th[i] * i for i in [20, 60, 100, 140, 180, 220]])
    print(a)


def part2(l):
    crt = ''
    x = 1
    buffer = []
    cur_cyc = 0
    for _ in l:
        s = _.split()
        # when the iteration reach 40, reset it to 0
        if cur_cyc == 40:
            cur_cyc = 0
        if s[0] == 'noop' or s[0] == 'addx':
            # the pixel is drawn on the sprite
            spr = list(range(x - 1, x + 2))
            if cur_cyc in spr:
                crt += '#'
            else:
                crt += '.'
            cur_cyc += 1
            if buffer:
                x += buffer.pop(0)
        # when the iteration reach 40, reset it to 0
        if cur_cyc == 40:
            cur_cyc = 0
        if s[0] == 'addx':
            spr = list(range(x - 1, x + 2))
            if cur_cyc in spr:
                crt += '#'
            else:
                crt += '.'
            cur_cyc += 1
            buffer.append(int(s[1]))
            if buffer:
                x += buffer.pop(0)
    for i in range(0, 240, 40):
        print(crt[i:i + 40])


def main():
    with open('day10.txt') as f:
        l = f.readlines()
        part1(l)
        part2(l)


if __name__ == '__main__':
    main()
