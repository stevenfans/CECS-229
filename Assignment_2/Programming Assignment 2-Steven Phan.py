#Steven Phan
#Shoraj Manandhar
#Allen Lupisan

# Problem 1
# Write a function that will take in three inputs: base, exponent, and divsor. The output would be the produc to the values
# of the modulus operaitons, such that when taking that as the modulus of the idvisor, you will get the problem's remainder. 
# Function name should be modulus_product.
def modulus_product(base, exponent, divisor):
    start_exponent = 1 #starting base exp. is 1 and will double each run
    answer = 1         #multiply to the product of the values of the modulus operations
    binary_equivalent_of_exponenet = format(exponent,"b")[::-1]

    for binary_digit in range(len(binary_equivalent_of_exponenet[::-1])): 
        remainder = (base**start_exponent) % divisor                #find the remainder of the modulus
        if (binary_equivalent_of_exponenet[binary_digit] == "1"):   #if we're at the binary 1 digit
            answer *= remainder                                     #multiply it
        start_exponent*=2                                           #double the exponenet
    answer %= divisor                                               #last modulus   

    return answer      

#comment out test case
#print(modulus_product(2,10,2))                                                
    
# Probelem 2.
# Write a function, isPrime(L)
# input:
#     L - list of numbers greater than 1.
# output: numbers from that list that are prime
def isPrime(L):
    #create an empty list
    list_of_primes = list()
    #traverse through every element in the list
    for num in range(len(L)): 
        prime_number = True                      #flag to check if a number is prime
        for int_below_num in range (2,L[num]):   #iterate though all ints below that number starting from 2
            #if the element number modded by anything below it is 0 then it is not prime
            if L[num]%int_below_num==0:          
                prime_number = False             #set flag to false and break to iterate new element
                break
        if prime_number == True:                 #if the elment flag is true then the number is prime
            list_of_primes.append(L[num])        #append the prime to the list  
            
    return list_of_primes         

#comment out test case
#print(isPrime([2,3,5,8,10,13]))