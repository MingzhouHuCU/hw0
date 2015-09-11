import csv

liquor = open('iowa-liquor-sample.csv')
l = csv.reader(liquor)
count = 0


for rows in l:
    if  rows[11].lower() == 'single malt scotch':
	count += 1

print count
