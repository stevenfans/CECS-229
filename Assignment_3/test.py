
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

def main(): 

    test = ([[1,3],[3,5],[2,7]])
    test2 = ([[1,5], [2,7], [3,9], [4,11]])
    a = list()
    m = list()
    y = list()
    count = 0
    M = 1
    M_list = list()
    Sum = 0


    for group in test2:
        # print(group)
        a.append(group[0])
        m.append(group[1])
        M *= group[1]
        count+=1 
    for times in range(len(m)):
        M_list.append(M/m[times])
        y.append(inverseY(M_list[times],m[times]))
        Sum += (a[times] * M_list[times]* y[times])

    Sum = Sum % M

    # print(M_list)
    # print(y)
    print(int(Sum))
    # print(inverseY(M_list[1],m[1]))
    

if __name__ == "__main__": 
    main()