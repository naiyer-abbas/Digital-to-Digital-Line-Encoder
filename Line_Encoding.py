import random
from matplotlib import pyplot as plt

########################################################### PALINDROME  ############################
def lps(st) :
    string_list = [str(x) for x in st]
    new_st = ""
    for i in range(0,len(string_list)):
        new_st = new_st + string_list[i]
    n = len(new_st)
    table = [[0 for x in range(n)] for y
             in range(n)]

    max_length = 1
    i = 0
    while i < n:
        table[i][i] = 1
        i = i+12
    begin = []
    i = 0
    while i < n-1:
        if new_st[i] == new_st[i+1]:
            table[i][i + 1] = 1
            begin.append(i)
            max_length = 2
        i = i+1


    p = 2
    while p < n:
        i = 0
        while i < (n-p):
            j = i+p
            if (new_st[i] == new_st[j] and table[i+1][j-1] == 1):
                table[i][j] = 1
                if p >= max_length - 1:
                    if p >= max_length:
                        begin = []
                    max_length = p+1
                    begin.append(i)
            i = i+1
        p = p+1
    str_final = ""
    for i in range (0,len(begin)) :
        str_final = str_final  + new_st[begin[i] : begin[i] + max_length] + ' '

    print("\nLongest Palndromic sequences : ", str_final)
    print("length = ",max_length)


#***********************************************NRZ-L**********************************************************#
def nrz_l(l):
    l1 = [0]
    l2=[0]
    for y in range(1,len(l)):
        l2.append(y)
    l2.append(y+1)
    for j in range(0,len(l)):
        if l[j] == 0:
            l1.append(1)
        elif l[j] == 1:
            l1.append(-1)
        else:
            print("error")
            quit()
    plt.step(l2, l1, 'r')
    plt.plot([0,0,0,0,0],[-2,-1,0,1,2],'c')
    plt.hlines(0, 0, len(l2)-1, linestyles='-', colors='c')
    plt.show()

#*********************************************** NRZ-I *************************************************************#
def nrz_i(l):
    l1 = [1]
    l2 = [0]
    for i in range(1,len(l)):
        l2.append(i)
    l2.append(i+1)
    for j in range(0,len(l)):
        if l[j] == 0:
            l1.append(l1[j])
        elif l[j] == 1:
            l1.append(-1*l1[j])
        else:
            print("Error")
            quit()
    plt.step(l2, l1, 'r')
    plt.plot([0, 0, 0, 0, 0], [-2, -1, 0, 1, 2], 'c')
    plt.hlines(0, 0, len(l2) - 1, linestyles='-', colors='c')
    plt.show()

# **********************************************************************    MANCHESTER  *********************************************************************#

def manchester(l):
    l1 = [1]
    l2 = [0]
    for i in range(1, 2*len(l)):
        l2.append(i/2)
    l2.append(i/2 + 1)
    for j in range(0, len(l)):
        if l[j] == 0:
            l1.append(1)
            l1.append(-1)
        elif l[j] == 1:
            l1.append(-1)
            l1.append(1)
        else:
            print("Error")
            quit()
    plt.step(l2, l1, 'r')
    plt.plot([0, 0, 0, 0, 0], [-2, -1, 0, 1, 2], 'c')
    plt.hlines(0, 0, len(l2) - 1, linestyles='-', colors='c')
    plt.show()

# ************************************************************************************  DIFF MANCHESTER *************************************************************************#

def diff_manchester(l):
    l1 = []
    l2 = [0]
    for i in range(1, 2 * len(l)):
        l2.append(i / 2)

    l2.append(i / 2 + 1)
    if(l[0] == 0):
        l1.append(-1)
        l1.append(1)
    elif(l[0] == 1):
        l1.append(1)
        l1.append(-1)
    k = 2
    for j in range(1, len(l)):

        if l[j] == 0:
            l1.append(l1[k-2])
            l1.append(l1[k-1])
        elif l[j] == 1:
            l1.append(-1*l1[k-2])
            l1.append(-1*l1[k-1])
        else:
            print("Error")
            quit()
        k = k + 2
    l1.insert(0,1)
    plt.step(l2, l1, 'r')
    plt.plot([0, 0, 0, 0, 0], [-2, -1, 0, 1, 2], 'c')
    plt.hlines(0, 0, len(l2) - 1, linestyles='-', colors='c')
    plt.show()

# **********************************************************************************    AMI     *********************************************************************************#

