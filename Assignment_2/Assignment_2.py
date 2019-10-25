#Steven Phan
#014358810

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
        

# Probelem 2.
# Write a function, isPrime(L)
# input:
#     L - list of numbers greater than 1.
# output: numbers from that list that are prime
def isPrime(L):
    (values) = [(expression) for (value) in (collection) if condition]
    for num in len(range(L)):
        if L[num] 
    test = list()
    for num in range(len(L)): 
        for ints_below_num in range (2,L[num]+1):
           # print (L[num], "divided by", ints_below_num, "equal to", L[num]%ints_below_num)
            if x
    answer = [L[num] for num in range(len(L)) for ints_below_num in range(2,L[num]+1) if L[num]%ints_below_num != 0]
     print(answer)
    return False

isPrime([2,3,5,8,10,13])
# print (list(set(range(2,11)) - {x for x in range(11) for y in range(2,x) if x%y == 0}))