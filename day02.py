# find the total score according to the strategy guide
def prior(a, b):
    match a:
        case 'X':
            match b:
                case 'X': return 3
                case 'Y': return 6
                case 'Z': return 0
        case 'Y':
            match b:
                case 'X': return 0
                case 'Y': return 3
                case 'Z': return 6
        case 'Z':
            match b:
                case 'X': return 6
                case 'Y': return 0
                case 'Z': return 3

def sign_score(a):
    match a:
        case 'X':
            return 1
        case 'Y':
            return 2
        case 'Z':
            return 3

def rprior(a, b):
    match a:
        case 'A':
            match b:
                case 3: return 'X'
                case 6: return 'Y'
                case 0: return 'Z'
        case 'B':
            match b:
                case 0: return 'X'
                case 3: return 'Y'
                case 6: return 'Z'
        case 'C':
            match b:
                case 6: return 'X'
                case 0: return 'Y'
                case 3: return 'Z'

def task1(l):
    dic = {'A': 'X', 'B': 'Y', 'C': 'Z'}
    tol_score = 0
    for _ in l:
        # opp is opponent`s choice, me is my choice
        opp = _[0]
        me = _[2]
        # obtain my score
        s1 = sign_score(me)
        # obtain a pair (opp, me) score
        s2 = prior(dic[opp], me)
        tol_score += s1 + s2
    print(tol_score)

def task2(l):
    dic1 = {'X':0, 'Y':3, 'Z':6}
    tol = 0
    for _ in l:
        opp = _[0]
        me = _[2]
        # given opponent`s choice and score, find my choice
        s = rprior(opp, dic1[me])
        # calculate my score
        s1 = sign_score(s)
        tol += s1 + dic1[me]
    print(tol)

def main():
    with open('day02.txt', 'r') as f:
        l = f.readlines()
        ### task 1
        task1(l)
        ### task 2
        task2(l)

if __name__ == '__main__':
    main()