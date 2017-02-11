
def isPalindrome( num ) :
    
    strNum = str( num )
    nDigits = len( strNum )

    isNumPalindrome = True
    for q in range ( int( nDigits / 2 ) ) :
        if strNum[q] != strNum[ nDigits - q - 1 ] :
            isNumPalindrome = False
            break
    
    return isNumPalindrome

def findPalindromes() :
    
    ## finding palindromes of the form palindrome = 'abccba'
    ## a = 1-9, b = 0-9, c = 0-9
    for a in range( 9 ) :
        aDigit = ( 9 - a )
        for b in range( 10 ) :
            bDigit = ( 9 - b )
            for c in range( 10 ) :
                cDigit = ( 9 - c )
                
                palindrome = 100001 * aDigit + 10010 * bDigit + 1100 * cDigit
                print 'checking ' , palindrome

                maxNumStep = 90
                minNumStep = 10
                rangeSteps = maxNumStep - minNumStep + 1

                for i in range( rangeSteps ) :
                    testFirstNumber = ( i + minNumStep ) * 11
                    if palindrome % testFirstNumber == 0 :
                        testSecondNumber = palindrome / testFirstNumber
                        print 'first: ' , testFirstNumber
                        print 'second: ' , testSecondNumber
                        if len( str( testSecondNumber ) ) == 3 :
                            return
                

## print isPalindrome( 12321 )
## print isPalindrome( 12322 )

findPalindromes()
 
