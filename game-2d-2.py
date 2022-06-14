from math import ceil
from const import FIELD_SIZE, D, PLAYER_N
from game import TACTIC_LIST, game_process
from random import randint, choice
from copy import deepcopy
from graph import get_scatter


field = [[False]*FIELD_SIZE for _ in range(FIELD_SIZE)]
a = []
new_a = []


def get_distance(a1, a2):
    return (a1[0]-a2[0])**2 + (a1[1]-a2[1])**2


def get_pair(s, e):
    if s==e: return []
    if e-s==1:
        if get_distance(a[s], a[e]) <= D: return [[a[s], a[e]]]
        else: return []

    m = (s+e)//2
    hubo = get_pair(s,m-1) + get_pair(m+1,e)

    hubo2 = []
    for i in range(s, e+1):
        if (a[i][0]-a[m][0])**2 <= D: hubo2.append(a[i])
    
    hubo2.sort(key=lambda x:x[1])
    l = len(hubo2)
    for i in range(l-1):
        for j in range(i+1, l):
            if (hubo2[i][1]-hubo2[j][1])**2 <= D:
                if get_distance(hubo2[i], hubo2[j]) <= D: hubo.append([hubo2[i], hubo2[j]])
            else: break
    return hubo


def get_baby(ai, n):
    field[ai[0][0]][ai[0][1]] = field[ai[1][0]][ai[1][1]] = False
    midx = (ai[0][0]+ai[1][0])//2
    midy = (ai[0][1]+ai[1][1])//2
    for _ in range(n):
        x = y = -1
        r = 5
        k = 0
        while x==-1 or field[x][y]:
            x = randint(midx-r, midx+r)
            if x<0: x=0
            elif x>=FIELD_SIZE: x=FIELD_SIZE-1
            y = randint(midy-r, midy+r)
            if y<0: y=0
            elif y>=FIELD_SIZE: y=FIELD_SIZE-1
            k += 1
            if k > r**2:
                r += 2
                k = 0
        field[x][y] = True
        new_a.append([x, y, choice([ai[0][2], ai[0][3]]), choice([ai[1][2], ai[1][3]]), len(new_a), choice([True, False])])


if __name__ == "__main__":
    t1 = 'Downing'
    t2 = 'Grudger'

    # init
    a.append([19, 19, t1, t1, 0, True])
    a.append([21, 21, t1, t1, 1, False])
    a.append([19, 41, t1, t2, 2, True])
    a.append([21, 39, t1, t2, 3, False])
    a.append([39, 21, t1, t2, 4, True])
    a.append([19, 41, t1, t2, 5, False])
    a.append([39, 39, t2, t2, 6, True])
    a.append([41, 41, t2, t2, 7, False])
    for i in a: field[i[0]][i[1]] = True
    
    # iterate
    for _ in range(4):
        s = [[0, i] for i in range(len(a))]
        h = get_pair(0, len(a)-1)
        p = []
        for i in h:
            if i not in p: 
                p.append(i)
                f = lambda x: TACTIC_LIST[x[2] if x[2]==x[3] else t1]
                x, y = game_process(f(i[0]), f(i[1]), randint(10, 30))
                s[i[0][4]][0] += x
                s[i[1][4]][0] += y
        
        s2 = deepcopy(s)
        s.sort()
        l = len(s)
        n = max(round((70/l)**0.5), 2)

        sums = []
        for i in range(l):
            for j in range(i+1, l):
                sums.append(s[i][0]+s[j][0])
        sums.sort()
        #print(sums)
        #print(s2)
        ls = len(sums)

        for i in p:
            if i[0][5]^i[1][5]: 
                score = s2[i[0][4]][0] + s2[i[1][4]][0]
                if score < sums[ls//3]: get_baby(i, n-1)
                elif score <= sums[ls//3*2]: get_baby(i, n)
                else: get_baby(i, n+1)
        
        a = deepcopy(new_a)
        new_a.clear()
        
        t1_n = 0
        t2_n = 0
        t3_n = 0
        for i in a:
            if i[2] == t1 and i[3] == t1: t1_n += 1
            elif i[2] == t2 and i[3] == t2: t2_n += 1
            else: t3_n += 1

        print(t1_n, t3_n, t2_n)

        #get_scatter(a)