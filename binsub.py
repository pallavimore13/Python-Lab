def binary_subtraction(a, b):
    # Convert integers to lists of bits (most significant bit first)
    a_bits = []
    b_bits = []
    while a > 0:
        a_bits.append(a % 2)
        a //= 2
    while b > 0:
        b_bits.append(b % 2)
        b //= 2

    # Make sure a_bits and b_bits have the same length
    max_len = max(len(a_bits), len(b_bits))
    a_bits = [0] * (max_len - len(a_bits)) + a_bits
    b_bits = [0] * (max_len - len(b_bits)) + b_bits

    # Perform binary subtraction
    result_bits = []
    borrow = 0
    for i in range(max_len - 1, -1, -1):
        bit_sum = a_bits[i] - b_bits[i] - borrow
        if bit_sum < 0:
            bit_sum += 2
            borrow = 1
        else:
            borrow = 0
        result_bits.append(bit_sum)

    # Convert result bits back to integer
    result = 0
    for bit in result_bits:
        result = (result << 1) | bit

    # Print result in binary and integer
    print(''.join(str(bit) for bit in result_bits[::-1]))
   

# Test the function
binary_subtraction(12, 7)

