from .constants import  S

def splitting(section):
    return [section[i:i+6] for i in range(0, len(section), 6)]

def wither(six_blocks):
    out = []
    for i, block in enumerate(six_blocks):
        out.append(s_box(block, i))
    return out


def s_box(block, index):
    out = []
    row = ''+ block[0] + block[-1]
    col = ''.join(block[1:5])
    row = int(row, base=2)
    col = int(col, base=2)
    num = S[index][row][col]
    result = str(bin(num))[2:].zfill(4)
    return result

def substitute(T1):
    return wither(splitting(T1))