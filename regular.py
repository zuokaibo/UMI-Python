import re
handle = open('regular.txt')
numbers = 0
for line in handle:
    line = line.rstrip()
    numbers = numbers + sum(map(lambda x: int(x), re.findall('([0-9]+)',line)))
# line 6 is using map() function and lambda function,
# check this web: https://www.geeksforgeeks.org/python-lambda-anonymous-functions-filter-map-reduce/

print(numbers)