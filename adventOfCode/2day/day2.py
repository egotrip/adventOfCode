###
# optcode :
# 99 -halt the program
# 1 - adds together numbers read from two positions and stores the result in a third position.
# 2 - multiplies numbers ---|---



ex_input = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,10,19,23,1,6,23,27,1,5,27,31,1,10,31,35,2,10,35,39,1,39,5,43,2,43,6,47,2,9,47,51,1,51,5,55,1,5,55,59,2,10,59,63,1,5,63,67,1,67,10,71,2,6,71,75,2,6,75,79,1,5,79,83,2,6,83,87,2,13,87,91,1,91,6,95,2,13,95,99,1,99,5,103,2,103,10,107,1,9,107,111,1,111,6,115,1,115,2,119,1,119,10,0,99,2,14,0,0]


def restore_the_gravity_assist(nums):
	restored = nums

	starting_index = 0
	while True:
		if restored[starting_index] == 99:
			return restored
		
		# adding 
		if restored[starting_index] == 1:
			restored[restored[starting_index+3]] = restored[restored[starting_index+1]] + restored[restored[starting_index+2]]
			starting_index += 4
			continue

		# multipling
		if restored[starting_index] == 2:
			restored[restored[starting_index+3]] = restored[restored[starting_index+1]] * restored[restored[starting_index+2]]
			starting_index += 4
			continue





def main():

	### PART ONE ###
	print(len(ex_input))
	result = restore_the_gravity_assist(ex_input)
	print(result)

	#####################################

	### PART TWO ###
	




if __name__ == '__main__':
	main()
