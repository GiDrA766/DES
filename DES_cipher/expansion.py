def expand(block: str) -> str:
    blocks = []
    for i in range(0, len(block), 4):
        if i  == 0:
            blocks.append(block[-1]+block[i:i+5])
        elif i == 28:
            blocks.append(block[i-1:]+block[0])
            break
        else:
            blocks.append(block[i-1:i+5])
    return ''.join(blocks)

