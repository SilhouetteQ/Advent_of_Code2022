# find the level of monkey business
import re


class monkey:
    def __init__(self, id):
        # ins represents the starting item list
        self.ins = []
        # upins represents the item list after calculation
        self.upins = []
        # identify each monkey
        self.id = id
        # operation on the item
        self.opp = []
        self.test = 0
        # tm: the monkey is thrown if true
        self.tm = ''
        # fm: the monkey is thrown if false
        self.fm = ''
        # monkey business
        self.bus = 0

    def oper(self, div, id_m, test_set):
        opp = self.opp
        # update the new list with calculated item
        if opp[0] == '+':
            if opp[1] == 'old':
                for i in self.ins:
                    self.upins.append(int((i + i) / div))
            else:
                val = int(opp[1])
                for i in self.ins:
                    self.upins.append(int((i + val) / div))
        if opp[0] == '*':
            if opp[1] == 'old':
                for i in self.ins:
                    self.upins.append(int((i * i) / div))
            else:
                val = int(opp[1])
                for i in self.ins:
                    self.upins.append(int((i * val) / div))
        # empty the starting item list
        self.ins.clear()
        # redistribute the after calculation item list
        for u in self.upins:
            self.bus += 1
            # here is a trick using Chinese remainder theorem to obtain unique remainder for the large number.
            # refer to https://en.wikipedia.org/wiki/Chinese_remainder_theorem
            if test_set is not None:
                u = u % test_set
            if u % self.test == 0:
                id_m[self.tm].ins.append(u)
            else:
                id_m[self.fm].ins.append(u)
        # empty the after calculation item list
        self.upins.clear()

def parse(l):
    m_obj = []
    for _ in l:
        s = _.split()
        if len(s) > 0:
            if s[0] == 'Monkey':
                # create monkey object, string type
                m = monkey(s[1][:-1])
                m_obj.append(m)
            if s[0] == 'Starting':
                l_str = re.findall('\d+', _)
                m.ins = [int(i) for i in l_str]
            if s[0] == 'Operation:':
                m.opp = s[4:]
            if s[0] == 'Test:':
                m.test = int(s[3])
            if s[0] == 'If':
                if s[1] == 'true:':
                    m.tm = s[5]
                elif s[1] == 'false:':
                    m.fm = s[5]
    return m_obj


def part1(l):
    # each monkey is constructed as an object and their information are stored
    # keep all monkey objects in a list
    m_obj = parse(l)
    ids = [i.id for i in m_obj]
    id_m = dict(zip(ids, m_obj))
    for _ in range(20):
        for m in m_obj:
            m.oper(3, id_m, None)
    # extract the level of monkey business of each monkey
    bus = [int(m.bus) for m in m_obj]
    bus.sort()
    print(bus[-1] * bus[-2])


def part2(l):
    m_obj = parse(l)
    test_set = 1
    # test_set is a common multiple of all divisibility checks, which represents the greatest common divisor
    # refer to https://en.wikipedia.org/wiki/Greatest_common_divisor
    for j in m_obj:
        test_set = test_set * int(j.test)
    ids = [i.id for i in m_obj]
    id_m = dict(zip(ids, m_obj))
    for _ in range(10000):
        for m in m_obj:
            m.oper(1, id_m, test_set)
    bus = [int(m.bus) for m in m_obj]
    bus.sort()
    print(bus[-1] * bus[-2])


def main():
    with open('day11.txt') as f:
        l = f.readlines()
        part1(l)
        part2(l)


if __name__ == '__main__':
    main()
