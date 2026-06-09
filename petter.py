for r in range(6):
    for c in range(5):
        if (c ==0 or c==4) and r!=0:
            print("*",end=" ")
        elif (c==1 or c==2 or c==3)and (r==0 or r==3):
            print("*",end=" ")
        
        else:
            print(end="  ")
    print()

#2
for r in range(6):
    for c in range(6):
        if c == 0 or c == 5 or (r == c and 1 <= r <= 4):
            print(f"({r},{c})")
        elif (c==5  or c==3)and (r==0 or r==3):
            print("*",end=" ")
        
        else:
            print(end="  ")
    print()