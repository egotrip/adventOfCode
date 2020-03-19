###
import math

from lst import values


def main():
	# result = single_module_fuel_requirement(value)
	# print(result)
	# result = total_fuel_requirements(values)
	# print(f'Sum : {result}')

	# print(fuel_recursion(14))

	result_2 = total_fuel_requirements_part_2(values)
	print(result_2)





### PART ONE ###

def single_module_fuel_requirement(num):
	if not num > 0:	
		return
	result = math.floor(num /3) - 2	
	return result


def total_fuel_requirements(lst):
	# check if the list is empty, return if so
	if not lst:
		return

	total = 0
	for val in values:
		total += math.floor(val/3) - 2
		print(f'Total: {total}')
	return total
#######################################################
##############
##############



### PART TWO ###


def total_fuel_requirements_part_2(lst):
	total = 0
	for val in values:
		single_module_total = 0
		single = math.floor(val/3) - 2
		while single > 0:
			single_module_total += single
			single = math.floor(single/3) - 2
		total += single_module_total
	return total




if __name__ == '__main__':
	main()
