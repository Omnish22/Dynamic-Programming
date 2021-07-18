hash = [0,1]

def fib(n):
    if n < len(hash):
        return hash[n]
    else:
        value = fib(n-1)+fib(n-2)
        hash.append(value)
        return value


print(fib(6))
print(fib(100))

