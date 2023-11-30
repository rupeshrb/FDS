total = 0
def dep_with(ch):
    global total
    if(ch=="W"):
        print("ENTER AMOUNT TO WITDRAW =")
        withdraw=int(input())
        if (total > withdraw):
            total=total - withdraw
            print("after money withdraw total =",total)
        else:
            print("balance is insufficent")
    elif(ch=="D"):
        print("ENTER AMOUNT TO DEPOSIT =")
        deposit=int(input())
        total=deposit + total
        print("after money deposit total =",total)
    else:
        print("invalid choise")
while(True):
    print("1 deposit")
    print("2 withdraw")
    print("3 total money in bank")
    print("4 Exit")
    print("Enter Choice")
    choice=int(input())
    if(choice==1):
        dep_with("D")
    if(choice==2):
        dep_with("W")
    if (choice == 3):
        print("total amount in bank =",total)
    if (choice == 4):
        exit()
        

