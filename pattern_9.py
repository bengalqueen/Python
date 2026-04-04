
# |  |
# |  |
# ||||
# |  |
# |  |

for i in range(5):
    for j in range(4):
        if j == 0 or j == 3 or (i == 2 and (j > 0 or j < 4)):
            print("|",end="")
        else:
            print(end = " ")

    print()