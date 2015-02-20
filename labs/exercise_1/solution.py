import random

def divide_33():
    random_numbers = random.sample(xrange(10000), 100)

    for num in random_numbers:
	    if num % 33 == 0:
		    print num

divide_33() 