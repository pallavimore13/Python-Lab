def str_to_int(text):
    result = 0
    for char in text:
        digit = ord(char) - ord('0')
        result = result * 10 + digit
    return result

def decimal_sub(num1, num2):
    max_len = max(len(num1), len(num2))
    num1 = num1.zfill(max_len)
    num2 = num2.zfill(max_len)
    
    num1 = str_to_int(num1)
    num2 = str_to_int(num2)
    
    if num1 < num2:
        num1, num2 = num2, num1
        negative = True
    else:
        negative = False
    
    result = []
    borrow = 0
    
    # Loop over each digit from right to left
    for i in range(max_len):
        digit1 = num1 % 10
        digit2 = num2 % 10
        
        if digit1 < digit2 + borrow:
            digit1 += 10
            result_digit = digit1 - digit2 - borrow
            borrow = 1
        else:
            result_digit = digit1 - digit2 - borrow
            borrow = 0
        
        result.append(chr(result_digit + ord('0')))
        num1 //= 10
        num2 //= 10
    
    # Reverse the result and strip leading zeros
    result_str = ''.join(result[::-1]).lstrip('0')
    
    if negative:
        result_str = '-' + result_str
    
    # Handle case where result is zero
    if not result_str:
        result_str = '0'
    
    return result_str

print(decimal_sub("12", "10"))  # Output should be "2"
print(decimal_sub("10", "12"))  # Output should be "-2"
