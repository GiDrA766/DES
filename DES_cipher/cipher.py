from .function import permute, f
from .constants import *
from .key_generator import key_generator
from .xor import  xor

def cipher(text, HexKey):
    Keys = key_generator(HexKey)
    text = permute(text, initial_perm_map)

    Left, Right  = text[:32], text[32:]
    for i in range(16):
        temp = f(Right, Keys[i])
        Left = xor(Left, temp)
        if i != 15 :
            Left, Right = Right, Left
    text = Left + Right
    return permute(text, inverseInitial_perm_map)




