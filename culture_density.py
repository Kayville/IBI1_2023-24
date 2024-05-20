cell_density = 5%
day_count = 0

def day_count(n)
if cell_density > 90%:
   return 
    day_count += 1
    cell_density *= 2
# Cell density doubled


if __name__ == '__main__':
    n = int(input("Please enter the number of days："))
    r = day_count(n)
    print(r)

    print("On day {day_count}, cell density is {cell_density}.")

print("Total days taken: {day_count}")
