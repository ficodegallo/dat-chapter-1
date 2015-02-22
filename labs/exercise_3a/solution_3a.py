#import the csv library
import csv

#read in the rock.csv file and save as rock_data
with open('rock.csv', 'rb') as rock_data:
#store rock_data into reader
    reader = csv.reader(rock_data)

#count the amount of songs released in 1981
    count = 0
    for row in reader:
    	if row[2] =='1981':
    		count += 1

    print "The number of songs released in 1981 was: "
    print count


""""
    #read the header of the file
    header = reader.next()
    print header
"""

    
  