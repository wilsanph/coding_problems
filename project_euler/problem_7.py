

import math

def isPrime( num ) :

    maxTest = int( math.sqrt( num ) )
    testFactor = 2

    for q in range( 1, maxTest + 1 ) :
        
        if testFactor == num :
            return True
        elif num % testFactor == 0 :
            return False
        
        testFactor += 1

    return True

def naive_generatePrimes( maxLen ) :
    
    primes = []
    testPrime = 2

    while True :

        if isPrime( testPrime ) :
            primes.append( testPrime )

        testPrime += 1
        
        if len( primes ) == maxLen :
            break
     
    return primes   

print naive_generatePrimes( 101 )
