def base(text, text_base, output_base):
    # Function to convert a number to a Roman numeral
    def to_roman(num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num

   
    num = int(text, text_base)

   
    if output_base == 2:
        return bin(num)[2:]  
    elif output_base == 8:
        return oct(num)[2:]  
    elif output_base == 10:
        return str(num)  
    elif output_base == 16:
        return hex(num)[2:].upper()
    elif output_base == "r":
        return to_roman(num)  
    else:
        raise ValueError("Unsupported output base")

# Test cases
print(base("11", 2, 2))  
print(base("11", 2, 3))  
print(base("17", 8, "r"))