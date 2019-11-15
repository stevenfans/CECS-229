# Steven Phan 
# RSA Encryption 

def RSAencrypt(p,q,e,message):
    #check if the keys are relative prime
    #if they are then you can continue to encrypt message
    # isRelativePrime = True if gcd(e, ((p-1)*(q-1)))==1 else False 

    #isRelativePrime = gcd(e, ((p-1) * (1-1)))
    #check to see if p and q are prime and gcd(e,(p-1)(q-1))=1
    if len(message)<1:
        print("Message length needs to be greater than 0")
    elif isPrime(p)==False or isPrime(q)==False:
        print("Both p and q need to be prime")
    elif gcd(e,((p-1)*(q-1)))!=1:
        print("e needs to be relatively prime to (p-1)(q-1)")
    else:
        # passed through all the flag checkers
        n=p*q               #get the n value
        size = blockSize(n) #get the block size
        #first turn the letters to number values
        #second turn the number value to strings
        #third combine the string 
        string= ''.join(map(str,[letterToNumber(char) for char in message]))
        stringList = [(string[i:i+size]) for i in range(0,len(string),size)]
        # print(stringList)
        

def blockSize(n): 
    block = 25
    size = 0

    #check to when n is smaller than the block size
    while (block<n):
        block = (block*100)+25
        size +=2
    return size

def gcd(x,y):
    #get the lowest number
    min_num = min(x,y)

    # cycle and see what number divides both numbers
    for dividing_num in range(1,min_num): 
        if x%dividing_num==0 and y%dividing_num==0:
                gcd = dividing_num

    return gcd

def isPrime(x): 
    primeFlag = True
    #cycle from 1 ~ x and mod to get 0
    for num in range(2,x): 
        if x%num==0:
            primeFlag=False
            break; 
    return primeFlag

def letterToNumber(letter): 
    #get the unicode of the upperase letter
    return ord(letter)-65    
    
def main():
     RSAencrypt(43,59,13,"STOP")
    #print(blockSize(2536))
    

if __name__ == "__main__":
    main()