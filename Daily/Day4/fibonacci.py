#print the fibonacci series
def fibonacci(n):
    a, b = 0 ,1
    if n <= 0:
        print('pls enter a positive number')
    elif n == 1:
        print(a)
    else:
        for i in range(0,n):
            print(a)
            nxt = a + b
            a = b
            b = nxt
fibonacci(1)
fibonacci(0)
fibonacci(10)