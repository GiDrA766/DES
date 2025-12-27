def parity_drop(key):
    assert len(key)==64
    parity_drop_table = [
    56, 48, 40, 32, 24, 16, 8,
    0, 57, 49, 41, 33, 25, 17,
    9, 1, 58, 50, 42, 34, 26,
    18, 10, 2, 59, 51, 43, 35,
    62, 54, 46, 38, 30, 22, 14,
    6, 61, 53, 45, 37, 29, 21,
    13, 5, 60, 52, 44, 36, 28,
    20, 12, 4, 27, 19, 11, 3
    ]
    return [key[parity_drop_table[i]] for i in range(56)]

def shift_left(key, shift):
    return [key[(i + shift) % len(key)] for i in range(len(key))]

def compression(key):
    compression_table = [
    13, 16, 10, 23, 0, 4,
    2, 27, 14, 5, 20, 9,
    22, 18, 11, 3, 25, 7,
    15, 6, 26, 19, 12, 1,
    40, 51, 30, 36, 46, 54,
    29, 39, 50, 44, 32, 47,
    43, 48, 38, 55, 33, 52,
    45, 41, 49, 35, 28, 31
    ]
    return [key[compression_table[i]] for i in range(48)]

def key_generator(hex_key):
    binary_string = bin(int(hex_key, 16))[2:].zfill(64)
    key_with_parities = [int(bit) for bit in binary_string]
    shift_table = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]
    round_keys = []
    key_56_bit = parity_drop(key_with_parities)
    left_key = key_56_bit[:28]
    right_key = key_56_bit[28:]
    for i in range(16):
        left_key = shift_left(left_key, shift_table[i])
        right_key = shift_left(right_key, shift_table[i])
        preround_key = left_key + right_key
        key_48_bit = compression(preround_key)
        key_48_bit_as_binary = int("".join(map(str, key_48_bit)), 2)
        round_keys.append(bin(key_48_bit_as_binary)[2:].zfill(48))
    return round_keys
