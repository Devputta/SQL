numbers = (1,2,3,4,5,6,7,8,9,0)
num = int(input("ENTER THE NUMBER TOBE FOUND : "))
idex = 0
for i in numbers:
    if(i == num):
        print("THE NUMBER :",i,"FOUND")
        print("IT FOUND AT INDER : ",idex)
    idex += 1
        

 