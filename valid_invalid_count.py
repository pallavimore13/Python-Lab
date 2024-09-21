def get_valid_invalid_text_count(text):
	valid_count = 0
	invalid_count = 0
	
	for i in text:
		if isinstance(i,str):
			valid_count += 1
		else:
			invalid_count += 1
	return (valid_count,invalid_count)
	
text_list = ["avs",[1,2,3],"dfs",(12,34),'']
print(get_valid_invalid_text_count(text_list))
