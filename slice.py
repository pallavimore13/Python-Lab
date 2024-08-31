def slice(obj, slicing_parameter):

    start, end, step = slicing_parameter

    if start is None:
        start = 0
    if end is None:
        end = len(obj)
    if step is None:
        step = 1

    result = []
    

    i = start
    while (i < end and step > 0) or (i > end and step < 0):
        result.append(obj[i])
        i += step

    return result

# Example usage
my_list = [1, 2, 3, 4, 5]
print(slice(my_list, (1, 4, 1)))  # Output: [2, 3, 4]

my_string = "Hello, World!"
print("".join(slice(my_string, (7, 12, 1))))  # Output: World

my_tuple = (10, 20, 30, 40, 50)
print(slice(my_tuple, (1, 4, 2)))  # Output: [20, 40]