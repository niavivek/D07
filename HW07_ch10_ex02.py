# I want to be able to call capitalize_nested from main w/ various lists
# and get returned a new nested list with all strings capitalized.
# Ex. ['apple', ['bear'], 'cat']
# Verify you've tested w/ various nestings.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()


def capitalize_nested(capital_list):
	#initialize an empty list
	cap_string = []
	for words in capital_list:
		#for each item in list, if item is a list call function recursively and add to list
		if type(words) == list:
			cap_string.append(capitalize_nested(words))
		else:# else append to list if the item is not a list
			cap_string.append(words.upper())
	return cap_string

def main():
	#print(capitalize_nested(['hello',['apple', 'bear'], 'cat']))
	pass
if __name__ == '__main__':
	main()


