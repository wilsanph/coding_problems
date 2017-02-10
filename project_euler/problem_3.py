
import math
import time

#N = 13195
N = 600851475143
#N = 2048

open_factors = []
prime_factors = []

def search_prime_factors( pN, pOpen, pPrime ) :
    pOpen.append( pN )
    while len( pOpen ) > 0 :
        print 'open: ' , pOpen
        print 'prime: ' , pPrime
        currentNum = pOpen.pop()
        maxCheck = int( math.sqrt( currentNum ) )
        print 'currentNum: ' , currentNum
        found = False
        for q in range( maxCheck ) :
            testFactor = q + 1
            if testFactor < 2 :
                continue
            if currentNum % testFactor == 0 :
                pOpen.append( testFactor )
                newNum = currentNum / testFactor
                if ( newNum > 1 ) :
                    pOpen.append( newNum )
                found = True
                print 'newNum: ' , newNum
                print 'testFactor: ' , testFactor
                break
        print 'found: ' , found
        if not found :
            pPrime.append( currentNum )
        ## time.sleep( 1 )

search_prime_factors( N, open_factors, prime_factors )

print 'open: ' , open_factors
print 'prime: ' , prime_factors

