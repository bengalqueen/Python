# Print all the Prime Numbers

def is_prime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
    
def print_primes(limit):
    for num in range(2, limit + 1):
        if is_prime(num):
            print(num)

n = int(input("Enter the limit:"))
print("Prime numbers are:")
print_primes(n)