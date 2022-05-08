from enum import Enum

GAME_COUNT = 200
FIELD_SIZE = 100
D = 50

class log(Enum):
    SET = 0
    GAME = 1
    RESULT = 2

class result(Enum):
    COOP = 1
    DEFECT = 3
    DEFECTED = -3
    DRAW = -1