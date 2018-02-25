# Python code for CTF question.
import random

d = 10
max_input = 255

# min input is 2

def valid_primes_sieve():
	bound = ((d+2)*max_input)
	isprime = [True for x in range(bound)]
	for i in range(2, bound):
		for j in range(2, bound/i):
			isprime[i*j] = False;
	prime_options = {}
	count = 0
	primes = isprime
	for i in range(len(isprime)):
		if isprime[i] is True:
			prime_options[count] = i
			count = count + 1
	return prime_options

def sieve():
	bound = ((d+2)*max_input)
	isprime = [True for x in range(bound)]
	for i in range(2, bound):
		for j in range(2, bound/i):
			isprime[i*j] = False;
	return isprime

def factorize(input):
	factors = []
	for i in range(1, input):
		if input%i is 0:
			factors.append(i)
	return factors


input = # Input List

print "Encrypting..."

# Step 1: Inflate input difficulty(d)+1 times
inflated_input = [(d+1)*x for x in input]
prime_options = valid_primes_sieve()
priv_key = 2
while priv_key <= (d+1)*max_input:
	priv_key = prime_options[random.randint(1,len(prime_options))]

pub_key = 2
while pub_key <= (d+1)*max_input or pub_key == priv_key:
	pub_key = prime_options[random.randint(1,len(prime_options))]

print "Private Key: ", priv_key
print "Public Key: ", pub_key

check = [0 for x in range(pub_key+1)]
for x in range(1, 256):
	check[(priv_key*(d+1)*x)%(pub_key)] = check[(priv_key*(d+1)*x)%(pub_key)] + 1
	if check[(priv_key*(d+1)*x)%(pub_key)] > 1:
		print "error"

cipher = []
for x in input:
	cipher.append((priv_key*(d+1)*x)%(pub_key)+random.randint(1,3))

print "Cipher Text: ", cipher
