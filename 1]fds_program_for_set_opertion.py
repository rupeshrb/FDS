groupA=[]
groupB=[]
groupC=[]
univ=[]

def get_data():
    print("enter number of student in class :")
    uni=int(input());
    global univ
    for i in range(1,uni+1):
        univ.append(i)
    print(univ)
    
    print("enter number of student cricket :")
    A=int(input())
    global groupA
    print("enter the roll no who play cricket :")
    for i in range(A):
        A_roll=int(input("enter roll no :"))
        groupA.append(A_roll)
    print(groupA)
    
    print("enter number of student badmiton :")
    B=int(input())
    global groupB
    print("enter the roll no who play badmiton :")
    for i in range(B):
        B_roll=int(input("enter roll no :"))
        groupB.append(B_roll)
    print(groupB)

    print("enter number of student football :")
    C=int(input());
    global groupC
    print("enter the roll no who play football :")
    for i in range(C):
        C_roll=int(input("enter roll no :"))
        groupC.append(C_roll)
    print(groupC)

    
#1. List of Students who play both Cricket And Badminton:
def Cri_Bad():
    cri_bad=[]
    for i in groupA:
        for j in groupB:
            if i==j:
                cri_bad.append(j)
    print("List of Students who play both Cricket And Badminton: ",cri_bad)    
#2. List of Students who play either Cricket Or Badminton but Not Both:
def Eit_Cri_Bad():
    eit_cri_bad=[]
    for i in groupA:
        if i not in groupB:
            eit_cri_bad.append(i)
    for j in groupB:
        if j not in groupA:
            eit_cri_bad.append(j)  
    print("List of Students who play either Cricket Or Badminton but Not Both: ",eit_cri_bad)
#3. List of Students who play neither Cricket nor Badminton:
def Nei_Cri_bad():
    nei_cri_bad=[]
    nei_cri_bad.extend(groupA)
    for j in groupB:
        if j not in nei_cri_bad:
            nei_cri_bad.append(j)
    not_cri_bad=[]
    for i in univ:
        if i not in nei_cri_bad:
            not_cri_bad.append(i)
    print("List of Students who play neither Cricket nor Badminton: ",not_cri_bad)
#4. List of students who play Cricket And football but not Badminton:
def Not_bad():
    cri_foot=[]
    cri_foot.extend(groupA)
    for j in groupC:
        if j not in cri_foot:
            cri_foot.append(j)
    not_bad=[]
    for i in cri_foot:
        if i not in groupB:
            not_bad.append(i)
    print("List of students who play Cricket And football but not Badminton: ",not_bad)
get_data()
while(True):
    print("1. List of Students who play both Cricket And Badminton: ")
    print("2. List of Students who play either Cricket Or Badminton but Not Both: ")
    print("3. List of Students who play neither Cricket nor Badminton but Not Both: ")
    print("4. List of students who play Cricket And Football but not Badminton: ")
    print("5. Exit")
    print("Enter choice =")
    ch=int(input())
    if(ch==1):
        Cri_Bad()
    if(ch==2):
        Eit_Cri_Bad()
    if(ch==3):
        Nei_Cri_bad()
    if(ch==4):
        Not_bad()
    if(ch==5):
        exit()    
