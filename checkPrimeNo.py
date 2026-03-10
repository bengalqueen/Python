# Check Prime Number or Not

def is_prime(n):
    if n <= 1:
        return False

    else:
        for i in range(2,n):
            if n % i == 0:
                return False
        return True
    
ans = is_prime(13)

if ans == True:
    print("Prime No")
else:
    print("Not a Prime No")
