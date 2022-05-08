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


TACTIC_LIST = {
    'Tft': Tft(), 
    'Tftt': Tftt(), 
    'All-C' : AlwaysCoop(), 
    'All-D' : AlwaysDefect(), 
    'Random' : Random(), 
    'Downing': Downing(),
    'Downing2': Downing2(), 
    'Grudger': Grudger(), 
    'Joss': Joss(), 
    'Tester': Tester()
}

