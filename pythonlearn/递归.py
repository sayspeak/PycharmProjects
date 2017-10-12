def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return (fib(n - 1) + fib(n - 2))
print(fib(5))
def fib (n):
    a,b = 0,1
    count = 1
    while count < n:
        a,b = a, a+b
        count = count + 1
    print(a)