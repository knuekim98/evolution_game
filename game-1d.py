from const import GAME_COUNT
from game import game, TACTIC_LIST
from itertools import combinations

if __name__ == "__main__":
    t = TACTIC_LIST
    s = {i:0 for i in t.keys()}

    for i, j in combinations(t.keys(), r=2):
        print(f'game: {i} vs {j}')
        
        for x in range(GAME_COUNT):
            r1, r2 = game(t[i].run(), t[j].run())
            t[i].next(r1)
            t[j].next(r2)

        print(f'{s[i]}->{t[i].end()}, {s[j]}->{t[j].end()}')
        s[i] = t[i].end()
        s[j] = t[j].end()
    
    print("----------result----------")
    print(sorted(s.items(), key=lambda x:(-x[1])))
    