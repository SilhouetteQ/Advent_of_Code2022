def main():
    ### part 1
    ### cal_list store the calorie sum of each Elve
    cal_list = []
    with open('day01.txt', 'r') as f:
        l = f.readlines()
        cal_sum = 0
        for _ in l:
            ### this indicates the empty line
            if _ == "\n":
                cal_list.append(cal_sum)
                cal_sum = 0
            ### calculate the sum
            else:
                cal_sum += int(_.strip())
        cal_list.append(cal_sum)
    ### find the maximum one
    print(max(cal_list))

    ### part 2
    ### use sorted() to sort the list and sum up the top 3
    print(sum(sorted(cal_list, reverse=True)[0:3]))

if __name__ == '__main__':
    main()