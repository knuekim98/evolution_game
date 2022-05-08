from const import FIELD_SIZE, D
from game import game, TACTIC_LIST


field = [[0] for _ in range(FIELD_SIZE)]*FIELD_SIZE
a = []


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


if __name__ == "__main__":
    # init
    a.append([250, 250, 'Tft'])
    a.append([250, 251, 'All-D'])
    a.append([253, 250, 'Downing'])
    a.append([255, 251, 'Random'])

    x = get_pair(0, len(a)-1)
    p = []
    for i in x:
        if i not in p: p.append(i)

    print(p)