from .function import permute
from .constants import *
def cipher(text):
    text = permute(text, initial_perm_map)
    Left, Right  = text[:33], text[33:]
    for i in range(16):
        Left, Right = permute(Left, Right)
        if i != 0:
            Left, Right = Right, Left
    text = Left + Right
    return permute(text, inverseInitial_perm_map)




