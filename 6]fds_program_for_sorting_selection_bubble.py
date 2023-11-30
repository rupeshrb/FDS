L=[]
def get():
    n=int(input("Enter Number of First Year Students: "))
    for i in range(n):
        no=int(input("Enter their Percentage: "))
        L.append(no)
def dis():
    for i in L:
        print(i,end=" ")
def bubble():
    cnt=1
    for i in range(len(L)-1,0,-1):
        print("Iteration No:", cnt)
        for j in range(0,i):
            if(L[j]>L[j+1]):
                L[j], L[j + 1] = L[j + 1], L[j]
                print(L)
                
        cnt+=1
    

def sel():
    for i in range(len(L)):
        min=i
        print("\nIteration No:",i)
        for j in range(i+1,len(L)):
            if L[j]<L[min]:
                min=j
        L[i],L[min]=L[min],L[i]
        print(L,end="\n")

if __name__ == '__main__':
    while(True):
        print("\n1: Selection Sort")
        print("2: Bubble Sort")
        print("3: Exit")
        ch=int(input("Enter choice"))
        if(ch==1):
            get()
            print("****Displaying List****")
            dis()
            sel()
        if(ch==2):
            get()
            print("****Displaying List****")
            dis()
            bubble()
        if(ch==3):
            exit()
