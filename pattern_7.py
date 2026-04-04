# 1 
# 2 3
# 4 5 6
# 7 8 9 10

n = 4
p = 1
for i in range(n):
    for j in range(i + 1):
        print(p, end = " ")
        p += 1
    print()
