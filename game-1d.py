from const import GAME_COUNT
from game import game, TACTIC_LIST, game_process
from itertools import combinations

if __name__ == "__main__":
    t = TACTIC_LIST
    s = {i:0 for i in t.keys()}

    for i, j in combinations(t.keys(), r=2):
        x, y = game_process(t[i], t[j], GAME_COUNT)
        print(f'{i} vs {j}: +{x}, +{y}')
        s[i] += x
        s[j] += y
    
    print("----------result----------")
    print(sorted(s.items(), key=lambda x:(-x[1])))
    