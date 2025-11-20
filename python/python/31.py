#EVEN numbers

i = 0
while i <= 10:
    if(i%2 != 0):
        i += 1
        continue # here i am skipping odd numbers
    print(i)
    i += 1