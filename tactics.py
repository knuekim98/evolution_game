from const import result
import random

class Tft:
    def __init__(self) -> None:
        self.score = 0
        self.last_reaction = True

    def run(self):
        return self.last_reaction

    def next(self, r):
        self.score += r.value
        if r == result.COOP or r == result.DEFECT:
            self.last_reaction = True
        else:
            self.last_reaction = False
    
    def end(self):
        self.last_reaction = True
        return self.score


class Ttft:
    def __init__(self) -> None:
        self.score = 0
        self.last_reaction = True
        self.last_last_reaction = True

    def run(self):
        return self.last_reaction | self.last_last_reaction

    def next(self, r):
        self.score += r.value
        self.last_last_reaction = self.last_reaction
        if r == result.COOP or r == result.DEFECT:
            self.last_reaction = True
        else:
            self.last_reaction = False
    
    def end(self):
        self.last_reaction = True
        self.last_last_reaction = True
        return self.score


class AlwaysCoop:
    def __init__(self) -> None:
        self.score = 0
    
    def run(self):
        return True
    
    def next(self, r):
        self.score += r.value

    def end(self):
        return self.score


class AlwaysDefect:
    def __init__(self) -> None:
        self.score = 0
    
    def run(self):
        return False
    
    def next(self, r):
        self.score += r.value

    def end(self):
        return self.score

class Random:
    def __init__(self) -> None:
        self.score = 0
    
    def run(self):
        return random.choice([True, False])
    
    def next(self, r):
        self.score += r.value

    def end(self):
        return self.score


class Downing:
    def __init__(self) -> None:
        self.score = 0
        self.game_count = 0
        self.coop_count = 0
    
    def run(self):
        if self.game_count == 0:
            return True
        if self.coop_count / self.game_count > 0.5:
            return True
        return False
    
    def next(self, r):
        self.score += r.value
        self.game_count += 1
        if r == result.COOP or r == result.DEFECT:
            self.coop_count += 1

    def end(self):
        self.game_count = self.coop_count = 0
        return self.score
        