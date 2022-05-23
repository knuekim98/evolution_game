from const import result
from tactics import Tft, Tftt, AlwaysCoop, AlwaysDefect, Random, Downing, Downing2, Grudger, Joss, Tester

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


def game_process(p1, p2, n):
    r1 = r2 = 0
    p1.__init__()
    p2.__init__()
    for _ in range(n):
        r1, r2 = game(p1.run(), p2.run())
        p1.next(r1)
        p2.next(r2)

    return p1.end(), p2.end()


TACTIC_LIST = {
    'Tft': Tft(), 
    'Tftt': Tftt(), 
    #'All-C' : AlwaysCoop(), 
    #'All-D' : AlwaysDefect(), 
    'Random' : Random(), 
    'Downing': Downing(),
    #'Downing2': Downing2(), 
    'Grudger': Grudger(), 
    'Joss': Joss(), 
    #'Tester': Tester()
}

