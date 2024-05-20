# Recurse back one by one from high to low terms, then determine the lowest number of non recursive terms, and write code in the positive direction
def a(n):
  if n<1:
    print('wrong')
  else:
    if n==1:
    return 4
else:
    return a(n-1)+a(n-1)+3

if _name_=='_main_'；
 n=int(input(“Please enter the number of items in the sequence：”）)
       r=a(n)
print(r)
# So when n is equal to 1,2,3,4,5, a (n) is equal to 4,11,25,53,109
