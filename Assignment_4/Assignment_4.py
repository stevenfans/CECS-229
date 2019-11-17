# Steven Phan 
# RSA Encryption 

def RSAencrypt(p,q,e,message):
    #make message all caps just in case
    message = message.upper()
    
    #check to see if p and q are prime and gcd(e,(p-1)(q-1))=1
    if len(message)<1:
        # print("Message length needs to be greter than 0")
        answer = "Message length needs to be greater than 0"
    elif isPrime(p)==False or isPrime(q)==False:
        # print("Both p and q need to be prime")
        answer = "Both p and q need to be prime"
    elif gcd(e,((p-1)*(q-1)))!=1:
        # print("e needs to be relatively prime to (p-1)(q-1)")
        answer = "e needs to be relatively prime to (p-1)(q-1)"
    else:
        # passed through all the flag checkers
        n=p*q               #get the n value
        size = blockSize(n) #get the block size
        print(size)
        #first create a list and turn the letters to their index values from 0~25
        string= ''.join(map(str,[letterToNumber(char) for char in message]))
        print(string)
        #second turn the index values from string to int  and then seperate them by the block size
        # intList = list(map(int,[(string[i:i+size]) for i in range(0,len(string),size)]))
        strList = [string[i:i+size] for i in range(0,len(string),size)]
        print(strList)
        #pad the string with extra zeros where it needs it on the right 
        #then turn all contents in list from string->int
        intList = list(map(int,[rightPad(stringToPad,size) for stringToPad in strList]))
        print(intList)
        #used the formula C=M^e(mod n) and put into a string list
        c_list = list(map(str,[((M**e)%n) for M in intList]))
        print(c_list)
        answer = [leftPad(stringToPad,size) for stringToPad in c_list]
        #TODO: need to pad 0's to string
    return answer

#function pads extra zeros to the right side
def rightPad(stringToPad,blockSize):
    number_of_zeros =(blockSize-len(stringToPad)) * '0'
    return stringToPad+number_of_zeros

#funciton pads extra zeros on the left side
def leftPad(stringToPad,blockSize):
    number_of_zeros=(blockSize-len(stringToPad))*'0'
    return number_of_zeros+stringToPad
       
#returns the size block for RSA encryption
def blockSize(n): 
    block = 25
    size = 0

    #check to when n is smaller than the block size
    while (block<n):
        block = (block*100)+25
        size +=2
    return size

#returns the greatest common divisor of 2 numbers
def gcd(x,y):
    #get the lowest number
    min_num = min(x,y)

    # cycle and see what number divides both numbers
    for dividing_num in range(1,min_num): 
        if x%dividing_num==0 and y%dividing_num==0:
                gcd = dividing_num

    return gcd

#checks if number is prime and returns T/F
def isPrime(x): 
    primeFlag = True
    #cycle from 1 ~ x and mod to get 0
    for num in range(2,x): 
        if x%num==0:
            primeFlag=False
            break; 
    return primeFlag

#function reutrns the index value of a capital letter as a string
def letterToNumber(letter): 
    # return ord(letter)-65    
    #get the unicode of the upperase letter
    number = ord(letter)-65
    #if the number is less than 10 pad it with a 0
    str_number = '0'+str(number) if number<10 else str(number)
    return str_number
    
def main():
    # print(RSAencrypt(43,59,13,"STOP"))
    # print(RSAencrypt(43,59,13,"ABC"))
    # print(RSAencrypt(43,59,13,""))
    print(RSAencrypt(503,509,21,"HELLO"))
    # print(RSAencrypt(43,14,13,"ABC"))
    # print(RSAencrypt(11,13,10,"EXCELLENT"))

if __name__ == "__main__":
    main()