
import math

def getSmallestMultiple( maxNum ) :

    nums = [ q + 1 for q in range( maxNum ) ]
    return lessCommonMultiple( nums )

def lessCommonMultiple( numbers ) :
    ## i.e. [1,2,3,4,5,6,7,8]
    result = 1
    ## naive way
    for i in range( len( numbers ) ) :
        print 'numbers: ' , numbers
        print 'result: ' , result
        while ( numbers[i] != 1 ) :
            maxCheck = int( math.sqrt( numbers[i] ) )
            foundDivisor = False
            for j in range( maxCheck - 1 ) :
                numTest = j + 2
                if numbers[i] % numTest == 0 :
                    result = result * numTest
                    for k in range( len( numbers ) ) :
                        if numbers[k] % numTest == 0 :
                            numbers[k] = numbers[k] / numTest
                    foundDivisor = True
                    break
            if not foundDivisor :
                result = result * numbers[i]
                ##print 'foo'
                for k in range( len( numbers ) ) :
                    if k == i :
                        continue
                    ##print 'num[k] ' , numbers[k] , 'num[i] ' , numbers[i]
                    if numbers[k] % numbers[i] == 0 :
                        numbers[k] = numbers[k] / numbers[i]
                numbers[i] = 1

    return result

print getSmallestMultiple( 10 )
print getSmallestMultiple( 20 )
##print math.factorial( 20 )
