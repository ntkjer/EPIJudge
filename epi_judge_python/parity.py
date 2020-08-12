from test_framework import generic_test


def parity(x: int) -> int:
    """
    Tn = O(k)
    
    Explanation:
    x &= x - 1 is equal to x with the lowest set bit erased.

    If  1.  x       = 00101100
        2.  x - 1   = 00101011
        3. [1 & 2]  = 00101000
    
    This means that we only go through the loop for the amount of 1 bits,k, in n-length bit sequence.
    """
    result = 0
    while x:
        result ^= 1
        x &= x - 1
    return result


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
