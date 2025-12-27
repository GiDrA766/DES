
from DES_cipher import  cipher, print_hex


if __name__ == '__main__':
    plaintext = "123456ABCD132536"
    Key = "AABB09182736CCDD"
    bin_str = bin(int(plaintext, 16))[2:].zfill(64)
    cipher_text = cipher(bin_str, Key)
    print_hex(cipher_text)


