
import math

def sum_mults_3_5( n ) :

    num_mult_3 = math.floor( n / 3. )
    num_mult_5 = math.floor( n / 5. )
    num_mult_15 = math.floor( n / 15. )

    if ( n % 3 == 0 ) : num_mult_3 -= 1
    if ( n % 5 == 0 ) : num_mult_5 -= 1
    if ( n % 15 == 0 ) : num_mult_15 -= 1

    sum_mult_3 = 3 * num_mult_3 * ( num_mult_3 + 1 ) / 2
    sum_mult_5 = 5 * num_mult_5 * ( num_mult_5 + 1 ) / 2
    sum_mult_15 = 15 * num_mult_15 * ( num_mult_15 + 1 ) / 2

    return sum_mult_3 + sum_mult_5 - sum_mult_15

print 'f(10):' , sum_mults_3_5( 10 )
print 'f(1000):' , sum_mults_3_5( 1000 )
