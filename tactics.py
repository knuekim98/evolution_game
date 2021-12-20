from const import result
import random


C, D = True, False

def opponent(r):
    if r == result.COOP or r == result.DEFECT:
        return True
    return False


# tit for tat
class Tft:
    def __init__(self) -> None:
        self.score = 0
        self.last_reaction = C

    def run(self):
        return self.last_reaction

    def next(self, r):
        self.score += r.value
        self.last_reaction = opponent(r)
    
    def end(self):
        self.last_reaction = C
        return self.score


# tit for two tat
class Tftt:
    def __init__(self) -> None:
        self.score = 0
        self.last_reaction = C
        self.last_last_reaction = C

    def run(self):
        return self.last_reaction | self.last_last_reaction

    def next(self, r):
        self.score += r.value
        self.last_last_reaction = self.last_reaction
        self.last_reaction = opponent(r)
    
    def end(self):
        self.last_reaction = C
        self.last_last_reaction = C
        return self.score


# always coop
class AlwaysCoop:
    def __init__(self) -> None:
        self.score = 0
    
    def run(self):
        return C
    
    def next(self, r):
        self.score += r.value

    def end(self):
        return self.score


# always defect
class AlwaysDefect:
    def __init__(self) -> None:
        self.score = 0
    
    def run(self):
        return D
    
    def next(self, r):
        self.score += r.value

    def end(self):
        return self.score


# perfect random(50%)
class Random:
    def __init__(self) -> None:
        self.score = 0
    
    def run(self):
        return random.choice([C, D])
    
    def next(self, r):
        self.score += r.value

    def end(self):
        return self.score


# first defect, opponent coop rate - coop(>50%) / defect(<=50%)
class Downing:
    def __init__(self) -> None:
        self.score = 0
        self.game_count = 0
        self.coop_count = 0
    
    def run(self):
        if self.game_count == 0:
            return D
        if self.coop_count / self.game_count > 0.5:
            return C
        return D
    
    def next(self, r):
        self.score += r.value
        self.game_count += 1
        if opponent(r):
            self.coop_count += 1

    def end(self):
        self.game_count = self.coop_count = 0
        return self.score


# first coop, opponent coop rate - coop(>=50%) / defect(<50%)
class Downing2:
    def __init__(self) -> None:
        self.score = 0
        self.game_count = 0
        self.coop_count = 0
    
    def run(self):
        if self.game_count == 0:
            return C
        if self.coop_count / self.game_count >= 0.5:
            return C
        return D
    
    def next(self, r):
        self.score += r.value
        self.game_count += 1
        if opponent(r):
            self.coop_count += 1

    def end(self):
        self.game_count = self.coop_count = 0
        return self.score


# coop, always defect once defected
class Grudger:
    def __init__(self) -> None:
        self.score = 0
        self.defected = False
    
    def run(self):
        if self.defected:
            return D
        return C
    
    def next(self, r):
        self.score += r.value
        if not opponent(r):
            self.defected = True

    def end(self):
        return self.score


# tft but defect by 10% rate
class Joss:
    def __init__(self) -> None:
        self.score = 0
        self.last_reaction = C

    def run(self):
        if random.randint(1, 10) == 1:
            return D
        return self.last_reaction

    def next(self, r):
        self.score += r.value
        self.last_reaction = opponent(r)
    
    def end(self):
        self.last_reaction = C
        return self.score


# wip
class Tester:
    def __init__(self) -> None:
        self.score = 0
        self.decision = True
        self.test_tft = False
        self.game_count = 0

    def run(self):
        if self.game_count == 0:
            return D
        return self.decision

    def next(self, r):
        self.score += r.value
        if self.game_count == 1 & (not opponent(r)):
            self.test_tft = True
        elif self.test_tft:
            self.decision = opponent(r)
        elif self.game_count <= 2:
            self.decision = True
        else:
            self.decision = not self.decision

        self.game_count += 1
    
    def end(self):
        self.decision = True
        self.test_tft = False
        self.game_count = 0
        return self.score
