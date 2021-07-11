from const import result, GAME_COUNT
from tactics import Tft, Ttft, AlwaysCoop, AlwaysDefect, Random, Downing

# True: coop, False: defect
def game(p1, p2):
    if p1 & p2: # COOP
        return result.COOP, result.COOP
    if p1: # DEFECTED / DEFECT
        return result.DEFECTED, result.DEFECT
    if p2: # DEFECT / DEFECTED
        return result.DEFECT, result.DEFECTED
    # DRAW
    return result.DRAW, result.DRAW


if __name__ == "__main__":
    t = [Tft(), Ttft(), AlwaysCoop(), AlwaysDefect(), Random(), Downing()]
    s = [0] * len(t)

    for i in range(len(t)):
        for j in range(i):
            print(f'game: {t[i].__class__.__name__} vs {t[j].__class__.__name__}')
            
            for x in range(GAME_COUNT):
                r1, r2 = game(t[i].run(), t[j].run())
                t[i].next(r1)
                t[j].next(r2)

            print(f'{s[i]}->{t[i].end()}, {s[j]}->{t[j].end()}')
            s[i] = t[i].end()
            s[j] = t[j].end()
    
    print("----------result----------")
    k = []
    for i in range(len(t)):
        k.append(t[i].__class__.__name__ + ":" + str(s[i]/len(t)))
    print(", ".join(k))