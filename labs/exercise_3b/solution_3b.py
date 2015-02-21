#import the csv library
import csv

from operator import itemgetter

#read in the rock.csv file and save as rock_data
f = open('rock.csv', 'rb')
#store rock_data into reader
data = csv.reader(f)

#sort the data on PlayCount to see the top songs played

sort = sorted(data, key=itemgetter(6), reverse=True)
top_20 = sort[0:21]

for row in top_20:
	print row
