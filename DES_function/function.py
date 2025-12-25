from expansion import expand
from xor import xor
from s_boxing import substitute
from constants import P

def permute(text):
    result = ''
    for i in P:
        result += text[i]


def f(right: str, Key: str):
    expanded = expand(right)
    xored = xor(expanded, Key)
    fit = substitute(xored)
    return permute(fit)



