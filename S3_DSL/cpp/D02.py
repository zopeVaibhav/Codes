# nai horra
def printMenu():

    print('-----------------Menu--------------------')
    print('1. Enter a str: ')
    print('2. Find the longest word in the str: ')
    print('3. Find Frequency of occurence of char: ')
    print('4. Find Frequency of occurence of word: ')
    print('5. Check for palindrome: ')
    print('6. Index of first appearance of substr: ')
    print('7. Exit: ')
    print('-----------------------------------------')
    choice = int(input('Enter a choice (1-7): '))
    return choice
# function to find character occurrence


def count_Occurrence(ch, str1):
    count = 0
    for i in range(len(str1)):
        if (str1[i] == ch):
            count = count + 1
            return count
# function to find word occurence


def word_Occurrence(word, str):
    count = 0
    for i in range(len(str)):
        if (word[i] == word):
            count = count + 1
            return count


def index_Substr(s1, s2):

    M = len(s1)
    N = len(s2)
    for i in range(N - M + 1):
        for j in range(M):
            if (s2[i + j] != s1[j]):
                break
    if j + 1 == M:
        return i
        return -1

choice = printMenu()
flag = False
    
while (choice != 7):
    if  choice == 1:
        flag = True
        # Input a str
        str = input('Enter a str: ')
        break
    
    elif choice == 2:
        if flag == False:
            print("Please Enter Choice 1")
        
            
        else:
        # Finding the length of the longest word
            word = str.split()
            print(word)
            maxlen = 0
            maxword = ''
            for word in word:
                if len(word) > maxlen:
                    maxlen = len(word)
                    maxword = word
            print('The longest word is : ', maxword)
            print('length of the longest word is : ', maxlen)
    
    elif choice == 3:
        if flag == False:
            print("Please Enter Choice 1")
            break
    
        else:
            # finding the occurrence of input char
            char = input("Please enter your own Character : ")
            cnt = count_Occurrence(char, str)
            print("The total Number of Times ", char, " has Occurred = ", cnt)
            
    elif choice == 4:
        if flag == False:
            print("Please Enter Choice 1")
            break
        else:
            word = input("Please enter your own Word : ")
            wrd = word_Occurrence(word, str)
            print("The total Number of Times ", word, " has Occurred = ", wrd)
            
    elif choice == 5:
        if flag == False:
            print("Please Enter Choice 1")
            break
        else:
            # s is reverse of str
            a = str.lower()
            s = a[::-1]
        if (s == a):
            print('The str is palindrome')
        else:
            print('The str is not a palindrome')
    elif choice == 6:
        if flag == False:
            print("Please Enter Choice 1")
            break
        else:
            substr = input('Enter a substr: ')
            res = index_Substr(substr, str)
        if res == -1:
            print("Not present")
        else:
            print("Present at index " + str(res))
            
            
    elif choice == 7:
        if flag == False:
            print("-----------Exit-----------")
choice = printMenu()
