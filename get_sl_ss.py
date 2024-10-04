def get_numeric_value(l, number):
    if isinstance(l, int):
        number.append(l)
    elif isinstance(l, (list, tuple, set)):
        for i in l:
            get_numeric_value(i, number)
    elif isinstance(l, dict):
        for key, value in l.items():
            get_numeric_value(key, number)
            get_numeric_value(value, number)

def get_unique_elements(number):
    res = []
    for i in number:
        if i not in res:
            res.append(i)
    return res

def sort_numbers(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def get_sl_ss(l):
    number = []
    get_numeric_value(l, number)
    
    number = get_unique_elements(number)
    
    if len(number) < 2:
        return "The list does not contain second smallest or largest element"
    
    sort_numbers(number)  

    second_smallest = number[1]
    second_largest = number[-2]
    
    return second_smallest, second_largest

l = [2, [8, 4], (6, 9), {2: 3, 9: 7}]
print(get_sl_ss(l))

