#pattern1
def print_pattern(array):
    n = len(array)
    
    # Printing the main pattern
    for i in range(2 * n + 1):
        for j in range(2*n-1): 
            print(" ", end="")
            
        for j in range(2 * n + 1):
            if (i + j == n or j - i == n or i + j == 3 * n or i - j == n):
                print("*", end="")
            elif i == n and j == n:
                print(n, end="")
            else:
                print(" ", end="")
        print()
    
   
    for _ in range(len(array)):
          print(' ' * (n + 1) + '*' * ((2 * (n + 1)+1)))

#pattern2
def pattern2(array):
    n = len(array)
    
    for i in range(2 * n + 1):
        for j in range(2 * n + 1):
            if (i + j == n or j - i == n):
                print("+", end="")
            elif(i - j == n or i + j == 3 * n):
                print("+", end="")
            elif(i == 2 * n and j == n):
                print("-", end="")
            else:
                print(" ", end="")
        print()


#pattern3
def pattern3(array):
    n = len(array)
    
    for i in range(2 * n + 1):
        for j in range(2 * n + 1):
            if (i + j == n or j - i == n):
                print("+", end="")
            elif(i - j == n or i + j == 3 * n):
                print("-", end="")
            elif(i == n and j == n):
                print(n, end="")
            else:
                print(" ", end="")
        print()



#modulo
def modulo(numerator, denominator):
    if denominator == 0:
        print("Denominator cannot be zero")
    
    return numerator - (numerator // denominator) * denominator

numerator=int(input("Numerator:"))
denominator=int(input("Denominator:"))


print(modulo(numerator, denominator))


#count function
def count(string, substring, flag):
    count = 0
    start = 0
    length = len(substring)

    while start < len(string):
        
        pos = string.find(substring, start)
        
        if pos == -1:
            break
        
        count += 1
        
        if flag:
            start = pos + 1
        else:
            start = pos + length

    return count

print( count("sgggs", "gg", False))  



def main():
	size = int(input("Enter the size of array"))
	array = [0]*size
	
	print_pattern(array)
	
	pattern2(array)
	
	pattern3(array)
	
	
	numerator=int(input("Numerator:"))

	denominator=int(input("Denominator:"))

    

	print(modulo(numerator, denominator))

    

	print( count("sgggs", "gg", False))	
	

if __name__ == "__main__":

    main()
	
	































