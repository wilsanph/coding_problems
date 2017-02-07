import time

def sum_even_fibo( Nmax ) :

    sum_fibo = 0
    f_n = 1
    f_n_1 = 1
    
    while ( f_n <= Nmax ) :
        temp = f_n
        f_n = f_n + f_n_1
        f_n_1 = temp
        if f_n % 2 == 0 :
            sum_fibo += f_n

    return sum_fibo

print 'sum_even_fibo( 20 ): ' , sum_even_fibo( 20 )
print 'sum_even_fibo( 4000000 ): ' , sum_even_fibo( 4000000 )
