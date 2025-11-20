#odd numbers

n = 0
while n <= 10:
    if( n % 2 == 0):
        n += 1
        continue # it just act like skip it will skip the 5th number in sequence "here i am skipping even numbers"
    print(n)
    
    n += 1