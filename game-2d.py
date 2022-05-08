from const import FIELD_SIZE, D
from game import TACTIC_LIST, game_process
from random import randint
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
    for _ in range(n):
        field[ai[0]][ai[1]] = False
        x = y = -1
        r = 5
        k = 0
        while x==-1 or field[x][y]:
            x = randint(ai[0]-r, ai[0]+r)
            if x<0: x=0
            elif x>=FIELD_SIZE: x=FIELD_SIZE-1
            y = randint(ai[1]-r, ai[1]+r)
            if y<0: y=0
            elif y>=FIELD_SIZE: y=FIELD_SIZE-1
            k += 1
            if k > r**2:
                r += 2
                k = 0
        field[x][y] = True
        new_a.append([x, y, ai[2], len(new_a)])


if __name__ == "__main__":
    # init
    a.append([20, 20, 'All-C', 0])
    a.append([40, 40, 'Downing', 1])
    a.append([20, 40, 'Joss', 2])
    a.append([40, 20, 'Random', 3])
    for i in a: field[i[0]][i[1]] = True
    
    # iterate
    for _ in range(5):
        s = [[0, i] for i in range(len(a))]
        h = get_pair(0, len(a)-1)
        p = []
        for i in h:
            if i not in p: 
                p.append(i)
                x, y = game_process(TACTIC_LIST[i[0][2]], TACTIC_LIST[i[1][2]], 30)
                s[i[0][3]][0] += x
                s[i[1][3]][0] += y
        
        s.sort()
        l = len(s)
        n = round((500/l)**0.5)
        for i in range(l):
            if s[i][0] < s[l//3][0]: get_baby(a[s[i][1]], n-1)
            elif s[i][0] < s[l//3*2][0]: get_baby(a[s[i][1]], n)
            else: get_baby(a[s[i][1]], n+1)
        
        a = deepcopy(new_a)
        new_a.clear()
        
        get_scatter(a)