from math import sqrt
def sushu(x):
    if x == 1:
        return False
    k = int(sqrt(x))
    for j in range(2,k+2):
        if x % j == 0:
            return False
        return True
for i in range(2,101):
    if sushu(i):
        print(i)