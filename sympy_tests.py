from sympy import sieve, prime

# https://docs.sympy.org/latest/modules/ntheory.html

print ([i for i in sieve.primerange(19)])
prime_less_than_100 = [i for i in sieve.primerange(100)]
print (prime_less_than_100)
print(len(prime_less_than_100))
prime_less_than_210 = [i for i in sieve.primerange(210)]
print(prime_less_than_210)
print(len(prime_less_than_210))
