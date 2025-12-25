def xor(a:list, b:list) -> list:
    return [str(int(a[i])^int(b[i])) for i in range(len(a))]