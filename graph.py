import matplotlib.pyplot as plt
from collections import defaultdict
COLOR = ('b', 'g', 'r', 'c', 'm', 'y', 'k')
COLOR = {'Tft': 'b', 'Grudger': 'g', 'Tftt': 'c', 'Random': 'r', 'Joss': 'y', 'Downing': 'm'}


def get_scatter(a):
    temp = defaultdict(list)
    for i in a: temp[i[2]].append([i[0], i[1]])

    for i in temp.keys():
        t = temp[i]
        plt.scatter(
            [t[j][0] for j in range(len(t))], 
            [t[j][1] for j in range(len(t))], 
            c=COLOR[i], s=7, label=i
        )
        print(f'{i}:{len(t)} ', end='')

    #plt.legend()
    print()
    plt.show()