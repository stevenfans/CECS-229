
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

    test = ([[2,3],[3,5],[2,7]])
    a = list()
    m = list()
    count = 0
    M = 1
    M_list = list()

    for group in test:
        print(group)
        a.append(group[0])
        m.append(group[1])
        M *= group[1]
        count+=1 
    for times in range(len(m)):
        M_list.append(M/m[times])

    print(M_list)

    print(inverseY(M_list[1],m[1]))

if __name__ == "__main__": 
    main()