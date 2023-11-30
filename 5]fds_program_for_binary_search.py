import array as arr
a=0
def Add_stud():
    global a
    a = arr.array('I', [])
    no_stud = int(input("Enter the number of Students : "))
    for i in range(0, no_stud):
        a.append(int(input("Enter the Roll Number : ")))
    return a
def Bin_sec_rec(a, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        # If element is present at the middle itself
        if a[mid] == x:
            return mid

            # If element is smaller than mid, then it
        # can only be present in left subarray
        elif a[mid] > x:
            return Bin_sec_rec(a, l, mid - 1, x)

            # Else the element can only be present
        # in right subarray
        else:
            return Bin_sec_rec(a, mid + 1, r, x)

    else:
        # Element is not present in the array
        return -1
def Bin_sec_nonrec(a, l, r, x):
    while l <= r:

        mid = l + (r - l) // 2;

        # Check if x is present at mid
        if a[mid] == x:
            return mid

            # If x is greater, ignore left half
        elif a[mid] < x:
            l = mid + 1

        # If x is smaller, ignore right half
        else:
            r = mid - 1

    # If we reach here, then the element
    # was not present
    return -1
    

Add_stud()
while(True):

    print("1 search for student(usingBinary Search (Recursive))")
    print("2 search for student(usingBinary Search (Non - Recursive))")
    print("3 Exit")
    print("Enter Choice")
    choice=int(input())
    if(choice==1):
        roll = int(input("Enter the Roll Number to be search : "))
        index = Bin_sec_rec(a, 0, len(a) - 1, roll)
        if index == -1:
            print("Roll number", roll, "has not Attended the training program")
        else:
            print("Roll number", roll, " at the index", index, "has Attended the training program")

    if (choice == 2):
        roll = int(input("Enter the Roll Number to be search : "))
        index = Bin_sec_nonrec(a, 0, len(a) - 1, roll)
        if index == -1:
            print("Roll number", roll, "has not Attended the training program")
        else:
            print("Roll number", roll, " at the index", index, "has Attended the training program")

    if (choice == 3):
        exit()
