###
# optcode :
# 99 -halt the program
# 1 - adds together numbers read from two positions and stores the result in a third position.
# 2 - multiplies numbers ---|---



ex_input = [1,0,1,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,10,19,23,1,6,23,27,1,5,27,31,1,10,31,35,2,10,35,39,1,39,5,43,2,43,6,47,2,9,47,51,1,51,5,55,1,5,55,59,2,10,59,63,1,5,63,67,1,67,10,71,2,6,71,75,2,6,75,79,1,5,79,83,2,6,83,87,2,13,87,91,1,91,6,95,2,13,95,99,1,99,5,103,2,103,10,107,1,9,107,111,1,111,6,115,1,115,2,119,1,119,10,0,99,2,14,0,0]


def intcode_program(nums):

	starting_index = 0
	while True:

		if nums[starting_index] == 99:
			return nums
		
		# adding 
		if nums[starting_index] == 1:
			nums[nums[starting_index+3]] = nums[nums[starting_index+1]] + nums[nums[starting_index+2]]
			starting_index += 4
			continue

		# multipling
		if nums[starting_index] == 2:
			nums[nums[starting_index+3]] = nums[nums[starting_index+1]] * nums[nums[starting_index+2]]
			starting_index += 4
			continue


ex_input_2 = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,10,19,23,1,6,23,27,1,5,27,31,1,10,31,35,2,10,35,39,1,39,5,43,2,43,6,47,2,9,47,51,1,51,5,55,1,5,55,59,2,10,59,63,1,5,63,67,1,67,10,71,2,6,71,75,2,6,75,79,1,5,79,83,2,6,83,87,2,13,87,91,1,91,6,95,2,13,95,99,1,99,5,103,2,103,10,107,1,9,107,111,1,111,6,115,1,115,2,119,1,119,10,0,99,2,14,0,0]


def noun_and_verb(pairs_collection, lst):
	'''
	Noun and verb values are between 0 - 99.
	'''
	counter = 1
	outputs = []
	print('Patience, my friend...')
	for pair in pairs_collection:
		copy_lst = lst[:]
		copy_lst[1] = pair[0]
		copy_lst[2] = pair[1]
		result = intcode_program(copy_lst)   # <----- problem!!
		
		if result[0] == 19690720:
			print('Appending...')
			outputs.append((pair, result[0]))
			break
		counter += 1
	return outputs




def pairs_of_numbers():
	collection = list(range(0, 100))
	
	pairs = []

	for verb in collection:
		for noun in collection:
			pairs.append((verb, noun))
	return pairs


def main():

	### PART ONE ###
	#print(len(ex_input))
	#result = intcode_program(ex_input)
	#print(result)

	#####################################

	### PART TWO ###
	
	pairs = pairs_of_numbers()
	uf = noun_and_verb(pairs, ex_input_2)
	print('Done!')
	print(uf)
	print(type(uf))
	print(100 * uf[0][0][0] + uf[0][0][1])
	#test_res = intcode_program(ex_input)
	#print(test_res)



if __name__ == '__main__':
	main()
