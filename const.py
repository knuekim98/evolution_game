from enum import Enum

GAME_COUNT = 200

class log(Enum):
    SET = 0
    GAME = 1
    RESULT = 2

class result(Enum):
    COOP = 3
    DEFECT = 5
    DEFECTED = 0
    DRAW = 1