import random

numbers_list = random.sample(xrange(10000), 100)

def divide_33(numbers):

    for num in numbers:
	    if num % 33 == 0:
		    print num

divide_33(numbers_list) 