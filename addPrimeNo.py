# Sum of Prime Numbers

def is_prime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

def sum_of_primes(limit):
    total = 0
    for num in range(2, limit + 1):
        if is_prime(num):
            total += num
    return total

n = int(input("Enter limit:"))
print("Sum of prime numbers is:", sum_of_primes(n))

        