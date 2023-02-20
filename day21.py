# find the number the monkey 'root' yell
def main():
    with open('day21.txt') as f:
        l = f.readlines()
        sc = {}
        sn = {}
        for _ in l:
            s = _.split()
            s1 = s[0].split(':')
            if s[1].isnumeric():
                # sn store monkey name as key and monkey number as value
                sn[s1[0]] = int(s[1])
            else:
                # sc store monkey name as key and other monkey names and operation as value
                sc[s1[0]] = s[1:]
        print(int(cal_root('root', sn, sc)))


def cal_root(name, sn, sc):
    # base case: monkey name corresponds to a number
    if name in sn:
        val = sn[name]
        return val
    if name in sc:
        val1 = cal_root(sc[name][0], sn, sc)
        val2 = cal_root(sc[name][2], sn, sc)
        match sc[name][1]:
            case "+":
                return val1 + val2
            case "-":
                return val1 - val2
            case "*":
                return val1 * val2
            case "/":
                return val1 / val2


if __name__ == '__main__':
    main()
