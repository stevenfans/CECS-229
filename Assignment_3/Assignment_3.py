#Steven Phan

#function takes in a list of lists
#returns whether the gcd of all sublists is 1
def isRelativePrime(L):

    for sub_list in L:
        lowest_int = sub_list[0] if sub_list[0] <= sub_list[1] else sub_list[1]

        #start from 1 and loop to the lowest input (x or y)
        for number in range(1,lowest_int): 
            if sub_list[0] % number == 0 and sub_list[1] % number == 0:
                gcd = number

    return True if gcd == 1 else False


#return the inverse mod a.k. y
def inverseY(M, m):
    
    isInverse = False
    y = 1

    while (isInverse == False): 
        answer = (M*y) % m
        if answer == 1: 
            isInverse == True
            break
        else: 
            y += 1

    return y

def ChineseRemainderTheorem(L): 
    a = list()
    m = list()
    y = list()
    count = 0
    M = 1
    M_list = list()
    Sum = 0
   
   #check to see if relatie prime
    if (isRelativePrime(L)  == True):
        for group in L:
            a.append(group[0])
            m.append(group[1])
            M *= group[1]
            count+=1 

        for times in range(len(m)):
            M_list.append(M/m[times])
            y.append(inverseY(M_list[times],m[times]))
            Sum += (a[times] * M_list[times]* y[times])
           
        for group in L:
            a.append(group[0])
            m.append(group[1])
            M *= group[1]
            count+=1 


        for times in range(len(m)):
            M_list.append(M/m[times])
            y.append(inverseY(M_list[times],m[times]))
            Sum += (a[times] * M_list[times]* y[times])

        print("test")
        Sum = Sum % M
        print(Sum)
        return Sum

    else:
        string = """Cannot proceed, the modulus values are not relatively prime. 
                  Thus, you should also implement a relatively prime function
                  to ensure the list of moduluses are relatively prime"""

        return (string)
    
def main(): 

    test = ([[1,3],[3,5],[2,7]])
    # test2 = ([[1,5], [2,7], [3,9], [4,11]])
    # test3 = ([1,5],[2,7], [3,9], [4,11],[8,22])

    print(ChineseRemainderTheorem(test))
    # a = list()
    # m = list()
    # y = list()
    # count = 0
    # M = 1
    # M_list = list()
    # Sum = 0


    # for group in test2:
    #     a.append(group[0])
    #     m.append(group[1])
    #     M *= group[1]
    #     count+=1 

    # for times in range(len(m)):
    #     M_list.append(M/m[times])
    #     y.append(inverseY(M_list[times],m[times]))
    #     Sum += (a[times] * M_list[times]* y[times])

    # Sum = Sum % M

    # print(int(Sum))
    # print(isRelativePrime(test3))
    

if __name__ == "__main__": 
    main()