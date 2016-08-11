# I want to be able to call cumulative_sum from main w/ various lists and
# get returned a list of the cumulative sums.
# You are safe to expect only integers in a flat list.
# Ex. the cumulative sum of [1, 2, 3] is [1, 3, 6]
#  - in the above example I want returned the list [1, 3, 6]
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def cummulative_sum(listname):
	#initialize an empty list
	cum_sum_list = []
	cum_sum = 0 # variable to store the sum
	for numbers in listname: # for each iterm
		cum_sum += numbers # add the number to the sum
		cum_sum_list.append(cum_sum) # append the number to the list
	return cum_sum_list

def main():
	#print(cummulative_sum([1, 2, 3]))
	pass

if __name__ == '__main__':
	main()