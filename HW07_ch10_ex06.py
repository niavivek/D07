# I want to be able to call is_sorted from main w/ various lists and get
# returned True or False.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()
import copy

def is_sorted(list_sort):
	new_list = copy.deepcopy(list_sort)#make a deep copy of the list
	new_list.sort()#sort the new list
	if new_list == list_sort:#compare the list and return true if they are same
		return True
	return False
	

def main():
	#print(is_sorted([6, 2, 3]))
	#print(is_sorted(['H','A','M']))
	pass

if __name__ == '__main__':
	main()