def ami(l):
    l1 = [1]
    l2 = [0]
    for y in range(1, len(l)):
        l2.append(y)
    l2.append(y + 1)
    ones_count = 0
    for j in range(0, len(l)):
        if l[j] == 0:
            l1.append(0)
        elif l[j] == 1:
            ones_count = ones_count + 1
            if ones_count % 2 == 1:
                l1.append(1)
            elif ones_count % 2 == 0:
                l1.append(-1)
        else:
            print("error")
            quit()
    plt.step(l2, l1, 'r')
    plt.plot([0, 0, 0, 0, 0], [-2, -1, 0, 1, 2], 'c')
    plt.hlines(0, 0, len(l2) - 1, linestyles='-', colors='c')
    plt.show()


    #***************************************************************************    B8ZS    ********************************************************#
def find_zero_sequence(l,x):
    zero_count = 0
    l2 = []
    for i in range(len(l)):
        if l[i] == 0:
            zero_count = zero_count + 1
        if l[i] == 1:
            zero_count = 0
        if zero_count == x:
            l2.append(i - (x-1))
            l2.append(i)
    return l2
#   *********************************************   #
def B8ZS(l):
    l3 = [0]
    l4 = [1]
    l2 = find_zero_sequence(l,8)
    ones_count = 0
    for y in range(1, len(l)):
        l3.append(y)
    l3.append(y + 1)
    if len(l2) > 0:
        for i in range(0,l2[0]):
            if l[i] == 0 :
                l4.append(0)
            elif l[i] == 1:
                ones_count = ones_count + 1
                if ones_count % 2 == 1:
                    l4.append(1)
                elif ones_count % 2 == 0:
                    l4.append(-1)

        if l4[-1] == 1:
            l4.append(0)
            l4.append(0)
            l4.append(0)
            l4.append(1)
            l4.append(-1)
            l4.append(0)
            l4.append(-1)
            l4.append(1)
        elif l4[-1] == -1:
             l4.append(0)
             l4.append(0)
             l4.append(0)
             l4.append(-1)
             l4.append(1)
             l4.append(0)
             l4.append(1)
             l4.append(-1)
        if len(l2) == 2:
            for i in range(l2[1] + 1, len(l)):
                if l[i] == 0:
                    l4.append(0)
                elif l[i] == 1:
                    ones_count = ones_count + 1
                    if ones_count % 2 == 1:
                        l4.append(1)
                    elif ones_count % 2 == 0:
                        l4.append(-1)
        elif len(l2) > 2:
            for i in range(l2[1] + 1, l2[2]):
                if l[i] == 0:
                    l4.append(0)
                elif l[i] == 1:
                    ones_count = ones_count + 1
                    if ones_count % 2 == 1:
                        l4.append(1)
                    elif ones_count % 2 == 0:
                        l4.append(-1)
            if l4[-1] == 1:
                l4.append(0)
                l4.append(0)
                l4.append(0)
                l4.append(1)
                l4.append(-1)
                l4.append(0)
                l4.append(-1)
                l4.append(1)
            elif l4[-1] == -1:
                l4.append(0)
                l4.append(0)
                l4.append(0)
                l4.append(-1)
                l4.append(1)
                l4.append(0)
                l4.append(1)
                l4.append(-1)
            for i in range(l2[3]+1, len(l)):
                if l[i] == 0:
                    l4.append(0)
                elif l[i] == 1:
                    ones_count = ones_count + 1
                    if ones_count % 2 == 1:
                        l4.append(1)
                    elif ones_count % 2 == 0:
                        l4.append(-1)
    else:
        print("No sequence found. Please change your input")
        quit()
    plt.step(l3, l4, 'r')
    plt.plot([0, 0, 0, 0, 0], [-2, -1, 0, 1, 2], 'c')
    plt.hlines(0, 0, len(l), linestyles='-', colors='c')
    plt.show()

def count_nonzero_pulses(l):
    count = 0
    for i in range(len(l)):
        if l[i] == 1 or l[i] == -1:
            count = count + 1
    return count


