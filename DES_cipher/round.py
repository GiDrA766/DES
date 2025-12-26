import copy
from .xor import xor

from .function import f

def des_round(Left:str, Right:str, Key:str) -> str:
    copy_of_right = copy.deepcopy(Right)
    Right = f(Right, Key)
    Left = xor(Left, Right)
    return Left, Right
