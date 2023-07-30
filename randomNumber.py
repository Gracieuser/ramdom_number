import random
from time import sleep
sleep(1)

def generateNumber(num1, num2):
    sleep(1)
    return(random.randint(num1, num2))

if __name__=='__main__':
    print("Test 1 generates a random number between 1 and 10.") 
    generateNumber(1,10) 
    print('\n') #This will force a new line.

    print("Test 2 generates a random number between 11 and 20.") 
    generateNumber(11, 20) 
    print('\n')
    print("Test 3 generates a random number between 21 and 30.") 
    generateNumber(21, 30) 
    print('\n')