def HDB3(l):
    l3 = [0]
    l4 = [1]
    l2 = find_zero_sequence(l, 4)
    ones_count = 0
    for y in range(1, len(l)):
        l3.append(y)
    l3.append(y + 1)
    if len(l2) > 0:
        for i in range(0, l2[0]):
            if l[i] == 0:
                l4.append(0)
            elif l[i] == 1:
                ones_count = ones_count + 1
                if ones_count % 2 == 1:
                    l4.append(1)
                elif ones_count % 2 == 0:
                    l4.append(-1)

        if count_nonzero_pulses(l4) % 2 == 0:
            l4.append(0)
            l4.append(0)
            l4.append(0)
            l4.append(l4[-4])

        elif count_nonzero_pulses(l4) % 2 == 1:
            l4.append(-1*l4[-1])
            l4.append(0)
            l4.append(0)
            l4.append(l4[-3])
        if len(l2) == 2:
            for i in range(l2[1] + 1, len(l)):
                if l[i] == 0:
                    l4.append(0)
                elif l[i] == 1:
                    ones_count = ones_count + 1
                    if ones_count % 2 == 1:
                        l4.append(1)
                    elif ones_count % 2 == 0:
                        l4.append(-1)
        elif len(l2) >2:
            for i in range(l2[1] + 1, l2[2]):
                if l[i] == 0:
                    l4.append(0)
                elif l[i] == 1:
                    ones_count = ones_count + 1
                    if ones_count % 2 == 1:
                        l4.append(1)
                    elif ones_count % 2 == 0:
                        l4.append(-1)
            if count_nonzero_pulses(l4) % 2 == 0:
                l4.append(0)
                l4.append(0)
                l4.append(0)
                l4.append(l4[-4])
            elif count_nonzero_pulses(l4) % 2 == 1:

                l4.append(-1*l4[-1])
                l4.append(0)
                l4.append(0)
                l4.append(l4[-3])
                l4.append(-1)
                l4.append(0)
                l4.append(0)
                l4.append(l4[-3])
            for i in range(l2[3] + 1, len(l)):
                if l[i] == 0:
                    l4.append(0)
                elif l[i] == 1:
                    ones_count = ones_count + 1
                    if ones_count % 2 == 1:
                        l4.append(1)
                    elif ones_count % 2 == 0:
                        l4.append(-1)

    else:
        print("No sequence found. Please change your input")
        quit()
    plt.step(l3, l4, 'r')
    plt.plot([0, 0, 0, 0, 0], [-2, -1, 0, 1, 2], 'c')
    plt.hlines(0, 0, len(l), linestyles='-', colors='c')
    plt.show()

while True:
    print("     \nFor Random press 1\t\t For sequential press 2 \t\t Press 0 to exit")
    print("Enter Your Choice : ", end="")
    x = int(input())
    print("Data generated : ")
    if x == 1 :
        randomlist = [0, 1] * 6
        random.shuffle(randomlist)
        for i in randomlist :
            print(i, end="")
    elif x == 2 :
        randomlist_with_seq_1 = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
        random.shuffle(randomlist_with_seq_1)
        for i in randomlist_with_seq_1 :
            print(i, end="")
    elif x==0 :
        quit()
    else:
        print("Enter a valid character")
    if x==1:
        lps(randomlist)
    elif x==2:
        lps(randomlist_with_seq_1)
    print("\nWhich type of encoding do you want to perform : ")
    print("         NRZ-L -> 1")
    print("         NRZ-I -> 2")
    print("         MANCHESTER ->3")
    print("         Differential Manchester -> 4")
    print("         AMI -> 5")
    print("Enter your choice : ", end="")
    y = int(input())
        #NRZ-L
    if y == 1:
        if x ==1:
            nrz_l(randomlist)
        elif x ==2:
            nrz_l(randomlist_with_seq_1)

        #NRZ-I
    if y == 2:
        if x ==1:
            nrz_i(randomlist)
        elif x ==2:
            nrz_i(randomlist_with_seq_1)

        #MANCHESTER
    if y ==3:
        if x == 1:
            manchester(randomlist)
        elif x == 2:
            manchester(randomlist_with_seq_1)

        #DIFF_MANCHESTER
    if y == 4:
        if x==1:
            diff_manchester(randomlist)
        elif x==2:
            diff_manchester(randomlist_with_seq_1)

        #AMI
    if y == 5:
        if x == 1:
            ami(randomlist)
        elif x==2:
            ami(randomlist_with_seq_1)
        print("Do you wish to perform scrambling? (y/n) : ", end="")
        z = input()
        if z == 'y':
            print("\nWhich type of scrambling do you need? ")
            print("     B8ZS -> 1")
            print("     HDB3 -> 2")
            print("Enter you choice : ", end="")
            p = int(input())
            if (p == 1) and (x == 1):
                B8ZS(randomlist)
            elif (p == 1) and (x == 2):
                B8ZS(randomlist_with_seq_1)
            elif (p == 2) and (x == 1):
                HDB3(randomlist)
            elif (p == 2) and (x == 2):
                HDB3(randomlist_with_seq_1)
        elif z == 'n' :
            print("\nAlright")
        else:
            print("Wrong command! Please Star over")
    print("Run the program again? (y/n) : ", end="")
    f = input()
    if f == 'n':
        print("\nThank you for using this program!!")
        quit()






