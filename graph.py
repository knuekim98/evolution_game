import matplotlib.pyplot as plt
from collections import defaultdict
COLOR = ('b', 'g', 'r', 'c', 'm', 'y', 'k')


def get_scatter(a):
    temp = defaultdict(list)
    for i in a: temp[i[2]].append([i[0], i[1]])

    k = 0
    for i in temp.keys():
        t = temp[i]
        plt.scatter(
            [t[j][0] for j in range(len(t))], 
            [t[j][1] for j in range(len(t))], 
            c=COLOR[k], s=1, label=i
        )
        k+=1

    plt.legend()
    plt.show()