# Find the most pressure released with specified valve layout
import re


class State:
    def __init__(self, valve, open_valve: list = [], pressure: int = 0, total_pressure: int = 0):
        self.valve = valve
        self.pressure = pressure
        self.total_pressure = total_pressure
        self.open_valve = open_valve.copy() if open_valve else []

    def copy(self):
        return State(self.valve, self.open_valve, self.pressure, self.total_pressure)


def main():
    with open('day16.txt') as f:
        l = f.readlines()
        target = {}
        rate = {}
        for _ in l:
            s = re.findall(r'[A-Z]+', _)
            target[s[1]] = s[2:]
            s1 = re.findall(r'\d+', _)
            rate[s[1]] = int(s1[0])
        # dist is a 2-dim array that store the distance(time) between two valves
        # valve_order is a dict with valve name as key and the index of the valve in dist as value
        dist, valve_order = build_graph(target, rate)
        flowing_valve = []
        for i in rate:
            # only consider valves having flow rate larger than 0
            if rate[i] > 0:
                flowing_valve.append(i)
        # initialize start state with AA as the current valve
        m = State('AA')
        a = elap(dist, valve_order, rate, flowing_valve, [m], 30)
        print(a)


def find_pair_dist(p1, p2, dist, valve_order):
    vp1 = valve_order[p1]
    vp2 = valve_order[p2]
    return dist[vp1][vp2]


def elap(dist, valve_order, rate, flowing_valve, state_list, t):
    # state_list stores State objects
    cur = state_list[-1]
    options = []
    # all valves are open
    if len(cur.open_valve) == len(flowing_valve):
        total_pressure = cur.total_pressure + cur.pressure * t
        return total_pressure

    for i in flowing_valve:
        if i != cur.valve and i not in cur.open_valve:
            # find the time cost from one valve to other valve,
            # the additional time is the time cost for opening the valve
            t_cost = find_pair_dist(i, cur.valve, dist, valve_order) + 1
            t_remain = t - t_cost
            # if there is not enough time to open the next valve,
            # stop adding new valve and calculate the possible result
            if t_remain <= 2:
                options.append(cur.total_pressure + cur.pressure * t)
            else:
                # create a new state, representing that a valve is open
                # update its current valve, open_valve, pressure and total_pressure
                next_state = cur.copy()
                next_state.valve = i
                next_state.open_valve.append(i)
                next_state.pressure += rate[i]
                next_state.total_pressure += cur.pressure * t_cost
                options.append(elap(dist, valve_order, rate, flowing_valve, state_list + [next_state], t_remain))
    # choose the largest value among all options
    return max(options)


def build_graph(target, rate):
    all_valve = [i for i in rate]
    n = len(all_valve)
    # a random infinite large number
    inf = 999
    # dist is an n-by-n symetric distance matrrix
    # initial valve pairs have distance of infinite large, i.e., inf
    dist = [[inf for i in range(n)] for j in range(n)]
    for i in range(n):
        # diagonal value equal 0
        dist[i][i] = 0
        t = all_valve[i]
        t_bind = target[t]
        # any valve pair having direct contact will have a distance of 1
        for j in t_bind:
            k = all_valve.index(j)
            dist[i][k] = 1

    # use Floyd Warshall Algorithm to find the shortest distances between every pair of valves
    # refer to https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/
    # find the shortest distance between any valve pair
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    valve_order = dict(zip(all_valve, list(range(n))))
    return dist, valve_order


if __name__ == '__main__':
    main()
