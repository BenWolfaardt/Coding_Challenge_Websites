def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return (fibonacci(n-1) + fibonacci(n-2))
    
    
# Not recursive, but wanted to play #
    # fib = [0, 1]
    # for i in range(2, n+1):
    #     fib.append(fib[i-1] + fib[i-2])

    # return fib[n]     

n = int(input())
print(fibonacci(n))
