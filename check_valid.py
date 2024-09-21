def check_validity(text):
    if len(text) == 0:
        return "Valid"

    result = []
    brackets = {'{', '(', '<', '[', '}', ')', '>', ']'}
    pair = {'<': '>', '(': ')', '[': ']', '{': '}'}

    for symbol in text:
        if symbol in brackets:
            if symbol in pair: 
                result.append(symbol)
            else: 
                if len(result) == 0:
                    return "Invalid:There is no symbol to match"
                if symbol == pair[result[-1]]:  
                    result.pop()  
                else:
                    return "Invalid:No matching pair" 

   
    return "Valid" 
    if not result:
        return "Invalid:If symbol remains in list it means it not valid"
    
print(check_validity('{(<>)}')) 
print(check_validity('){}<>'))   
print(check_validity(''))        
print(check_validity('{[()]}'))   
  

