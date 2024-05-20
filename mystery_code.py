# What does this piece of code do?
# Answer:The purpose of this code is to generate random numbers from integers between 1 and 10, then add these random numbers together until the value reaches or exceeds 100, and then output the total.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress=0
total_random_number=0
while progress<100:
# As long as the value of progress is less than 100, the loop will continue to execute.
	progress+=1
# Increase the value of progress in each loop by 1
	n = randint(1,10)
	total_random_number = total_random_number+n

print(total_random_number)
