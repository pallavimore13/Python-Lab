roman_dict = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I"
}

dict_keys = list(roman_dict.keys())
dict_values = list(roman_dict.values())

def rom(text, text_base):
    k = int(text, text_base)
    lst = list(str(k))
    lst1 = [int(i) for i in lst]
    y = []
    for i in range(len(lst1)):
        ele = lst1[i] * pow(10, len(lst1) - i - 1)
        y.append(ele)
   
    print("List of significant digits:", y)  # For debugging
   
    roman = []
    for element in y:
        if element in roman_dict:
            roman.append(roman_dict[element])
        else:
            # Handle the "Null" case by breaking down the value
            while element > 0:
                for value in sorted(dict_keys, reverse=True):
                    if element >= value:
                        roman.append(roman_dict[value])
                        element -= value
                        break

    print("Roman numeral list:", roman)  # For debugging
    print(''.join(roman))

# Example usage
rom("1998", 10)  # Output should be "MCMXCVI"