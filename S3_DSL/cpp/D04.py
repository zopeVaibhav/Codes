#hora

def linear_search(a, target):
    for i in range(len(a)):
        if (a[i] == target):
            print("Roll no.", target, "is present at index", i)
            break

        else:
            print("Roll no.", target, "not found in list")


def binary_search(a, target):
    start = 0
    end = len(a)-1
    while (start <= end):
        mid = int((start+end)/2)

        if (a[mid] == target):
            print("Roll no.", target, "is present at index", mid)
            break

        elif (target > a[mid]):
            start = mid+1
        elif (target < a[mid]):
            end = mid-1
    else:
        print("Roll no.", target, "not found in list")


def sentinel_search(a, target):
    a.append(target)
    i = 0
    while (a[i] != target):
        i += 1

    if (i < (len(a)-1)):
        print("Roll no.", target, "is present at index", i)
    else:
        print("Roll no.", target, "not found in list")


def fibonacci_search(a, target):
    n = len(a)
    fibn_2 = 0
    fibn_1 = 1
    fibn = fibn_1+fibn_2
    while (fibn <= n):
        fibn_2 = fibn_1
        fibn_1 = fibn
        fibn = fibn_1+fibn_2
        offset = -1

    while (fibn_1 != 0):
        i = min((offset+fibn_2), n-1)
        if (target > a[i]):
            fibn = fibn_1
            fibn_1 = fibn_2
            fibn_2 = fibn-fibn_1
            offset = i

        elif (target < a[i]):
            fibn = fibn_2
            fibn_1 = fibn_1-fibn_2
            fibn_2 = fibn-fibn_1

        elif (target == a[i]):
            print("Roll no.", target, "is present at index", i)
        break

    else:
        print("Roll no.", target, "not found in list")


flag = 'y'
while (flag == 'y'):
    print("1.Sorted List Search")
    print("2.Unsorted List Search")
    choice = int(input("Enter the Choice:"))

    if (choice == 1):
        n = int(input("Enter number of students present : "))
        a = []
        for i in range(n):
            elem = int(input("Enter the roll no. of student:"))
            if (elem not in a):
                a.append(elem)
            else:
                while (elem in a):
                    print("Roll no. already present in the list!")
                    elem = int(input("Enter the roll no. of student again:"))
                a.append(elem)
        print("\nThe roll no. of students present: ", a)

        target = int(input("Enter the roll no. to be searched in list:"))
        print("1.Binary Search")
        print("2.Fibonacci Search")
        choice1 = int(input("Enter the choice:"))
        if (choice1 == 1):
            binary_search(a, target)
        if (choice1 == 2):
            fibonacci_search(a, target)
        if (choice == 2):
            n = int(input("Enter number of students present : "))
            a = []
        for i in range(n):
            elem = int(input("Enter the roll no. of student:"))
        if (elem not in a):
            a.append(elem)
        else:
            while (elem in a):
                print("Roll no. already present in the list!")
                elem = int(input("Enter the roll no. of student again:"))
            a.append(elem)
            
    print("\nThe roll no. of students present: ", a)
    target = int(input("Enter the roll no. to be searched in list:"))   
    print("1.Linear Search")
    print("2.Sentinel Search")
    choice2 = int(input("Enter the choice:"))

    if (choice2 == 1):
        linear_search(a, target)
    if (choice2 == 2):
        sentinel_search(a, target)
    flag = input("Do you want to continue (y/n):")
if (flag == 'n'):
    print("Thank You!!!")
