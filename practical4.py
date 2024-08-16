def change_case(text,style):
	

	def convert_to_capitalcase(t):
		result = ""
		
		for i in t:
			ascii = ord(i)
			
			if 97 <= ascii <= 122:
				result += chr(ascii-32)
			else:
				result += i
			
			
		return result
		
	def convert_to_smallcase(t):
		result = ""
		for i in t:
			ascii = ord(i)
			
			if 65 <= ascii <= 90:
				result += chr(ascii+32)
			else:
				result += i
			
		return result
		
	def convert_to_reversecase(t):
		result = ""
		for i in t:
			ascii = ord(i)
			
			if 97 <= ascii <= 122:
				result += chr(ascii-32)
				
			elif 65 <= ascii <= 90:
				result += chr(ascii+32)
			else:
				result += i
		return result
		
	
	def convert_to_zigzagcase(t):
		if not t:  # Handle empty input
		    return ""
		
		result = t[0]  
		for index in range(1, len(t)):
		    ascii_val = ord(t[index])
		    if index % 2 == 1:  
		        if 97 <= ascii_val <= 122:  
		            result += chr(ascii_val - 32)
		        else:
		            result += t[index]
		    else:  # Even index
		        if 65 <= ascii_val <= 90:  
		            result += chr(ascii_val + 32)
		        else:
		            result += t[index]
		return result

		
		
	if style == "c" or style == "C":
		return convert_to_capitalcase(text)
		
		
	elif style == 's' or style == 'S':
		return convert_to_smallcase(text)
		
	elif style == 'r' or style == 'R':
		return convert_to_reversecase(text)
		
	elif style == 'z' or style == 'Z':
		return convert_to_zigzagcase(text)
	else:
		print("Invalid style")
		
	
			
			
		


def main():
	#text = "SGGSie&t"
	#style = ""
	
	print(change_case("SGGsie&t",'Z'))
	
if __name__ == "__main__":
	main()

	

	
