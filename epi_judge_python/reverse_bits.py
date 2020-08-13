from test_framework import generic_test

import swap_bits


def generate_reversed_table() -> list:
    result = []
    for i in range(2**16 -1):
        tmp = i
        for j in range(8):
            tmp = swap_bits.swap_bits(tmp, j, 15-j)
        result.append(tmp)
    return result



def reverse_bits(x: int) -> int:
    """
    We divide x, a 64-bit number at most, into four 16-bit partitions.
    x = ABCD which the rev(x) = rev(D)rev(C)rev(B)rev(A)

    """
    mask_size = 16 # 64 bits divided by 4 partitions
    bit_mask = 0xFFFF # preserves the bits 
    reversed = _REVERSED_VALUES
    A = x & bit_mask 
    B = x >> mask_size & bit_mask 
    C = x >> (2 * mask_size) & bit_mask
    D = x >> (3 * mask_size) & bit_mask
    #print("testing x\n")
    #print(bin(x))
    #print(bin(A))
    #print(bin(B))
    #print(bin(C))
    #print(bin(D))
    return (reversed[A] << (3 * mask_size) |
            reversed[B] << (2 * mask_size) |
            reversed[C] << (mask_size) |
            reversed[D])


def reverse_bits_brute_force(x : int) -> int:
    """
    needs padding for trailing bits 
    """
    i, j = 1, x.bit_length() + 1
    z = 64 - x.bit_length()+1
    while j > x.bit_length() / 2:
        if (x >> i) & 1 != (x >> j) & 1:
            bit_mask = (1 << i) | (1 << j)
            x ^= bit_mask
        i += 1
        j -= 1
    return x
    

if __name__ == '__main__':
    _REVERSED_VALUES = generate_reversed_table()
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                        reverse_bits))
